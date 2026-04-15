from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer

log = core.getLogger()

class Monitor(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        self.last_bytes = 0

        # Request stats every 5 seconds
        Timer(5, self.request_stats, recurring=True)

    def request_stats(self):
        log.info("Requesting flow stats from switch...")
        req = of.ofp_stats_request(body=of.ofp_flow_stats_request())
        self.connection.send(req)

    def _handle_FlowStatsReceived(self, event):
        total_bytes = 0

        # Sum only valid flows (avoid noise/spikes)
        for stat in event.stats:
            if stat.packet_count > 0:
                total_bytes += stat.byte_count

        log.info("Total Bytes from switch: %s", total_bytes)

        # Calculate safe bandwidth
        delta_bytes = total_bytes - self.last_bytes

        if delta_bytes < 0:
            delta_bytes = 0  # prevent negative spikes

        bandwidth_kbps = (delta_bytes * 8) / (5 * 1000)  # 5 sec interval

        log.info("Estimated Bandwidth: %.2f Kbps", bandwidth_kbps)

        self.last_bytes = total_bytes


def launch():
    def start_switch(event):
        log.info("Monitoring switch %s", event.connection)
        Monitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)

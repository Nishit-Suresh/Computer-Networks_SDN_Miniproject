from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4

log = core.getLogger()

class Monitor(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        # Check for IP packet
        ip_packet = packet.find('ipv4')
        if ip_packet:
            log.info("IP Packet: %s -> %s", ip_packet.srcip, ip_packet.dstip)

def launch():
    def start_switch(event):
        log.info("Monitoring switch %s", event.connection)
        Monitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)

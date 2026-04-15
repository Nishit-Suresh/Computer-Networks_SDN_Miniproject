# 🚀 SDN-Based Network Utilization Monitoring using Mininet & POX

---

## 📌 Overview

This project demonstrates a Software Defined Networking (SDN) environment using:

- 🧠 POX Controller (Control Plane)
- 🌐 Mininet (Network Emulation)
- 📡 Wireshark (Packet Analysis)

The system monitors real-time network traffic and analyzes packet flow between hosts.

---

## 🧠 Objective

The goal of this project is to:

- Simulate an SDN network using Mininet
- Implement a custom POX controller (`monitor.py`)
- Monitor real-time packet flow (source → destination)
- Analyze traffic using Wireshark
- Observe flow table entries dynamically

---

## 🏗️ Network Architecture

The topology consists of:

- 1 Switch → `s1`
- 3 Hosts → `h1, h2, h3`
- Remote Controller → POX

```
h1 ----\
        \
         s1 ----> POX Controller
        /
h2 ----/
        \
         h3
```

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Start POX Controller

```bash
cd ~/pox
./pox.py forwarding.l2_learning monitor
```

---

### 🔹 Step 2: Run Mininet

```bash
sudo mn --topo single,3 --controller remote --mac
```

---

### 🔹 Step 3: Test Connectivity

```bash
pingall
```

✔ Expected: 0% packet loss

---

### 🔹 Step 4: Generate Traffic

```bash
iperf
```

✔ Used to measure bandwidth

---

### 🔹 Step 5: View Flow Tables

```bash
dpctl dump-flows
```

✔ Shows dynamically installed rules

---

### 🔹 Step 6: Run Wireshark

- Select interface: `any`
- Apply filters:
  - `icmp`
  - `tcp`

---

## 📊 Results & Observations

### 🔹 Mininet Output

- Successful host communication
- Zero packet loss
- Bandwidth measured via iperf

![Mininet Output](screenshots/mininet_output.png)

---

### 🔹 POX Monitoring Output

The custom controller logs IP traffic:

```
IP Packet: 10.0.0.1 -> 10.0.0.2
```

![POX Logs](screenshots/pox_logs.png)

---

### 🔹 Wireshark Analysis

Captured:

- ICMP packets (ping)
- TCP packets (iperf)

![Wireshark ICMP](screenshots/wireshark_icmp.png)
![Wireshark TCP](screenshots/wireshark_tcp.png)

---

### 🔹 Flow Table Entries

Flow rules installed dynamically:

- ICMP rules
- ARP rules
- Output port mapping

![Flow Table](screenshots/flow_table.png)

---

## 🔍 How It Works

1. Host sends packet → reaches switch  
2. Switch doesn’t know rule → sends to controller  
3. POX analyzes packet  
4. Installs flow rule  
5. Future packets bypass controller  

---

## 📌 Key Features

- ✅ Real-time traffic monitoring  
- ✅ Custom POX controller  
- ✅ Dynamic flow installation  
- ✅ Packet-level analysis  
- ✅ SDN architecture implementation  

---

## 🧠 Learning Outcomes

- Understanding SDN architecture  
- Controller-switch interaction  
- OpenFlow protocol basics  
- Network traffic analysis  
- Flow-based forwarding  

---

## 🧾 Conclusion

This project successfully demonstrates:

- Centralized control using SDN
- Real-time monitoring via POX
- Dynamic flow rule installation
- Packet-level analysis using Wireshark

It validates how SDN improves flexibility and visibility in modern networks.

---

## 📁 Repository Structure

```
.
├── monitor.py
├── README.md
└── screenshots/
    ├── mininet_output.png
    ├── pox_logs.png
    ├── wireshark_icmp.png
    ├── wireshark_tcp.png
    └── flow_table.png
```

---

## 📚 References

- Mininet Documentation  
- POX Controller Documentation  
- Wireshark Documentation  

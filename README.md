
# Dynamic Host Blocking System using SDN (POX + Mininet)

## Overview

This project demonstrates a Software Defined Networking (SDN) approach to dynamically monitor and control network traffic. Using a POX controller and Mininet emulator, the system detects hosts generating excessive traffic and blocks them by installing OpenFlow flow rules in real time.

---

## Objective

* Understand controller–switch interaction
* Implement OpenFlow match–action rules
* Detect abnormal traffic behavior
* Dynamically block suspicious hosts

---

## Technologies Used

* Mininet (network emulation)
* POX Controller (control logic)
* OpenFlow Protocol
* Ubuntu Linux

---

## Network Topology

A simple star topology is used:

* 1 switch (s1)
* 3 hosts (h1, h2, h3)
* Remote controller

All hosts are connected to a central switch, allowing traffic monitoring and control.

---

## Controller Logic

The controller handles `PacketIn` events and applies the following logic:

* Maintain packet count for each input port
* If packet count exceeds a threshold:

  * Install a high-priority flow rule with DROP action
* Otherwise:

  * Forward packets normally

This demonstrates dynamic network control using SDN principles.

---

## Setup Instructions

### Install Mininet

sudo apt update
sudo apt install mininet -y

### Install POX

git clone https://github.com/noxrepo/pox
cd pox

---

## Execution Steps

### Run Controller

cd ~/pox
sudo python3 pox.py controller.firewall_pox

### Run Topology

sudo mn --custom topology/topo.py --topo mytopo --controller=remote

### Verify Connectivity

pingall

---

## Test Scenarios

### Scenario 1: Normal Traffic

h1 ping h2
Result: Communication is successful

### Scenario 2: High Traffic

h1 ping -f h2
Result: Controller detects excessive traffic and installs a DROP rule

### Scenario 3: After Blocking

h1 ping h2
Result: Communication fails, confirming blocking

---

## Flow Table Verification

sudo ovs-ofctl dump-flows s1

Expected: A DROP rule for the offending port

---

## Results and Observations

* Normal traffic is forwarded correctly
* High traffic triggers blocking
* Flow rules are dynamically updated in the switch
* Network behavior changes based on controller logic

---

## Limitations

* Uses simple threshold-based detection
* Blocking is port-based rather than IP-based
* No deep packet inspection

---

## Future Enhancements

* IP/MAC-based filtering
* Advanced anomaly detection
* Multi-switch topology
* QoS and traffic prioritization

---

## Conclusion

This project shows how SDN enables centralized and programmable control of networks. Using POX and Mininet, abnormal traffic can be detected and controlled dynamically, demonstrating a practical approach to network security and management.

# SDN Link Failure Detection using POX

## SDN project using Mininet and POX controller to demonstrate topology monitoring, link failure detection, dynamic flow rule updates, and network recovery.

---

## Objective

This project demonstrates Software Defined Networking (SDN) using Mininet and POX controller. It focuses on:

* Monitoring topology changes
* Detecting link failures
* Updating flow rules dynamically
* Restoring connectivity
* Performance analysis

---

## Tools Used

* Mininet (Network Emulator)
* POX Controller
* OpenFlow Protocol
* Ubuntu (Linux Environment)

---

## Setup & Execution Steps

### 1. Clone POX Controller

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### 2. Run POX Controller

```bash
python3 pox.py openflow.of_01 --port=6633 openflow.discovery orange_project
```

### 3. Start Mininet (Open New Terminal)

```bash
sudo mn --topo linear,3 --mac --switch ovsk --controller remote
```

### 4. Test Connectivity

```bash
pingall
```

### 5. Simulate Link Failure

```bash
link s1 s2 down
pingall
```

### 6. Restore Link

```bash
link s1 s2 up
pingall
```

### 7. View Flow Table

```bash
dpctl dump-flows
```

### 8. Measure Throughput

```bash
h3 iperf -s &
h1 iperf -c h3
```

---

## Network Topology

Linear topology with 3 switches (s1–s3) and 3 hosts (h1–h3).

---

## Visualization of Switches and Hosts

h1 — s1 — s2 — s3 — h3
|
h2
       
---

## SDN Logic Implemented

* The controller handles **PacketIn events**
* Installs **flow rules dynamically**

### Match-Action Logic:

* **Match →** Source & Destination MAC
* **Action →** Forward / Flood

### Timeouts:

* **idle_timeout = 10 sec**
* **hard_timeout = 30 sec**

---

## Results & Screenshots

### 1. Controller Running

<img width="1213" height="648" alt="CN SS1" src="https://github.com/user-attachments/assets/99f10dc1-0d28-42d2-8374-bdba44d7d9b6" />

This screenshot shows the POX controller detecting topology and dynamically installing flow rules.
**Demonstrates:** Controller-switch interaction

---

### 2. Normal Network Operation

<img width="1209" height="585" alt="CN SS2" src="https://github.com/user-attachments/assets/82ad45c3-8b2a-472a-b183-9475a320bd34" />

`pingall → 0% dropped`
**Demonstrates:** Full connectivity

---

### 3. Link Failure Detection

<img width="1206" height="165" alt="CN SS3" src="https://github.com/user-attachments/assets/e33f7128-f6ac-499b-be4c-90cac34e7ff6" />

`link s1 s2 down → 66% dropped`
**Demonstrates:** Network failure behavior
(h1 becomes isolated)

---

### 4. Network Recovery

<img width="1206" height="165" alt="CN SS4" src="https://github.com/user-attachments/assets/b2fb08f3-dcee-49db-8351-e1a1cba6c164" />

`link s1 s2 up → 0% dropped`
**Demonstrates:** Restoration of connectivity

---

### 5. Flow Table (OpenFlow Rules)

<img width="1207" height="355" alt="CN SS5" src="https://github.com/user-attachments/assets/572009d9-07ae-40a1-8e98-2045e45a4f21" />

Shows:

* Match fields (dl_src, dl_dst)
* Actions (FLOOD / output)
* Timeouts

---

### 6. Performance Analysis (iperf)

<img width="1198" height="216" alt="CN SS6" src="https://github.com/user-attachments/assets/66cb9979-0e8c-4d61-8204-dc45be3bbff3" />

Throughput achieved:
**~37 Gbits/sec**
**Demonstrates:** Network performance

---

## Expected Output

- **pingall → 0% packet loss**
- **link down → ~66% packet loss**
- **link up → 0% packet loss**
- **iperf → ~30–40 Gbps**

---

## Observations

* Normal condition → 0% packet loss
* Failure condition → 66% packet loss
* Recovery → 0% packet loss
* Dynamic flow rule updates observed
* High throughput achieved using iperf

---

## Conclusion

The project successfully demonstrates:

* Centralized control using SDN
* Dynamic adaptation to link failures
* Efficient packet forwarding using flow rules
* Performance evaluation using network tools

---

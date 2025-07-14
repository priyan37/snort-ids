
# 🔥 Drop Action Demo Scenario

This guide demonstrates how to test and verify the **Drop Action** functionality using Snort and Python.

---

## 🎯 Objective
Detect ICMP (ping) attacks using Snort and automatically block the attacker’s IP address in **Windows Firewall** via a custom Python script (`drop.py`).

---

## 🛠 Environment Setup

| Component         | Details                    |
|--------------------|-----------------------------|
| IDS               | Snort (v2.9.20 for Windows) |
| Firewall          | Windows Defender Firewall   |
| Scripting         | Python 3.13                  |
| Victim Machine    | Windows 10                  |
| Attacker Machine  | Kali Linux (or any Linux VM)|

---

## 🚀 Steps to Demo

### ✅ Step 1: Configure Snort

1. Add the following rule to your `local.rules` file:  
   ```text
   alert icmp any any -> $HOME_NET any (msg:"⚠️ DETECTED ICMP Ping"; sid:1000001;)
   ```
2. In `snort.conf`, ensure:  
   ```text
   include $RULE_PATH/local.rules
   output alert_fast: alert.ids
   ```
3. Start Snort:  
   ```bash
   snort -i 1 -c C:\Snort\etc\snort.conf -l C:\Snort\log
   ```

---

### ✅ Step 2: Run the Drop Script

1. Start the `drop.py` script (Administrator privileges required):  
   ```bash
   python drop.py
   ```
2. The script monitors `alert.ids` and blocks IPs in real-time.

---

### ✅ Step 3: Simulate an Attack

1. On the attacker machine (Kali Linux):  
   ```bash
   ping <victim_IP>
   ```
2. Check the `drop.py` console for output:  
   ```text
   🚨 DROP script is running...
   🔒 Blocking IP: 192.168.1.10
   📋 Blocked IPs so far:
   • 192.168.1.10
   ```

---

## ✅ Expected Result

- The attacker’s IP is blocked by Windows Firewall.  
- Further pings or scans from the attacker fail.  
- The script lists all blocked IPs in the console.

---

## 🧪 Testing Notes
- To verify blocked IPs:  
  ```bash
  netsh advfirewall firewall show rule name=all
  ```
- Remove firewall rule for cleanup:  
  ```bash
  netsh advfirewall firewall delete rule name="Block_<attacker_IP>"
  ```

---

## 📄 Related Files
- [`drop.py`](./drop.py): Python script for automatic IP blocking


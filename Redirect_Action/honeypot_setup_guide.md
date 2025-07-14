# 🍯 Honeypot Setup Guide

This guide explains how to configure a basic honeypot to work with the deception proxy for redirecting attacker traffic.

---

## 🎯 Objective
Set up a honeypot on a Linux system to capture malicious traffic redirected from a victim machine running a deception proxy.

---

## 🛠 Environment Setup

| Component         | Details                     |
|--------------------|------------------------------|
| Honeypot Machine  | Linux (e.g., Ubuntu, Kali)   |
| Victim Machine    | Windows 10 (Proxy Enabled)   |
| Attacker Machine  | Kali Linux                   |
| Python Version    | 3.13                          |

---

## 🚀 Steps to Configure Honeypot

### ✅ Step 1: Prepare Honeypot Machine

1. Install Python 3 if not already installed:
   ```bash
   sudo apt update
   sudo apt install python3 -y
   ```

2. (Optional) Install common honeypot tools:

   * **Cowrie**: SSH/Telnet honeypot
   * **Dionaea**: Malware honeypot
   * For demo purposes, use a simple HTTP server.

---

### ✅ Step 2: Run a Simple HTTP Server

Run the following command on the honeypot machine:

```bash
sudo python3 -m http.server 80
```

This will serve as a basic honeypot listening on port 80.

---

### ✅ Step 3: Verify Network Connectivity

Ensure the victim machine can reach the honeypot.  
From the victim machine:

```bash
ping <honeypot_IP>
```

---

### ✅ Step 4: Redirect Traffic from Victim to Honeypot

The deception proxy on the victim machine forwards attacker traffic to the honeypot IP (configured in `deception_proxy.py`).

* Update `HONEYPOT_IP` in `deception_proxy.py` with your honeypot’s IP address.

Run the proxy script on the victim system:

```bash
python deception_proxy.py
```

---

### ✅ Step 5: Simulate Attack

1. On the attacker machine:

   ```bash
   curl http://<victim_IP>
   ```

2. The deception proxy will forward traffic to the honeypot.

3. The honeypot’s HTTP server will log the incoming requests.

---

## ✅ Expected Result

* Attacker traffic gets redirected to the honeypot.
* Honeypot logs show attacker interaction.
* Attacker receives fake responses from the honeypot.

---

## 📄 Related Files

* [`deception_proxy.py`](./deception_proxy.py): Python script for redirecting traffic


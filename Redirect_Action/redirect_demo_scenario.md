# 🔀 Redirect Action Demo Scenario

This guide demonstrates how to test and verify the **Redirect Action** functionality using the deception proxy and a honeypot system.

---

## 🎯 Objective
Redirect attacker traffic from the victim machine to a honeypot using a custom Python deception proxy (`deception_proxy.py`).

---

## 🚀 Steps to Demo

### ✅ Step 1: Configure Deception Proxy

1. On the victim machine, open `deception_proxy.py`.  
2. Set the honeypot IP and port:
   ```python
   HONEYPOT_IP = '192.168.56.103'  # Replace with honeypot IP
   HONEYPOT_PORT = 80              # Port on honeypot
   ```

3. Start the deception proxy:

   ```bash
   python deception_proxy.py
   ```

   The proxy listens on port 80 and forwards traffic to the honeypot.

---

### ✅ Step 2: Set Up Honeypot

1. On the honeypot machine, run a simple HTTP server:

   ```bash
   sudo python3 -m http.server 80
   ```

2. Alternatively, deploy a tool like **Cowrie** or **Dionaea** for a more advanced honeypot.

---

### ✅ Step 3: Simulate an Attack

1. From the attacker machine:

   ```bash
   curl http://<victim_IP>
   ```

2. The deception proxy will forward the HTTP request to the honeypot.

---

## ✅ Expected Result

* The attacker’s traffic is seamlessly redirected to the honeypot.
* Honeypot logs show attacker interaction.
* The attacker believes they’re interacting with the victim but actually communicates with the honeypot.

---

## 🧪 Verification

* Check `deception_proxy.log` for forwarded connections:

  ```text
  [INFO] Forwarding (Attacker -> Honeypot): 256 bytes
  ```

* On the honeypot, observe logs of incoming requests.

---

## 📄 Related Files

* [`deception_proxy.py`](./deception_proxy.py): Python script for redirecting traffic  
* [`honeypot_setup_guide.md`](./honeypot_setup_guide.md): Honeypot configuration guide


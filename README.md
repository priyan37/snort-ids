# 🛡️ Generative AI for Signature Creation in Snort IDS

This repository contains a Snort-based Intrusion Detection System (IDS) project enhanced with Python automation and AI-powered dynamic signature creation. It integrates Snort alerts with a MySQL database, implements real-time blocking and redirection of malicious traffic, and sets up a deception proxy for honeypot deployment.

---

## 📖 Project Overview

| Feature                     | Description                                          |
|------------------------------|------------------------------------------------------|
| 🐍 Python Integration        | Parse Snort alerts and push to MySQL database.      |
| 🛡️ Snort IDS                 | Detect malicious traffic in real-time.              |
| 🚫 IP Blocking                | Automatically block attacker IPs using firewall.    |
| 🔀 Traffic Redirection        | Redirect attackers to a honeypot (deception proxy). |
| 📊 Data Storage               | Log alerts in a structured MySQL table.             |

---

## 📂 Repository Structure

```
/Snort-IDS-Project
│
├── Alert_to_Database/
│   ├── snort_to_sql.py
│   ├── MySQL_Setup_Guide.md
│
├── Drop_Action/
│   ├── drop.py
│   ├── drop_demo_scenario.md
│
├── Redirect_Action/
│   ├── deception_proxy.py
│   ├── honeypot_setup_guide.md
│   ├── redirect_demo_scenario.md
│
├── Snort_Installation/
│   ├── Linux_Snort_Installation.md
│   ├── Windows_Snort_Installation.md
│   ├── local.rules
│   ├── snort.conf
│
├── README.md
└── LICENSE
```

---

## 🚀 Quick Start

### ✅ 1. Install Snort
- Follow the installation guide for your platform:  
  - [Linux Installation](./Snort_Installation/Linux_Snort_Installation.md)  
  - [Windows Installation](./Snort_Installation/Windows_Snort_Installation.md)

### ✅ 2. Configure MySQL
- Set up the database to store Snort alerts:  
  [MySQL Setup Guide](./Alert_to_Database/MySQL_Setup_Guide.md)

### ✅ 3. Run Snort
Start Snort in IDS mode and generate test alerts.

### ✅ 4. Automate Actions
- **Push alerts to DB**: [snort_to_sql.py](./Alert_to_Database/snort_to_sql.py)  
- **Block Attacker IPs**: [drop.py](./Drop_Action/drop.py)  
- **Redirect Traffic to Honeypot**: [deception_proxy.py](./Redirect_Action/deception_proxy.py)  

---

## 🧪 Demo Scenarios

| Action              | Guide                                                   |
|----------------------|----------------------------------------------------------|
| 🚫 IP Blocking       | [Drop Demo Scenario](./Drop_Action/drop_demo_scenario.md)|
| 🔀 Traffic Redirect  | [Redirect Demo Scenario](./Redirect_Action/redirect_demo_scenario.md)|
| 🍯 Honeypot Setup    | [Honeypot Setup Guide](./Redirect_Action/honeypot_setup_guide.md)|

---

## 🛠 Technologies Used

- **Snort IDS** (v2.9.20 for Windows/Linux)
- **Python 3.13**
- **MySQL Database**
- **Windows Defender Firewall**
- **Linux Firewall (iptables)**

---

## 📜 License
This project is under a custom license that allows personal and educational use only. Public forks and redistribution are prohibited without permission explicitly from me !

---

## 🙌 Credits
Developed by **Priyadharshan Vadivel**  
Under the guidance of:  
- **Dr. Ghanshyam S. Bopche**  
- **Nilin Prabhaker, Ph.D. Scholar**  
- **Abby S. P., Research Scholar**

# 🪟 Windows Snort Installation Guide

This guide provides step-by-step instructions to install and configure **Snort IDS** on a Windows machine.

---

## 🎯 Objective
Install Snort on Windows for intrusion detection and configure it to monitor network traffic.

---

## 🛠 Supported Environment

| Component         | Details                     |
|--------------------|------------------------------|
| OS                | Windows 10 (64-bit)          |
| Snort Version     | Snort 2.9.20                 |
| User Privileges   | Administrator                |

---

## 🚀 Installation Steps

### ✅ Step 1: Download Snort
1. Go to the [Snort Downloads Page](https://www.snort.org/downloads).
2. Download **Snort 2.9.20 for Windows (64-bit)**.
3. Extract the ZIP file to `C:\Snort`.

---

### ✅ Step 2: Set Up Environment Variables
1. Add `C:\Snort\bin` to the system PATH:
   - Open **System Properties** → **Advanced** → **Environment Variables**.
   - Under **System Variables**, edit `Path` and add:
     ```
     C:\Snort\bin
     ```

2. Verify Snort is accessible:  
   Open Command Prompt and run:
   ```cmd
   snort -V
   ```

---

### ✅ Step 3: Configure Snort

1. Navigate to `C:\Snort\etc` and open `snort.conf` for editing.
2. Set network variables:

   ```text
   var HOME_NET 192.168.1.0/24
   var EXTERNAL_NET any
   ```

3. Include your custom rules:

   ```text
   include $RULE_PATH\local.rules
   ```

4. Create `C:\Snort\rules\local.rules` and add a sample rule:

   ```text
   alert icmp any any -> $HOME_NET any (msg:"ICMP Detected"; sid:1000001;)
   ```

---

### ✅ Step 4: Test Configuration

Run Snort in test mode:

```cmd
snort -i 1 -c C:\Snort\etc\snort.conf -T
```

---

## 🧪 Example Usage

* Start Snort in IDS mode:

  ```cmd
  snort -i 1 -c C:\Snort\etc\snort.conf -l C:\Snort\log
  ```

* Perform a ping or port scan from another machine to trigger alerts.
* Check logs in `C:\Snort\log`.

---

## 📝 Troubleshooting

| Issue                      | Solution                                                      |
| -------------------------- | ------------------------------------------------------------- |
| **WinPcap not installed**  | Download and install from [npcap.org](https://npcap.org).     |
| **Permission errors**      | Run Command Prompt as Administrator.                          |
| **Interface not detected** | Run `snort -W` to list interfaces and choose the correct one. |

---

## 📄 Related Files

* [`snort.conf`](./snort.conf): Example configuration file  
* [`local.rules`](./local.rules): Custom rules file

---

## ✅ Expected Result

* Snort runs successfully on Windows.  
* Alerts are generated for suspicious traffic and logged in `C:\Snort\log`.


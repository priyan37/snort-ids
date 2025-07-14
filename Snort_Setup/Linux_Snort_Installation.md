
# 🐧 Linux Snort Installation Guide

This guide provides step-by-step instructions to install and configure **Snort IDS** on a Linux machine.

---

## 🎯 Objective
Install Snort on a Linux system for intrusion detection and configure it to monitor network traffic.

---

## 🛠 Supported Environment

| Component         | Details                     |
|--------------------|------------------------------|
| OS                | Ubuntu 20.04 LTS / Kali Linux|
| Snort Version     | Snort                     |
| User Privileges   | Root/Sudo                    |

---

## 🚀 Installation Steps

### ✅ Step 1: Update the System
```bash
sudo apt update && sudo apt upgrade -y
```

---

### ✅ Step 2: Install Dependencies

```bash
sudo apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev
sudo apt install -y liblzma-dev openssl libssl-dev wget
```

---

### ✅ Step 3: Install DAQ

Download and install DAQ (Data Acquisition library) for packet I/O:

```bash
wget https://www.snort.org/downloads/snort/daq-2.0.7.tar.gz
tar -xvzf daq-2.0.7.tar.gz
cd daq-2.0.7
./configure && make && sudo make install
```

---

### ✅ Step 4: Install Snort

Download the Snort source:

```bash
wget https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz
tar -xvzf snort-2.9.20.tar.gz
cd snort-2.9.20
./configure --enable-sourcefire && make && sudo make install
```

Verify installation:

```bash
snort -V
```

---

### ✅ Step 5: Configure Snort

1. Create necessary directories:

   ```bash
   sudo mkdir /etc/snort
   sudo mkdir /etc/snort/rules
   sudo mkdir /var/log/snort
   sudo mkdir /usr/local/lib/snort_dynamicrules
   ```

2. Copy configuration files:

   ```bash
   sudo cp etc/* /etc/snort
   ```

3. Update `snort.conf`:

   * Set network variables:

     ```bash
     var HOME_NET 192.168.1.0/24
     var EXTERNAL_NET any
     ```

   * Include your custom rules:

     ```bash
     include $RULE_PATH/local.rules
     ```

---

### ✅ Step 6: Test Snort

Run Snort in test mode:

```bash
sudo snort -T -c /etc/snort/snort.conf
```

---

## 🧪 Example Usage

* Run Snort in packet sniffing mode:

  ```bash
  sudo snort -A console -i eth0 -c /etc/snort/snort.conf
  ```

* Test with a ping or port scan from another machine.

---


## ✅ Expected Result

* Snort runs successfully on the Linux system.  
* Alerts are generated for detected suspicious traffic.

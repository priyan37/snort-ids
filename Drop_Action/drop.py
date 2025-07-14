
import os
import time
import subprocess
import re

alert_file = "C:\\Snort\\log\\alert.ids"
blocked_ips = set()

print("🚨 DROP script is running...\n")

def extract_ips_from_alerts(content):
    ips = []
    for line in content:
        match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3}) ->', line)
        if match:
            ip = match.group(1)
            if ip not in blocked_ips:
                ips.append(ip)
    return ips

while True:
    if not os.path.exists(alert_file):
        print("⚠️ alert.ids not found. Waiting...")
        time.sleep(5)
        continue

    with open(alert_file, "r") as file:
        lines = file.readlines()

    new_ips = extract_ips_from_alerts(lines)

    for ip in new_ips:
        try:
            print(f"🔒 Blocking IP: {ip}")
            subprocess.run([
                "netsh", "advfirewall", "firewall", "add", "rule",
                f"name=Block_{ip}", "dir=in", "action=block", f"remoteip={ip}"
            ], check=True)
            blocked_ips.add(ip)
        except Exception as e:
            print(f"⚠️ Error blocking {ip}: {e}")

    print("\n📋 Blocked IPs so far:")
    print("----------------------------------------")
    for b_ip in blocked_ips:
        print(f"• {b_ip}")
    print("----------------------------------------")

    time.sleep(5)

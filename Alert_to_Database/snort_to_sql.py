import mysql.connector
import os

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Add password if you set one
    database="snort_alerts"
)
cursor = conn.cursor()

# Define the alert file location
alert_file_path = "C:\\Snort\\log\\alert.fast"

# Check if the file exists
if not os.path.exists(alert_file_path):
    print("❌ alert.fast file not found.")
    exit()

# Read file content
with open(alert_file_path, "r") as file:
    lines = file.readlines()

# Parse each alert
for i in range(len(lines)):
    line = lines[i]
    if "[**]" in line and "Testing Msg" in line:
        parts = line.split()
        signature = parts[2] + " " + parts[3]
        message = " ".join(parts[4:])
        priority = 1
        src_ip, dst_ip = "0.0.0.0", "0.0.0.0"

        for j in range(i+1, min(i+6, len(lines))):
            if "->" in lines[j]:
                ip_line = lines[j].strip()
                ip_parts = ip_line.split("->")
                src_ip = ip_parts[0].split()[-1]
                dst_ip = ip_parts[1].strip()
                break

        # Insert into MySQL
        cursor.execute("""
            INSERT INTO alerts (signature, priority, src_ip, dst_ip, message)
            VALUES (%s, %s, %s, %s, %s)
        """, (signature, priority, src_ip, dst_ip, message))

conn.commit()
cursor.close()
conn.close()
print("✅ Alerts inserted into MySQL!")


# 🗄️ MySQL Setup Guide for Snort Alerts

This guide helps you configure a MySQL database to store Snort IDS alerts.

---

## ✅ Prerequisites
- XAMPP installed (includes Apache & MySQL)
- Python 3.13 installed
- `mysql-connector-python` library installed

---

## 🚀 Step 1: Install XAMPP
1. Download XAMPP from [Apache Friends](https://www.apachefriends.org).
2. Install XAMPP and ensure **MySQL** is selected during installation.
3. Open the XAMPP Control Panel:
   - Start **Apache** (use port 8080 if port 80 is occupied).
   - Start **MySQL**.
4. Access phpMyAdmin:
   - [http://localhost/phpmyadmin](http://localhost/phpmyadmin)  
   - Or [http://localhost:8080/phpmyadmin] if Apache runs on port 8080.

---

## 🗃️ Step 2: Create Database and Table
1. In phpMyAdmin, create a database:  
   **Database name**: `snort_alerts`
2. Create a table named `alerts` with the following schema:

```sql
CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signature VARCHAR(255),
    priority INT,
    src_ip VARCHAR(45),
    dst_ip VARCHAR(45),
    message TEXT
);
```

Alternatively, import the `alerts_table_schema.sql` file in this folder using phpMyAdmin.

---

## 🐍 Step 3: Install Python MySQL Connector
Install the connector library with:  
```bash
pip install mysql-connector-python
```

---

## ⚡ Step 4: Verify Setup
1. Trigger a Snort alert (e.g., ping or scan the victim machine).  
2. Run the `snort_to_sql.py` script in this folder:  
```bash
python snort_to_sql.py
```
3. Check phpMyAdmin under `snort_alerts.alerts` to see if alerts are stored.

---

## 📄 Related Files
- [`alerts_table_schema.sql`](./alerts_table_schema.sql) – SQL schema for table creation
- [`snort_to_sql.py`](./snort_to_sql.py) – Python script for inserting alerts into MySQL

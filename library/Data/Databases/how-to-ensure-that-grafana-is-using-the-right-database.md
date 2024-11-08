---
title: "How to ensure that Grafana is using the right database"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How can I make sure that Grafana is using the Postgres and not SQLite

# Prompt

To verify that Grafana is using PostgreSQL instead of the default SQLite database, you may need to check and configure some settings in the Grafana configuration file. Here’s how you can do that:

### Step 1: Check the Current Data Source

1. **Access Grafana Web Interface:**
   Open your web browser and go to `http://<your_vm_ip>:3000` and log in.

2. **Navigate to Data Sources:**
   Go to **Configuration** -> **Data Sources**. Here, you should see the configured data sources.

3. **Verify Database Type:**
   If you see PostgreSQL listed as a data source, it indicates that Grafana is set up to use PostgreSQL. If you see SQLite, you’ll need to change it.

### Step 2: Configure Grafana to Use PostgreSQL

1. **Edit Grafana Configuration:**
   Open the Grafana configuration file, typically located at `/etc/grafana/grafana.ini`:
   ```bash
   sudo nano /etc/grafana/grafana.ini
   ```

2. **Locate Database Configuration:**
   Look for the `[database]` section. It should have settings like this:
   ```plaintext
   [database]
   # You can configure the database here
   type = sqlite3
   ```

3. **Change Database Type to PostgreSQL:**
   Modify the settings to use PostgreSQL:
   ```plaintext
   [database]
   type = postgres
   host = localhost:5432
   name = your_database_name
   user = grafana
   password = WX9uoPXpyBas6wwyjQsR
   ```

4. **Save and Exit:**
   Save the changes (CTRL + X, then Y, then Enter) and exit the text editor.

### Step 3: Restart Grafana

After making changes to the configuration file, restart the Grafana service to apply the changes:
```bash
sudo systemctl restart grafana-server
```

### Step 4: Verify Connection

1. **Check Logs for Errors:**
   You can check the Grafana logs for any errors or confirmation that it is connected to PostgreSQL:
   ```bash
   sudo journalctl -u grafana-server -f
   ```

2. **Revisit Data Sources:**
   Go back to **Configuration** -> **Data Sources** in the Grafana web interface and confirm that PostgreSQL is set up correctly.

### References
- [Grafana Configuration Documentation](https://grafana.com/docs/grafana/latest/administration/configuration/#database)
- [Using PostgreSQL with Grafana](https://grafana.com/docs/grafana/latest/datasources/postgres/)
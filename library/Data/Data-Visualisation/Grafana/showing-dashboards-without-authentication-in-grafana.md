---
title: "Showing dashboards without authentication in Grafana"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Do I need to change any settings to allow public dashboards to be created in Grafana (that can be accessed without authentication)?

# Output

Yes, in order to make Grafana dashboards publicly accessible without requiring authentication, you need to adjust a few settings. Here’s how to configure it:

### 1. **Enable Anonymous Access**
   You will need to enable anonymous access in Grafana's configuration file (`grafana.ini`).

   - Locate and open the `grafana.ini` file. It’s usually located in `/etc/grafana/grafana.ini` (Linux) or wherever Grafana is installed.
   
   - Find the `[auth.anonymous]` section and modify the following settings:
   
     ```ini
     [auth.anonymous]
     enabled = true
     org_name = YourOrgName  # Optional: Specify the organization for anonymous access.
     org_role = Viewer       # Set the default role for anonymous users.
     ```

   - Save and close the file.

### 2. **Restart Grafana**
   After modifying the configuration file, restart Grafana for the changes to take effect:

   ```bash
   sudo systemctl restart grafana-server
   ```

### 3. **Set Dashboard Permissions**
   After enabling anonymous access, you need to configure permissions on specific dashboards or folders to allow anonymous users to view them.

   - Go to the Grafana dashboard you want to make public.
   - Click on the **Settings (gear icon)** of the dashboard.
   - Under **Permissions**, click **Add Permission for** and select **Anonymous** from the dropdown.
   - Assign the **Viewer** role to anonymous users and save the permissions.

### 4. **Make Sure to Disable Authentication for Proxies (Optional)**
   If you have Grafana behind a reverse proxy, ensure the proxy is not forcing authentication for anonymous users. You may need to modify your proxy settings if necessary.

After following these steps, users will be able to access your dashboards without logging in, using a public URL.

Be aware that anonymous access grants viewing privileges only, so if you're making dashboards public, make sure to limit the role to "Viewer" to avoid any unwanted modifications.
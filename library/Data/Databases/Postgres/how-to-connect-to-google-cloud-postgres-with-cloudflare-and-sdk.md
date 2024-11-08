---
title: "How to connect to Google Cloud Postgres with Cloudflare and SDK"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are using a Cloudflare Tunnel to connect to your GCP VM where PostgreSQL is running inside a Docker container. You also have the Google Cloud SDK installed on your computer and want to connect to the database using tools like DBeaver.

### Recommended Methods to Connect to Dockerized PostgreSQL via Cloudflare Tunnel

To connect to PostgreSQL securely via Cloudflare Tunnel, follow these steps:

### Method 1: **Set Up Cloudflare Tunnel for PostgreSQL**
1. **Configure Cloudflare Tunnel for PostgreSQL**
   - Ensure that your Cloudflare Tunnel is configured to route PostgreSQL traffic to your GCP VM.
   - **Example Configuration**: Modify your `config.yml` file for the tunnel (where `<tunnel-id>` is your unique tunnel identifier):
     ```yaml
     tunnel: <tunnel-id>
     ingress:
       - hostname: postgres.mydomain.com
         service: tcp://localhost:5432
       - service: http_status:404
     ```
   - Make sure you have registered a DNS entry (e.g., `postgres.mydomain.com`) that points to your Cloudflare Tunnel.

2. **Run Cloudflare Tunnel Locally**
   - Start your Cloudflare Tunnel client (`cloudflared`) on your local machine to create a TCP tunnel:
     ```bash
     cloudflared access tcp --hostname postgres.mydomain.com --url localhost:5432
     ```
   - This command forwards your local port `5432` to the PostgreSQL port on your VM, enabling you to connect as if it were running locally.

3. **Connect DBeaver or Other SQL Clients**
   - **In DBeaver**, create a new PostgreSQL connection:
     - **Host**: `localhost`
     - **Port**: `5432`
     - **Database**: `<database-name>`
     - **Username**: `<postgres-username>`
     - **Password**: `<password>`
   - Now, you should be able to connect securely to PostgreSQL using the Cloudflare Tunnel without exposing your database port to the internet.

### Method 2: **SSH Tunnel via Google Cloud SDK (Alternative Approach)**
1. **Set Up SSH Access to Your VM**
   - Ensure that your GCP VM allows SSH access. You can SSH to your VM using:
     ```bash
     gcloud compute ssh <instance-name> --zone <zone>
     ```

2. **Create an SSH Tunnel from Your Local Machine**
   - Use the following command to create an SSH tunnel, forwarding your local port `5432` to the PostgreSQL container on your VM:
     ```bash
     gcloud compute ssh <instance-name> --zone <zone> -- -L 5432:localhost:5432
     ```
   - **Note**: Ensure that your PostgreSQL Docker container is configured to listen on `localhost` (`0.0.0.0`) so that it can accept the forwarded connection.

3. **Connect DBeaver or Other SQL Clients**
   - **In DBeaver**, set up the connection as:
     - **Host**: `localhost`
     - **Port**: `5432`
     - **Database**: `<database-name>`
     - **Username**: `<postgres-username>`
     - **Password**: `<password>`
   - DBeaver will now connect to your PostgreSQL instance via the secure SSH tunnel.

### Additional Security Tips:
- **Enable SSL/TLS for PostgreSQL Connections**: If you want to further encrypt your database connections, configure PostgreSQL to use SSL/TLS.
- **Use `cloudflared` with Access Policies**: Protect access by requiring login through Cloudflare Access, which can enforce additional authentication layers (e.g., SSO, MFA).
- **Limit Connections in PostgreSQL Configuration**: Modify `pg_hba.conf` to accept connections only from `localhost` or trusted networks.

### Summary of Connection Steps:
1. **Set up Cloudflare Tunnel**: Route PostgreSQL traffic through your Cloudflare Tunnel.
2. **Run Local Tunnel**: Use `cloudflared` or `gcloud` to securely forward connections to `localhost:5432`.
3. **Configure DBeaver**: Connect to PostgreSQL as if it were local, using `localhost` as the host.

Using these methods, you can securely connect to your Dockerized PostgreSQL instance on the GCP VM without opening any public ports, ensuring that your database remains protected while you access it conveniently from tools like DBeaver.
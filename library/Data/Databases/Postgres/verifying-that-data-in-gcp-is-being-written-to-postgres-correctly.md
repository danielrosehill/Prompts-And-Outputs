---
title: "Verifying that data in GCP is being written to Postgres correctly"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I want to verify that the data that I'm writing to my new Outline KM is being written onto Postgres. The Postgres, like Outline, is a Docker container. Both are hosted on a Google Cloud server. I have created one note to use to verify that the data is being written to the database. Can you suggest a guide on how I can do this using PSQL? I would like to reboot the VM during the test to verify that the data is persistent**Summary:** You want a guide to verify that data from Outline KM is being correctly stored in the PostgreSQL database, which is running in a Docker container. You also want to reboot the VM to confirm that the data is persistent.

### Guide to Verify Data Persistence in PostgreSQL for Outline KM

To verify that your Outline KM data is being stored in PostgreSQL, and that the data remains persistent across VM reboots, follow the steps below.

### Step 1: Verify That Your Note Is Saved in Outline KM

1. **Create a Note in Outline KM**
   - Make sure the note has some identifiable content (e.g., "Test Note for Verification").
   - Remember the title or content so you can search for it in PostgreSQL.

### Step 2: Connect to the PostgreSQL Container Using `psql`

1. **Connect to Your Google Cloud VM via SSH**
   - Use the `gcloud` command to SSH into your VM:
     ```bash
     gcloud compute ssh <vm-instance-name> --zone <zone>
     ```
   - Replace `<vm-instance-name>` and `<zone>` with your VM's details.

2. **Access the PostgreSQL Container**
   - List your running Docker containers to find the PostgreSQL container ID or name:
     ```bash
     docker ps
     ```
   - Use the following command to connect to the PostgreSQL container:
     ```bash
     docker exec -it <postgres-container-id> /bin/bash
     ```
   - Replace `<postgres-container-id>` with the ID or name of the PostgreSQL container.

3. **Log In to PostgreSQL Using `psql`**
   - Once inside the container, use `psql` to connect to the Outline database:
     ```bash
     psql -U outline -d outline
     ```
   - Replace `outline` (username and database name) if your configuration uses different names.

### Step 3: Check if the Data is Stored in the Database

1. **Find the Table Storing Notes**
   - Outline KM uses a relational structure to store documents (notes). Typically, notes would be stored in a table like `documents` or `notes`. You can list all tables to find the relevant one:
     ```sql
     \dt
     ```

2. **Query the Table for Your Note**
   - To confirm that your note is being saved, run a query to search for it using the title or part of the content. For example:
     ```sql
     SELECT * FROM documents WHERE title LIKE '%Test Note for Verification%';
     ```
   - **Note**: The actual column names and table structure might differ, so if this query does not return results, list the columns in the `documents` table to identify which fields to search:
     ```sql
     \d documents;
     ```

### Step 4: Reboot the VM and Verify Data Persistence

1. **Exit PostgreSQL and Docker**
   - Use `\q` to exit `psql` and `exit` to leave the Docker container.

2. **Reboot the VM**
   - Use the following command to reboot your Google Cloud VM:
     ```bash
     sudo reboot
     ```

3. **Reconnect to the VM**
   - After the VM reboots, SSH back into it:
     ```bash
     gcloud compute ssh <vm-instance-name> --zone <zone>
     ```

4. **Recheck the PostgreSQL Database**
   - Follow the previous steps to connect to the PostgreSQL container and verify the note still exists:
     ```bash
     docker exec -it <postgres-container-id> /bin/bash
     psql -U outline -d outline
     SELECT * FROM documents WHERE title LIKE '%Test Note for Verification%';
     ```

### Step 5: Confirm Data Persistency

If your note is still present in the database after the reboot, this confirms that:

1. **Data Is Stored Persistently in PostgreSQL**: 
   - The PostgreSQL container's volume is properly configured to store data persistently on the host machine.

2. **VM Reboots Do Not Affect Data**: 
   - Your VM's setup ensures that data remains accessible and isn't lost during restarts.

### Optional Step: Verify Docker Volume Persistence

To further ensure that PostgreSQL data is being stored persistently, you can check Docker volumes:

1. **Inspect Docker Volumes**
   - List Docker volumes on your VM:
     ```bash
     docker volume ls
     ```
   - Check the details of the volume bound to `/var/lib/postgresql/data`:
     ```bash
     docker volume inspect <postgres-volume-name>
     ```
   - This will show where on the host system the data is stored, ensuring it’s mounted correctly.

### Summary:
1. **Create a test note** in Outline KM to verify.
2. **Connect to PostgreSQL** using `psql` within the Docker container to confirm the note is saved.
3. **Reboot the VM** to ensure the setup persists data across restarts.
4. **Recheck the database** after the reboot to verify data persistence.
5. Optionally, **inspect Docker volumes** to confirm persistent storage is correctly configured.

Following these steps will help you confirm that data from Outline KM is correctly written to PostgreSQL and that it remains persistent, even after a VM reboot.
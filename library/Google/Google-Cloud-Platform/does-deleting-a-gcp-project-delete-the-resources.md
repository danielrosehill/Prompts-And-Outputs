---
title: "Does deleting a GCP project delete the resources"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking if deleting a Google Cloud Project will also delete all resources associated with it.

### Deleting a Google Cloud Project: What Happens to Resources

Yes, **deleting a Google Cloud Project will delete all resources associated with it**. When you delete a project in Google Cloud, the following happens:

1. **Resources Are Marked for Deletion**
   - All resources (e.g., **VM instances, storage buckets, databases, Cloud SQL instances, network configurations, Kubernetes clusters, etc.**) under the project will be marked for deletion.
   - This includes **compute resources**, **persistent disks**, **network components**, **IP addresses**, and more.

2. **Billing Stops**
   - Billing for the project will stop immediately, and you will no longer incur charges for any resources tied to the project.
   - Any resources that are **billing-enabled** will cease to accrue costs once the project is deleted.

3. **30-Day Grace Period for Data Recovery**
   - Google Cloud provides a **30-day grace period** after you initiate the project deletion. During this period, the project is **scheduled for deletion** but not completely erased. You can **restore the project** and its resources within this 30-day window.
   - **After 30 days**, the project and all associated resources are permanently deleted, and recovery is not possible.

4. **Service Accounts and Permissions**
   - All **service accounts**, **IAM policies**, and **permissions** related to the project will be deleted.
   - Any **API keys** or **credentials** associated with the project will no longer work once the project is deleted.

### Resources That Will Be Deleted
When a Google Cloud Project is deleted, the following resources, among others, will be deleted:

- **Compute Engine**: Virtual machine instances, persistent disks, snapshots, and images.
- **Cloud Storage**: Buckets and all files within them.
- **Cloud SQL**: Databases and instances.
- **BigQuery**: Datasets and tables.
- **Kubernetes Engine (GKE)**: Clusters and associated resources.
- **Cloud Functions**: All deployed functions.
- **Pub/Sub**: Topics and subscriptions.
- **VPC Networks**: Custom networks, firewalls, and static IPs.
- **IAM Policies**: Roles, permissions, and service accounts specific to the project.

### How to Delete a Project Safely

1. **Check Resources Before Deleting**
   - Before you delete a project, list all the resources associated with it to ensure there are no critical or valuable assets that might be lost.
   - You can use the **Google Cloud Console** or the **`gcloud` CLI** to view resources:
     ```bash
     gcloud projects list
     ```

2. **Export Data and Backups**
   - Make sure to **back up any critical data** or export it to another project if you need to retain specific information or resources. For example, export Cloud SQL databases, download Cloud Storage buckets, or create snapshots of VMs.

3. **Delete or Migrate Specific Resources (If Needed)**
   - If there are specific resources you want to keep, **migrate them to another project**. This might include **storage buckets**, **VM images**, or **data** stored in databases.

4. **Delete the Project**
   - You can delete the project via the **Google Cloud Console**:
     - Navigate to **"IAM & Admin" > "Manage Resources"**.
     - Find the project you want to delete, select it, and click **"Delete"**.
     - Confirm the deletion by typing the project ID.
   - **Via `gcloud` CLI**:
     ```bash
     gcloud projects delete <PROJECT_ID>
     ```

### Things to Consider Before Deletion
- **Dependencies**: Ensure no other projects or services rely on the resources of the project you're deleting.
- **Data Loss**: Permanent data loss will occur after the 30-day grace period. Ensure backups are secured before initiating the deletion.
- **Billing Accounts**: Verify that deleting a project will not affect other projects connected to the same billing account.

### Summary
Deleting a Google Cloud Project will **delete all resources** associated with it, including VMs, databases, storage, networks, and more. A **30-day grace period** allows for restoration if needed. Ensure to **back up data** and verify dependencies before proceeding with project deletion.
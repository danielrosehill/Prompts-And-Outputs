---
title: Recommendations to secure publicly accessible Grafana dashboards
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


For secure public access to your Grafana dashboards without authentication, where users can view your dashboards without logging in, you can still take several measures to minimize security risks:

1. Anonymous Access with Limited Permissions:

Enable anonymous access in Grafana, but configure it to give read-only permissions. This ensures that users can only view the dashboard and not make any changes.

In Grafana’s settings, set allow_sign_up to false to prevent users from creating new accounts and restrict their access only to viewing dashboards.



2. Public Sharing of Specific Dashboards:

Use Grafana’s public sharing links. These links can provide public access to specific dashboards without exposing your entire Grafana instance.

Ensure that the sharing links are read-only, and consider enabling time-limited access to further control how long the dashboard is publicly available.



3. Embed in a Secure Website:

Embed the Grafana dashboard into a secure website using iframe or similar embedding methods. This lets you control the external environment around the dashboard and manage security features such as HTTPS, even if Grafana's internal security is limited.

Consider using content security policies (CSP) on the embedding site to restrict where the iframe can be displayed, reducing clickjacking risks.



4. Rate Limiting and Throttling:

To prevent abuse or attacks, set up rate limits for public access. This can help mitigate risks like DDoS attacks or high-frequency requests that could overload your Grafana server.



5. Restrict Data Sources for Public Access:

Ensure the data available on the publicly shared dashboards is not sensitive. Only include data that is safe for public consumption.

Use read-only database users or query permissions to restrict the data source queries for public dashboards, so users can’t manipulate or query unintended datasets.



6. Separate Public and Private Dashboards:

Host public dashboards in a separate organization or folder in Grafana, isolated from your private or sensitive dashboards. This way, even if the public-facing dashboards are exposed, your sensitive data remains protected.



7. Limit Resource Consumption:

Use lightweight visualizations for your public dashboards. Avoid complex queries or expensive visualizations that could lead to performance issues, especially if many users access the dashboard at once.



8. Monitor and Log Public Access:

Set up logging and monitoring to track public access. While the users won’t be authenticated, you can still log IP addresses, access times, and the frequency of access to detect suspicious activity.




By carefully controlling the scope of what is shared and minimizing possible attack vectors, you can provide secure public access to your Grafana dashboards without requiring authentication, while still protecting your underlying systems and data.


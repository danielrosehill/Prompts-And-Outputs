---
title: "Crowdsourced shelter monitoring for Jerusalem"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you think of any platforms or tools that could be used for crowdsourced geographic information gathering and sharing? Specifically: where I live in Jerusalem the public bomb shelters are often in poor condition or not available during wartime. Given how controversial Israel is, it is likely that if a crowdsourced reporting tool were made available it would be subjected to abuse and hate and hacking. Despite these limitations, can you think of any way it might be possible to stand up a platform that would allow local residents to share information such as the accessability of the shelters, their condition, etc. And perhaps it could also be used to relay concerns to the authorities (for shelters found non operational etc)?

# Output

Creating a platform for **crowdsourced geographic information gathering** in a highly sensitive environment like Jerusalem presents challenges in terms of **security**, **resilience against abuse**, and **protecting participants**. However, there are existing platforms and technical strategies that could be adapted to meet these requirements while mitigating risks. Here’s how you might proceed:

### Potential Platforms and Tools

1. **Ushahidi**
   - **Overview**: Ushahidi is an open-source platform specifically designed for crowdsourcing crisis information. It allows users to report events via SMS, email, web forms, or a dedicated mobile app, and map those reports in real-time.
   - **Why It Could Work**: 
     - Ushahidi has been used in conflict zones and during natural disasters to collect and map important information like shelter conditions.
     - It has integrated **moderation tools** to help manage incoming reports and filter out inappropriate content.
     - **Deployment**: You can self-host Ushahidi to ensure control over the data and enhance security.
   - **Challenges**: You would need a strong community moderation system to prevent misuse or abuse of the reporting feature, especially given the sensitive political climate.

2. **OpenStreetMap (OSM) with Custom Overlays**
   - **Overview**: OpenStreetMap is an open-source mapping project that allows anyone to add and edit geographical data.
   - **Customization**:
     - You can create a **custom overlay** to mark shelters and add a plugin that enables users to provide updates on the condition and accessibility of each shelter.
     - Users can leave **comments** or rate each shelter’s condition.
   - **Deployment**: This can be hosted on your own infrastructure using tools like **Mapbox** or **Leaflet** for greater customization.
   - **Security Considerations**:
     - While OSM itself has no integrated moderation, by hosting it yourself you could add additional tools for user verification (e.g., phone-based authentication) and moderation to avoid trolling or vandalism.

3. **ArcGIS Hub Community Engagement Platform**
   - **Overview**: **ArcGIS Hub** is a platform for community engagement built by ESRI. It provides tools to create a **public-facing dashboard** for gathering geographic information and integrating data collection from community members.
   - **Benefits**:
     - With **ArcGIS Online**, you can collect data, create a shelter map, and set up **survey forms** for citizens to report conditions.
     - You can control who is allowed to submit data, and use **role-based access** to moderate submissions.
   - **Cost and Deployment**: ArcGIS is a commercial platform but often offers discounts to **nonprofits** and **municipal projects**. You could use ArcGIS Online, which provides a **cloud-based service**.
   - **Security**: ArcGIS provides **enterprise-level security**, including features to prevent abuse, such as authentication systems, configurable user roles, and data privacy controls.

### Custom-Built Platform Approach

If none of the existing solutions seem ideal due to concerns like **security** or **customization**, you could build a bespoke solution by combining various tools and components. Here’s a potential architecture:

1. **Core Components**:
   - **Backend and Database**:
     - Use a secure database such as **PostgreSQL** with **PostGIS** to store all geographic data.
     - You can deploy the application on a secure hosting service like **AWS** or **Azure**, with strong security measures.
   - **Frontend**:
     - Use mapping libraries like **Leaflet.js** or **Mapbox GL JS** to create a visual frontend where users can view the shelters and click on each one to see status or add reports.
   - **User Authentication**:
     - Implement **two-factor authentication (2FA)** for contributors to reduce risks of trolling or malicious inputs.
     - Consider requiring **verified phone numbers** to submit reports, with an **admin panel** to allow manual approval.

2. **Moderation and Reporting**:
   - Use **AI-based content moderation** tools to filter text submissions for abusive content. Tools like **Microsoft Azure Content Moderator** or **Perspective API** can be integrated into the workflow.
   - Allow users to flag inappropriate content or false reports, and set up a **volunteer moderation team** to review flagged submissions.
   - Use **rate limiting** for new submissions from the same IP address to prevent spamming.

3. **Alert and Engagement Features**:
   - Enable **email alerts** or notifications to authorities when a shelter is marked as non-operational or in poor condition.
   - Integrate a feature for community members to send **automated reports** to local authorities about critical shelter issues.

### Addressing Security Concerns

1. **Authentication and Verification**:
   - To prevent misuse or hacking, implement a **strong user verification system**. You could use **OAuth** with Google or Facebook or require **phone number validation**.
   - Limit who can access the tool by employing a **trusted network** of users. Only verified users should be able to contribute.

2. **Data Encryption and Security**:
   - Encrypt all data at rest and in transit using **SSL/TLS**.
   - Make sure to **obfuscate sensitive data**, especially any personal information of contributors.

3. **Community Moderation**:
   - Build a **community of local users** who are invested in providing accurate information. Empower this group to **moderate submissions** and ensure reliability.
   - Use **trusted volunteers** or community leaders to help validate the information.

4. **Anonymous Submissions (Optional)**:
   - Since some users may be hesitant to report due to safety concerns, consider allowing **anonymous submissions** but flag these for manual review.

### Example Workflow

1. **User Reports**: Residents open the app, locate a shelter on the map, and submit a report on its accessibility or condition. Photos can be attached to provide evidence.
2. **Moderation**: Reports are first reviewed by an automated filter (for inappropriate content), then by community moderators.
3. **Data Display**: Validated reports are added to the public map, showing accessible and inaccessible shelters.
4. **Authority Alerts**: Issues are forwarded to relevant authorities or municipal services for maintenance or action.

### Summary of Options

| Solution                 | Benefits                       | Security Measures                  | Difficulty Level | Deployment Type   |
|--------------------------|--------------------------------|------------------------------------|------------------|-------------------|
| **Ushahidi**             | Open-source, crisis-tested     | Moderation tools available         | Moderate         | Self-hosted       |
| **OpenStreetMap Custom** | Familiar platform, customizable| Requires custom moderation tools   | Moderate         | Self-hosted       |
| **ArcGIS Hub**           | High security, enterprise-level| Role-based access, configurable    | Moderate         | Cloud-based       |
| **Custom-Built Solution**| Complete customization         | High security and role-based       | High             | Self-hosted/cloud |

In conclusion, while setting up such a platform does present challenges given the **sensitive political climate**, existing technologies like **Ushahidi**, **ArcGIS**, or a **custom-built platform** can provide resilient solutions for crowdsourcing shelter information. Careful implementation of **authentication**, **moderation**, and **community engagement** measures will be essential to mitigate abuse and ensure the system is reliable and useful for residents in Jerusalem.
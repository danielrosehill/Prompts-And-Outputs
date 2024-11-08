---
title: "OSINT dashboard links with Israel focus"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Please create an OSINT themed dashboard with a focus on Israel. Your task is to aggregate OSINT resources which frequently comment on Israel. You can also try to find any flight monitoring resources that can be embedded with links that will only display traffic in and around Israel (Or Ben Gurion LLBG)

# Output

Creating an **OSINT (Open Source Intelligence) themed dashboard** with a focus on Israel is a fantastic way to stay informed about ongoing developments, especially from public data and independent sources. This type of dashboard will leverage various **OSINT accounts** on **Twitter (X)**, flight monitoring resources, and other tools that provide open-source insights, specifically for Israel. Below is a detailed breakdown of the OSINT resources that frequently comment on Israel, followed by how to integrate flight monitoring tools with a specific focus on **Ben Gurion Airport (LLBG)** or traffic in and around Israel.

### **OSINT Resources Dashboard for Israel**
#### **1. OSINT Accounts (Twitter/X Feeds)**
These accounts are known for monitoring and commenting on military, geopolitical, and intelligence developments with a focus on Israel or the wider region.

- **@ELINTNews**: [https://twitter.com/ELINTNews](https://twitter.com/ELINTNews)
  - Provides real-time intelligence from open sources, focusing on Israel and regional conflicts.

- **@AuroraIntel**: [https://twitter.com/AuroraIntel](https://twitter.com/AuroraIntel)
  - Shares satellite imagery, OSINT analysis, and situational reports (SITREPs) on incidents involving Israel.

- **@IntelCrab**: [https://twitter.com/IntelCrab](https://twitter.com/IntelCrab)
  - Focuses on real-time conflict monitoring using open-source tools, often with coverage of developments in Israel.

- **@JOSINTUpdates**: [https://twitter.com/JOSINTUpdates](https://twitter.com/JOSINTUpdates)
  - Provides updates related to military and intelligence activities around Israel and the broader Middle East.

- **@ImageSatIntl (ImageSat International)**: [https://twitter.com/ImageSatIntl](https://twitter.com/ImageSatIntl)
  - Satellite imagery of military installations, missile strikes, and other defense-related activities in Israel and surrounding areas.

- **@Intel_Sky (Intelsky)**: [https://twitter.com/Intel_Sky](https://twitter.com/Intel_Sky)
  - Monitors aerial activity, military movements, and geopolitical updates in the region, often posting about Israeli airspace and neighboring areas.

#### **2. Flight Monitoring Tools (with Focus on Israel)**
Flight monitoring tools are valuable for tracking civil and military aviation activity in Israel, specifically around **Ben Gurion Airport (LLBG)**.

- **Flightradar24 (Filtered for Israel Traffic)**:
  - **Flightradar24** provides real-time flight tracking that can be filtered to show specific **airports** or **regions**.
  - Link to **Ben Gurion Airport (LLBG)**: [https://www.flightradar24.com/32.01,34.89/10](https://www.flightradar24.com/32.01,34.89/10)
    - Use the link to focus on **Ben Gurion Airport** and surrounding airspace. You can embed this link in your dashboard for quick access.

- **ADS-B Exchange (Filtered for Israel Airspace)**:
  - **ADS-B Exchange** is another real-time flight tracking platform that does not block military flights.
  - Link to **Israel Airspace**: [https://globe.adsbexchange.com/?lat=32.01&lon=34.89&zoom=9](https://globe.adsbexchange.com/?lat=32.01&lon=34.89&zoom=9)
    - This link provides a view of **flights over Israel**, and **Ben Gurion Airport**, including military aircraft.

#### **3. Satellite Imagery and Analysis**
These OSINT resources use satellite data to provide real-time imagery and analysis of significant developments in Israel.

- **@ImageSatIntl (ImageSat International)**: [https://twitter.com/ImageSatIntl](https://twitter.com/ImageSatIntl)
  - Shares satellite imagery of military bases, strikes, and geopolitical developments in Israel and neighboring regions.

- **Sentinel Hub**:
  - **Sentinel Hub** provides satellite imagery from the **European Space Agency**.
  - Link to Israel imagery: [https://apps.sentinel-hub.com/eo-browser/](https://apps.sentinel-hub.com/eo-browser/)
  - You can customize the view to focus on **Israel** and monitor activities, such as changes in terrain or troop movements.

#### **4. Marine Traffic Monitoring**
These resources allow for real-time tracking of maritime traffic near Israel, which can be useful for understanding naval movements or monitoring potential maritime security incidents.

- **MarineTraffic** (Filter for Eastern Mediterranean):
  - Provides live tracking of maritime vessels, including **military**, **cargo**, and **civilian** ships.
  - Link to **Eastern Mediterranean and Israel Coast**: [https://www.marinetraffic.com/en/ais/home/centerx:34.89/centery:32.01/zoom:9](https://www.marinetraffic.com/en/ais/home/centerx:34.89/centery:32.01/zoom:9)
  - This link focuses on the **coast of Israel**, including the **Haifa Port** area.

#### **5. Independent Media and Situational Updates**
These independent sources provide **situational updates** regarding ongoing conflicts, protests, and other security developments involving Israel.

- **@OAlexanderDK**: [https://twitter.com/OAlexanderDK](https://twitter.com/OAlexanderDK)
  - OSINT analyst focusing on Israel and the wider Middle East, providing breakdowns of current events with a focus on military actions.

- **@MiddleEastEye**: [https://twitter.com/MiddleEastEye](https://twitter.com/MiddleEastEye)
  - Provides broader context and coverage of the Middle East, often including updates on Israel.

- **@CalibreObscura**: [https://twitter.com/CalibreObscura](https://twitter.com/CalibreObscura)
  - Independent analysis of military gear, weapons, and conflicts involving Israel, with a focus on hardware used by the IDF and various militant groups.

#### **6. News and Alert Accounts**
These news and alert accounts provide **breaking news** that is often relevant to military and security developments.

- **@Conflicts (Conflicts News Worldwide)**: [https://twitter.com/Conflicts](https://twitter.com/Conflicts)
  - Provides breaking news on global conflicts, including updates related to Israel.
  
- **@Roi_Kais (Middle Eastern Affairs Analyst)**: [https://twitter.com/Roi_Kais](https://twitter.com/Roi_Kais)
  - A journalist focusing on **Middle Eastern Affairs**, providing commentary and updates on events in Israel.

#### **Suggested Layout for the OSINT Dashboard**
To effectively organize these OSINT resources into a functional and user-friendly **dashboard**, consider the following layout:

##### **1. Real-Time Flight Monitoring (Top Section)**
- **Flightradar24** and **ADS-B Exchange**:
  - Embed these links into **iframes** that can display **real-time air traffic** focused on **Ben Gurion Airport** and **Israeli airspace**.
  - This section should be at the **top of the dashboard** to provide continuous visibility on any air traffic, including **military activities**.

##### **2. OSINT Twitter Feeds (Central Section)**
- **@ELINTNews**, **@AuroraIntel**, **@IntelCrab**, **@ImageSatIntl**, **@Intel_Sky**:
  - Use **Twitter widgets** or **RSS feed widgets** to display the latest tweets from these key OSINT accounts.
  - Arrange them in a **three-column grid** to allow simultaneous viewing of multiple feeds for different perspectives on **Israel**.

##### **3. Satellite and Maritime Monitoring (Right Sidebar)**
- **Sentinel Hub** for satellite imagery and **MarineTraffic** for maritime updates.
  - Embed interactive links that users can click on to see the latest **satellite data** or **maritime vessel tracking**.
  - **Place these links in the right sidebar** to complement other visual resources like flight monitoring.

##### **4. Official Government and State Accounts (Bottom Section)**
- **@IDF**, **@PikudHaoref**, **@IsraelMFA**, **@kann_news**:
  - Include these **official Twitter accounts** in a section near the **bottom**, allowing for comparison between **official sources** and **OSINT insights**.
  - Create a **scrollable feed** or timeline format so you can quickly review statements directly from **official sources**.

##### **5. Independent Media and Situational Updates (Left Sidebar)**
- **@MiddleEastEye**, **@OAlexanderDK**, **@CalibreObscura**, **@Roi_Kais**:
  - Place independent analysts in the **left sidebar** to provide **alternative views** and **independent insights** on ongoing events.
  - This helps in understanding different **narratives** around any conflict or military operation.

### ** 
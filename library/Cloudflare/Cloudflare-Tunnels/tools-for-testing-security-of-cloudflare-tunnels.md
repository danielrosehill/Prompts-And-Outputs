---
title: "Tools for testing security of Cloudflare Tunnels"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When it comes to **Cloudflare Tunnels**, which are usually configured as **CNAME DNS records**, you want to perform specific enumeration to identify if those **CNAME records** can be easily discovered. Here are some tools and approaches specifically geared towards discovering **Cloudflare Tunnel CNAMEs**:

### **1. Amass**
**Amass** is particularly effective at discovering subdomains, including **CNAMEs**. By scraping multiple sources, it can help identify **CNAME records** created for Cloudflare Tunnels.

**Usage**:
```bash
amass enum -d testhomewebsite.com
```
This will perform a deep scan for subdomains, including **CNAME** records.

### **2. DNSRecon**
**DNSRecon** can also help you find **CNAME records** by performing comprehensive enumeration.

**Usage**:
```bash
dnsrecon -d testhomewebsite.com
```
Look specifically for entries labeled **CNAME** in the output to identify Cloudflare Tunnel entries.

### **3. Dig Command with Specific CNAME Lookups**
You can also use **`dig`** to specifically query **CNAME** records for any known subdomains.

**Usage**:
```bash
# To check the CNAME record for a specific subdomain
dig CNAME nas.testhomewebsite.com
```
If there are multiple subdomains to check, you can automate this using a small script to cycle through known or discovered subdomains.

### **4. Subfinder**
**Subfinder** is another open-source tool that focuses on finding subdomains by querying passive sources, and it may be effective for detecting **CNAMEs** linked to Cloudflare Tunnels.

**Installation**:
You can use **Go** to install Subfinder on Fedora.
```bash
sudo dnf install golang -y
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
Ensure **`$GOPATH/bin`** is in your **`$PATH`** to run the tool.

**Usage**:
```bash
subfinder -d testhomewebsite.com
```
This will provide a list of subdomains, including potential **CNAMEs**.

### **5. MassDNS (with a Wordlist for Brute-Force)** 
**MassDNS** can be useful if you want to brute-force potential subdomains, and then **dig** can be used to verify if they are **CNAME** records pointing to Cloudflare.

**Installation**:
```bash
git clone https://github.com/blechschmidt/massdns.git
cd massdns
make
```

**Usage**:
1. **Run MassDNS** to discover potential subdomains:
   ```bash
   ./bin/massdns -r resolvers.txt -t A -o S testhomewebsite.com -w subdomains.txt
   ```
2. **Check CNAME Records** for discovered subdomains:
   Use **`dig`** to loop through the subdomains discovered by MassDNS:
   ```bash
   while read sub; do dig CNAME $sub; done < subdomains.txt
   ```

### **6. Cloudflare's API for Zone Records**
If you have access to **Cloudflare's API** for your domain, you can also use their API to list all **DNS records**, including **CNAMEs** created for tunnels. This is particularly useful if you have permission to perform a full audit.

**API Command Example**:
First, you need to get your **zone ID** and **API token** from your Cloudflare dashboard.

```bash
# Replace <zone_id> and <api_token> with your actual values
curl -X GET "https://api.cloudflare.com/client/v4/zones/<zone_id>/dns_records?type=CNAME" \
     -H "Authorization: Bearer <api_token>" \
     -H "Content-Type: application/json"
```
This will return a list of all **CNAME records**, including those pointing to your **Cloudflare Tunnel** endpoints.

### **7. Check for Certificate Transparency Logs**
**Certificate Transparency Logs** can be used to identify subdomains if SSL certificates were issued for your subdomains, including those using Cloudflare Tunnels.

- **crt.sh** provides a search for certificates issued for your domain.
  ```bash
  curl "https://crt.sh/?q=%25.testhomewebsite.com&output=json" | jq '.[] | .name_value'
  ```

### **Summary**
- **Amass** and **Subfinder** are effective for general **subdomain enumeration**, which can reveal **CNAME records** linked to **Cloudflare Tunnels**.
- Use **`dig CNAME`** to check for specific records directly.
- **DNSRecon** and **MassDNS** can be used for more exhaustive enumeration and validation.
- **Cloudflare API** is the most direct method if you have control of the domain.
- **Certificate Transparency Logs** can help discover subdomains with SSL certificates.

These tools will help you identify any **Cloudflare Tunnel endpoints** that are publicly discoverable and provide insights into whether extra security measures or remediation are needed. Let me know if you need specific guidance on using any of these tools!
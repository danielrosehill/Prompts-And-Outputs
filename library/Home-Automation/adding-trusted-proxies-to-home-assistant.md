---
title: "Adding trusted proxies to Home Assistant"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you should add Cloudflare’s IP ranges as trusted proxies in your Home Assistant configuration to ensure that it properly handles requests coming through the tunnel. Since Cloudflare will act as a reverse proxy, Home Assistant needs to trust it in order to handle features like `X-Forwarded-For` headers correctly, especially for logging the real IP addresses of clients.

### Add Trusted Proxies in `configuration.yaml`:
You will need to configure the `trusted_proxies` field under the `http:` section to include Cloudflare's IP ranges.

1. Update your `configuration.yaml` file:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 192.168.1.20  # Your network gateway
    - 172.30.33.0/24  # Local docker network
    # Cloudflare IP ranges
    - 173.245.48.0/20
    - 103.21.244.0/22
    - 103.22.200.0/22
    - 103.31.4.0/22
    - 141.101.64.0/18
    - 108.162.192.0/18
    - 190.93.240.0/20
    - 188.114.96.0/20
    - 197.234.240.0/22
    - 198.41.128.0/17
    - 162.158.0.0/15
    - 104.16.0.0/13
    - 104.24.0.0/14
    - 172.64.0.0/13
    - 131.0.72.0/22
```

2. **Explanation**:
   - `use_x_forwarded_for: true` ensures that Home Assistant respects the `X-Forwarded-For` header, which contains the client’s real IP.
   - `trusted_proxies` should include:
     - The IP of your gateway (`192.168.1.20` in this case).
     - Cloudflare’s IP ranges, as listed above. These IP ranges are from Cloudflare’s infrastructure and may be updated, so it’s good to occasionally verify them on [Cloudflare's website](https://www.cloudflare.com/ips/).

3. **Restart Home Assistant**: After updating your `configuration.yaml`, restart Home Assistant to apply the changes.

This setup will ensure that traffic routed through Cloudflare is properly trusted and handled by your Home Assistant instance.
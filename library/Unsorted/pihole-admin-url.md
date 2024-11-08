---
title: "PiHole admin URL"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The default admin URL for Pi-hole, assuming it is running on `192.168.1.30`, would be:

```
http://192.168.1.30/admin
```

You can access this URL from any device on your network to manage your Pi-hole settings. If you have configured Pi-hole to use HTTPS or a custom port, you may need to adjust the URL accordingly:

- If using HTTPS:
  ```
  https://192.168.1.30/admin
  ```

- If using a custom port (e.g., `8080`):
  ```
  http://192.168.1.30:8080/admin
  ```

If you haven't changed any of the default settings, the standard `http://192.168.1.30/admin` should work.
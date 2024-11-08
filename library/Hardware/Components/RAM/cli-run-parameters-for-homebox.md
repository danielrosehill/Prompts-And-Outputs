---
title: "CLI run parameters for Homebox"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


### Summary of CLI Arguments for **api** Command

Below is a summary of the command-line arguments and environment variables for running the `api`:

| Option                                                                        | Type       | Default Value              | Description                                               |
| ----------------------------------------------------------------------------- | ---------- | -------------------------- | --------------------------------------------------------- |
| `--mode` / `$HBOX_MODE`                                                       | `<string>` | `development`              | Set the application mode (development, production, etc.). |
| `--web-port` / `$HBOX_WEB_PORT`                                               | `<string>` | `7745`                     | The port for the web interface.                           |
| `--web-host` / `$HBOX_WEB_HOST`                                               | `<string>` | (empty)                    | The host address for the web interface.                   |
| `--web-max-upload-size` / `$HBOX_WEB_MAX_UPLOAD_SIZE`                         | `<int>`    | `10`                       | Max upload size in MB.                                    |
| `--storage-data` / `$HBOX_STORAGE_DATA`                                       | `<string>` | `./.data`                  | Directory to store data.                                  |
| `--storage-sqlite-url` / `$HBOX_STORAGE_SQLITE_URL`                           | `<string>` | `./.data/homebox.db?_fk=1` | SQLite database URL.                                      |
| `--log-level` / `$HBOX_LOG_LEVEL`                                             | `<string>` | `info`                     | Logging level (info, debug, error, etc.).                 |
| `--log-format` / `$HBOX_LOG_FORMAT`                                           | `<string>` | `text`                     | Log format (text or json).                                |
| `--mailer-host` / `$HBOX_MAILER_HOST`                                         | `<string>` | (empty)                    | SMTP mail server host.                                    |
| `--mailer-port` / `$HBOX_MAILER_PORT`                                         | `<int>`    | (empty)                    | SMTP mail server port.                                    |
| `--mailer-username` / `$HBOX_MAILER_USERNAME`                                 | `<string>` | (empty)                    | SMTP username.                                            |
| `--mailer-password` / `$HBOX_MAILER_PASSWORD`                                 | `<string>` | (empty)                    | SMTP password.                                            |
| `--mailer-from` / `$HBOX_MAILER_FROM`                                         | `<string>` | (empty)                    | The "from" address for outgoing emails.                   |
| `--swagger-host` / `$HBOX_SWAGGER_HOST`                                       | `<string>` | `localhost:7745`           | Host for Swagger documentation.                           |
| `--swagger-scheme` / `$HBOX_SWAGGER_SCHEME`                                   | `<string>` | `http`                     | Scheme for Swagger (http or https).                       |
| `--demo` / `$HBOX_DEMO`                                                       | `<bool>`   | (empty)                    | Enable demo mode.                                         |
| `--debug-enabled` / `$HBOX_DEBUG_ENABLED`                                     | `<bool>`   | `false`                    | Enable debugging.                                         |
| `--debug-port` / `$HBOX_DEBUG_PORT`                                           | `<string>` | `4000`                     | Port for debugging.                                       |
| `--options-allow-registration` / `$HBOX_OPTIONS_ALLOW_REGISTRATION`           | `<bool>`   | `true`                     | Allow user registration.                                  |
| `--options-auto-increment-asset-id` / `$HBOX_OPTIONS_AUTO_INCREMENT_ASSET_ID` | `<bool>`   | `true`                     | Auto-increment asset IDs.                                 |
| `--options-currency-config` / `$HBOX_OPTIONS_CURRENCY_CONFIG`                 | `<string>` | (empty)                    | Configure currency settings.                              |
| `--help` / `-h`                                                               | (none)     | (none)                     | Show the help message.                                    |

### Example Command

To set the **data directory** to `/homeboxdata` and the **port** to `3100`, you can use the following command:

```bash
api --storage-data /homeboxdata --web-port 3100
```

This command will:
- Set the **data directory** to `/homeboxdata` with the `--storage-data` option.
- Set the **port** to `3100` with the `--web-port` option.

If you have additional configuration options, you can combine them in the same command as needed.

Let me know if you need further clarification!
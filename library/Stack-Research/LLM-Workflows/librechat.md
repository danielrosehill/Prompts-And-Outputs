---
tite: "LibreChat for self-hosted chatbot UI with conversation routing to managed storage"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



To get started with **LibreChat** for your project, follow this step-by-step guide to set up the system, integrate GPT-4, enable authentication, and configure conversation storage. This guide assumes you are deploying on a cloud server like a VPS or GCP.

### 1. Set up LibreChat

LibreChat provides a Docker-based setup, which makes deployment straightforward. Here's how you can get started:

#### Step 1: Clone the LibreChat Repository

You can either download the ZIP file or clone the repository using Git.

```bash
git clone https://github.com/danny-avila/LibreChat.git
cd LibreChat
```

#### Step 2: Install Docker

If Docker is not installed on your server, install it first. You can follow [Docker's installation guide](https://docs.docker.com/get-docker/) for your specific operating system.

#### Step 3: Configure Environment Variables

Create and configure the `.env` file by copying the provided example:

```bash
cp .env.example .env
```

Edit the `.env` file to include necessary configurations such as API keys for GPT-4 (OpenAI), database credentials, and any other environment-specific settings.

For GPT-4 integration, you will need to set your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key
```

#### Step 4: Configure librechat.yaml

LibreChat uses a `librechat.yaml` file for additional configuration. You can copy the example config file and modify it according to your needs (e.g., setting up GPT-4 endpoints).

```bash
cp librechat.yaml.example librechat.yaml
```

Make sure to bind this file in your Docker setup by editing `docker-compose.override.yml`:

```yaml
version: '3.4'

services:
  api:
    volumes:
      - type: bind
        source: ./librechat.yaml
        target: /app/librechat.yaml
```

This ensures that your configuration is applied when you start the service.

#### Step 5: Start LibreChat with Docker

Now that everything is configured, start the application using Docker Compose:

```bash
docker compose up -d
```

This will pull the necessary images and start LibreChat on your server.

### 2. Set Up Authentication

LibreChat supports both email-based and social logins (OAuth2). Here’s how to set up authentication for private access:

#### Email Login (Basic Authentication)

To enable email login and registration, modify your `.env` file with the following settings:

```bash
ALLOW_EMAIL_LOGIN=true
ALLOW_REGISTRATION=false  # Disable public registration if it's only for personal use.
```

You can manually create users using the provided script:

```bash
docker-compose exec api npm run create-user
```

Follow the prompts to enter an email and password for your user account.

#### OAuth2 (Optional)

If you prefer using OAuth2 for authentication (e.g., Google, GitHub), you can configure it in `librechat.yaml`. For example, to enable Google OAuth:

1. Set up OAuth credentials in your Google Developer Console.
2. Add the following to `librechat.yaml`:

```yaml
oauth:
  google:
    client_id: "your_google_client_id"
    client_secret: "your_google_client_secret"
    redirect_uri: "https://your-domain.com/auth/callback/google"
```

You can find more details on configuring OAuth2 in [LibreChat's OAuth2 documentation](https://www.librechat.ai/docs/configuration/authentication/OAuth2-OIDC)\[6].

### 3. Store Conversations in a Database

LibreChat allows you to store conversations in a database for later retrieval and search functionality. You’ll need to configure a database like PostgreSQL or MongoDB.

#### Step 1: Install PostgreSQL or MongoDB

For PostgreSQL:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

For MongoDB:

```bash
sudo apt update
sudo apt install -y mongodb-org
```

#### Step 2: Configure Database Connection

In your `.env` file, add database connection details:

For PostgreSQL:

```bash
DB_CONNECTION=postgresql://username:[email protected]:5432/librechat_db
```

For MongoDB:

```bash
DB_CONNECTION=mongodb://localhost:27017/librechat_db
```

Ensure that LibreChat is configured to store conversations in this database by modifying the `librechat.yaml` file if needed.

### 4. Search and Retrieve Conversations

To implement search functionality, you can either use PostgreSQL’s full-text search capabilities or integrate an external search engine like Elasticsearch.

#### Option 1: Full-Text Search with PostgreSQL

PostgreSQL has built-in support for full-text search that allows you to query stored conversations efficiently.

Example SQL query for searching through conversations:

```sql
SELECT * FROM conversations WHERE conversation_text @@ plainto_tsquery('search_term');
```

#### Option 2: Elasticsearch Integration

If you expect large-scale data storage or more advanced search features, consider integrating Elasticsearch as a dedicated search engine.

1. Install Elasticsearch on your server.
2. Configure LibreChat to index conversations into Elasticsearch by modifying `librechat.yaml`.

### 5. Markdown Rendering

LibreChat supports rendering Markdown natively in messages. To ensure that saved conversations are displayed correctly with Markdown formatting:

1. Use libraries like `react-markdown` in the frontend if you're customizing it.
2. Markdown will be rendered automatically if saved correctly in the conversation storage.

### 6. Deploying on a Cloud Server (VPS/GCP)

Once everything is working locally, deploy it on a cloud server like GCP or any VPS provider (e.g., DigitalOcean).

#### Steps:

1. Set up a VPS instance with Ubuntu or any preferred Linux distribution.
2. Install Docker and Docker Compose on the VPS.
3. Clone your LibreChat project onto the server.
4. Use `docker compose up -d` to run LibreChat in detached mode.
5. Ensure that ports are open (e.g., port 80/443 for HTTP/HTTPS) and set up SSL certificates using Let's Encrypt if needed.

### Conclusion

By following these steps, you can quickly set up **LibreChat** as a self-hosted chatbot interface with GPT-4 integration, secure authentication, conversation storage, and search functionality—all while supporting Markdown rendering natively.

&#x20;

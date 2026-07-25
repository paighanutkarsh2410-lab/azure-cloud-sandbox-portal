# Cloud Sandbox Portal

A Flask-based self-service cloud sandbox provisioning portal deployed on Microsoft Azure App Service.

## Features

- Request a cloud sandbox
- Dashboard to track provisioning status
- Automatic status updates
- SQLite database integration
- Responsive UI
- Azure App Service deployment
- GitHub version control

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- HTML
- CSS
- JavaScript
- SQLite
- Microsoft Azure App Service
- Azure Blob Storage
- GitHub

## Project Structure

```
app.py
requirements.txt
Procfile
templates/
static/
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

This application is deployed to Azure App Service (Linux) using ZIP deployment.

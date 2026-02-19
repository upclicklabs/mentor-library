---
title: "Dive into Anthropic's Computer Use quickstart"
source_url: "https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo"
source_type: blog
mentor: "Borris"
date_synced: "2026-02-20T00:00:00Z"
---

# Dive into Anthropic's Computer Use quickstart

This repository provides a reference implementation to get started with computer use on Claude, featuring:

- Build files to create a Docker container with all necessary dependencies
- A computer use agent loop using the Claude API, Bedrock, or Vertex to access Claude models
- Anthropic-defined computer use tools
- A streamlit app for interacting with the agent loop

## Important Notices

### Beta Feature

Computer use is a beta feature with unique risks distinct from standard API features. To minimize risks:

- Use a dedicated virtual machine or container with minimal privileges
- Avoid giving the model access to sensitive data (login information, etc.)
- Limit internet access to an allowlist of domains
- Ask humans to confirm decisions with meaningful real-world consequences
- Be aware that Claude may follow instructions found in webpage content or images, potentially conflicting with user instructions

### API Subject to Change

The Beta API used in this reference implementation is subject to change.

## Quickstart: Running the Docker Container

### Claude API

```bash
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

### Bedrock

#### Option 1: Use AWS Credentials File and Profile (Suggested)

```bash
export AWS_PROFILE=<your_aws_profile>
docker run \
  -e API_PROVIDER=bedrock \
  -e AWS_PROFILE=$AWS_PROFILE \
  -e AWS_REGION=us-west-2 \
  -v $HOME/.aws:/home/computeruse/.aws \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

#### Option 2: Use Access Key and Secret

```bash
export AWS_ACCESS_KEY_ID=%your_aws_access_key%
export AWS_SECRET_ACCESS_KEY=%your_aws_secret_access_key%
export AWS_SESSION_TOKEN=%your_aws_session_token%
docker run \
  -e API_PROVIDER=bedrock \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN \
  -e AWS_REGION=us-west-2 \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

### Vertex

```bash
docker build . -t computer-use-demo
gcloud auth application-default login
export VERTEX_REGION=%your_vertex_region%
export VERTEX_PROJECT_ID=%your_vertex_project_id%
docker run \
  -e API_PROVIDER=vertex \
  -e CLOUD_ML_REGION=$VERTEX_REGION \
  -e ANTHROPIC_VERTEX_PROJECT_ID=$VERTEX_PROJECT_ID \
  -v $HOME/.config/gcloud/application_default_credentials.json:/home/computeruse/.config/gcloud/application_default_credentials.json \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it computer-use-demo
```

## Accessing the Demo App

Once the container is running, open your browser to http://localhost:8080 to access the combined interface that includes both the agent chat and desktop view.

The container stores settings like the API key and custom system prompt in `~/.anthropic/`. Mount this directory to persist settings between container runs.

### Alternative Access Points

- Streamlit interface only: http://localhost:8501
- Desktop view only: http://localhost:6080/vnc.html
- Direct VNC connection: vnc://localhost:5900 (for VNC clients)

## Screen Size

Environment variables `WIDTH` and `HEIGHT` can be used to set the screen size:

```bash
docker run \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -e WIDTH=1920 \
  -e HEIGHT=1080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

### Recommended Resolution

Do not send screenshots above XGA/WXGA resolution to avoid issues with image resizing.

- For higher resolutions: Scale the image down to XGA and map coordinates back to the original resolution proportionally
- For lower resolutions or smaller devices: Add black padding around the display area until it reaches 1024x768

## Development

```bash
./setup.sh # configure venv, install development dependencies, and install pre-commit hooks
docker build . -t computer-use-demo:local # manually build the docker image (optional)
export ANTHROPIC_API_KEY=%your_api_key%
docker run \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $(pwd)/computer_use_demo:/home/computeruse/computer_use_demo/ \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it computer-use-demo:local
```

The docker run command above mounts the repo inside the docker image for editing files from the host. Streamlit is already configured with auto-reloading.

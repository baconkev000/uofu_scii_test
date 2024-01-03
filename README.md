# U of U Coding Challenge

License: MIT

## Getting Started

These instructions will get you through launching phase of this project.

### Prerequisites

- Make sure that you have Docker and Docker Compose installed
  - Windows or macOS:
    [Install Docker Desktop](https://www.docker.com/get-started)
  - Linux: [Install Docker](https://www.docker.com/get-started) and then
    [Docker Compose](https://github.com/docker/compose)

### Launching Project

- Clone this repository

- CD into the frotnend directory and install vue-cli-service using the command:
      ```
      cd frontend && npm install @vue/cli-service --save-dev && cd ../
      ```

- To launch, run the command:

      $ docker compose up -d --build

- Follow Project Setup Instructions from [Backend Readme](https://github.com/baconkev000/uofu_scii_test/blob/main/backend/README.md)


### Project Urls

- Frontend port at [localhost:8080](http://localhost:8080)
- Backend port at [localhost:8000](http://localhost:8080)
# Egyptian National ID Validator and Data Extractor 
## Description
This Django Rest Framework (DRF) task is a simple API project that provides endpoints for validating and extracting information from Egyptian national identification numbers. It can validate the structure of Egyptian national IDs and extract the gender, birthdate, and birth governorate information from valid IDs.

## Features
### National ID Validation: 
> Validate Egyptian national identification numbers for correct format.

### Data Extraction: 
> Extract gender, birthdate, and birth governorate from valid national IDs.


## Prerequisites
Before getting started, ensure you have the following prerequisites installed on your system:

- Docker
- Docker Compose
- Git

## Setup
- Clone the repository to your local machine:
```bash
git clone https://github.com/MohamedAbdElMeged/task.git

cd task
```
- build and start the Docker containers:
```bash
docker compose build
docker compose up
```
> This command will download the necessary Docker images, build the application, and start the containers.
- Access the API at http://0.0.0.0:8000


## Usage
### API Endpoints
- Validate Egyptian National ID:
`POST /validate`


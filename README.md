# Egyptian National ID Validator and Data Extractor 
## Description
This Django Rest Framework (DRF) task is a simple API project that provides endpoints for validating and extracting information from Egyptian national identification numbers. It can validate the structure of Egyptian national IDs and extract the gender, birthdate, and birth governorate information from valid IDs.

## Features
### National ID Validation: 
> Validate Egyptian national identification numbers for correct format.

### Data Extraction: 
> Extract gender, birthdate, and birth governorate from valid national IDs.

## Technologies 
- python 3.12.0
- Django==3.2.5
- djangorestframework==3.12.4


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
`POST /api/v1/validate`
To validate an Egyptian national identification number, send a POST request with the national ID in the request body as follows:
```json
{
  "id": "25601011234567"
}
```
The API will respond with a validation result, and if the ID is valid, it will include the extracted data.
```json
{
    "gender": "Female",
    "birth_date": "1956-01-01",
    "governorate": "Daqahliya"
}
```

### Some Useful Commands
- start the project
```bash
docker compose up
```
- stop the project
```bash
docker compose down
```
- check running containers
```bash
docker compose ps
NAME                COMMAND                  SERVICE             STATUS              PORTS
djangoapp           "python manage.py ru…"   djangoapp           running             0.0.0.0:8000->8000/tcp

```
- access backend container
```bash
docker exec -it djangoapp /bin/bash
```
- list urls 
> after accessing the backend container
```bash
python manage.py show_urls
```
or you can run the command directly using
```bash
docker compose exec djangoapp python manage.py show_urls
```

## Test Coverage
### Api Testing
- To run test cases (after accessing the backend container)
```bash
python manage.py test
```

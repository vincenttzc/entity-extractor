# Entity Extractor

Entity Extractor is a web API service that scrapes the text body from an URL, then extracts entities and the accompanying sentences.

Click on the Google Cloud button below to deploy this container on a GCP account via Google Cloud Run.

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

## Usage

### Run on Google Cloud Run

1. Click on Cloud Run button above
2. Google Cloud will show a popup, asking you if you trust the repo. Tick Trust and select Confirm

<img src="img/gcp_1.jpg"  width="500" />

3. Google Cloud will then show another popup asking if you Authorize GCP API call with ypur credentials. Click Authorize

<img src="img/gcp_2.jpg" width="600"/>

4. Select project to deploy application
5. Select region to deploy application
6. Google Cloud Run will build the container image and push to your Project registry. The image will then be deployed.
7. Note down the web server URL provided by Google Cloud Run

### Run locally

1. Clone repo

```
git clone https://github.com/vincenttzc/entity-extractor.git
```

2. Build docker image

```
docker build -t entity-extractor .
```

3. Run docker container

```
docker run --env-file config/.env.dev -p 8080:8080 entity-extractor
```

## API Endpoints

When run on Cloud Run, web server URL is provided by Google Cloud Run.

When run locally, web server URL is `http://127.0.0.1:8080/`.

| Endpoint            | Request Type | Description                                                                                                               | Example request body                                   | Example response body                                                         |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| /extract_entities   | POST         | Extract the entities and sentences from URL provided then insert in database. Returns unique entities extracted from URL. | {"input_link": "https://en.wikipedia.org/wiki/Betta" } | {"entities": ["Betta", "United Nations"]}                                     |
| /query_all_entities | GET          | Query all unique entities in database                                                                                     | NA                                                     | {"entities": ["Betta", "United Nations"]}                                     |
| /query_sentences    | POST         | Query all sentences containing specified entity from database                                                             | {"entity": "Betta"}                                    | {"sentences": ["sentence 1 containing Betta", "sentence 2 containing Betta"]} |

Refer to [openapi.json](openapi.json) for more detailed information of the API

## Config

Environment variables can be added to the `.env` files in the config folder. This allows different environment variables to be used when running the Docker container for different environments.

Application config can be configured in [config/config.yaml](config/config.yaml)

## Extension

To change the database, datasource type (eg. url or object store) and text format (eg. HTML or CSV):

1. Create a new class in the respective database/ datasource/ datapipeline folder which inherits from the base class - `DatabaseType`, `SourceType` or `TextFormat`
1. Import new class in `__init__.py`
1. Add new class in `main.py`, add condition to make it configurable through `config.yaml`. Add new class as input to `Database`, `DataSource` or `DataPipeline`
1. Modify `config.yaml` to use new class

## Testing

To test the files:

1. Clone repo

```
git clone https://github.com/vincenttzc/entity-extractor.git
```

2. At root directory, execute:

```
pytest
```

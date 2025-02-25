# OpenCTI {% if cookiecutter.connector_type == "external-import" %}External Ingestion{% elif cookiecutter.connector_type == "internal-enrichment" %}Internal Enrichment{% elif cookiecutter.connector_type == "internal-export-file" %}Internal Export{% elif cookiecutter.connector_type == "internal-import-file" %}Internal Import{% elif cookiecutter.connector_type == "stream" %}STREAM{% endif %} Connector {{cookiecutter.connector_name}}

<!--
General description of the connector
* What it does
* How it works
* Special requirements
* Use case description
* ...
-->

Table of Contents

- [OpenCTI {% if cookiecutter.connector_type == "external-import" %}External Ingestion{% elif cookiecutter.connector_type == "internal-enrichment" %}Internal Enrichment{% elif cookiecutter.connector_type == "internal-export-file" %}Internal Export{% elif cookiecutter.connector_type == "internal-import-file" %}Internal Import{% elif cookiecutter.connector_type == "stream" %}STREAM{% endif %} Connector {{cookiecutter.connector_name}}](#opencti-{% if cookiecutter.connector_type == "external-import" %}external-ingestion{% elif cookiecutter.connector_type == "internal-enrichment" %}internal-enrichment{% elif cookiecutter.connector_type == "internal-export-file" %}internal-export{% elif cookiecutter.connector_type == "internal-import-file" %}internal-import{% elif cookiecutter.connector_type == "stream" %}stream{% endif %}-connector-{{cookiecutter.__connector_name_kebabcase}})
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Configuration variables](#configuration-variables)
    - [OpenCTI environment variables](#opencti-environment-variables)
    - [Base connector environment variables](#base-connector-environment-variables)
    - [Connector extra parameters environment variables](#connector-extra-parameters-environment-variables)
  - [Deployment](#deployment)
    - [Docker Deployment](#docker-deployment)
    - [Manual Deployment](#manual-deployment)
  - [Usage](#usage)
  - [Behavior](#behavior)
  - [Debugging](#debugging)
  - [Additional information](#additional-information)

## Introduction

## Installation

### Requirements

- OpenCTI Platform >= 6...

## Configuration variables

There are a number of configuration options, which are set either in `docker-compose.yml` (for Docker) or
in `config.yml` (for manual deployment).

### OpenCTI environment variables

Below are the parameters you'll need to set for OpenCTI:

| Parameter     | config.yml | Docker environment variable | Mandatory | Description                                          |
|---------------|------------|-----------------------------|-----------|------------------------------------------------------|
| OpenCTI URL   | url        | `OPENCTI_URL`               | Yes       | The URL of the OpenCTI platform.                     |
| OpenCTI Token | token      | `OPENCTI_TOKEN`             | Yes       | The default admin token set in the OpenCTI platform. |

### Base connector environment variables

Below are the parameters you'll need to set for running the connector properly:

| Parameter                             | config.yml                  | Docker environment variable             | Default                                                                                                                                                                                                                                                                                                                                                                                               | Mandatory   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -----------------                     | ------------                | -----------------------------           | -----------------                                                                                                                                                                                                                                                                                                                                                                                     | ----------- | ------------------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                  |
| Connector ID                          | id                          | `CONNECTOR_ID`                          | /                                                                                                                                                                                                                                                                                                                                                                                                     | Yes         | A unique `UUIDv4` identifier for this connector instance.                                                                                                                                                                                                                                                                                                                                                                                                   |
| Connector Type                        | type                        | `CONNECTOR_TYPE`                        | {% if cookiecutter.connector_type == "external-import" %}EXTERNAL_IMPORT{% elif cookiecutter.connector_type == "internal-enrichment" %}INTERNAL_ENRICHMENT{% elif cookiecutter.connector_type == "internal-export-file" %}INTERNAL_EXPORT_FILE{% elif cookiecutter.connector_type == "internal-import-file" %}INTERNAL_IMPORT_FILE{% elif cookiecutter.connector_type == "stream" %}STREAM{% endif %} | Yes         | Should always be set to {% if cookiecutter.connector_type == "external-import" %}`EXTERNAL_IMPORT`{% elif cookiecutter.connector_type == "internal-enrichment" %}`INTERNAL_ENRICHMENT`{% elif cookiecutter.connector_type == "internal-export-file" %}`INTERNAL_EXPORT_FILE`{% elif cookiecutter.connector_type == "internal-import-file" %}`INTERNAL_IMPORT_FILE`{% elif cookiecutter.connector_type == "stream" %}`STREAM`{% endif %} for this connector. |
| Connector Name                        | name                        | `CONNECTOR_NAME`                        | /                                                                                                                                                                                                                                                                                                                                                                                                     | Yes         | Name of the connector.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Connector Scope                       | scope                       | `CONNECTOR_SCOPE`                       | /                                                                                                                                                                                                                                                                                                                                                                                                     | Yes         | The scope or type of data the connector is importing, either a MIME type or Stix Object.                                                                                                                                                                                                                                                                                                                                                                    |
| Log Level                             | log_level                   | `CONNECTOR_LOG_LEVEL`                   | info                                                                                                                                                                                                                                                                                                                                                                                                  | Yes         | Determines the verbosity of the logs. Options are `debug`, `info`, `warn`, or `error`.                                                                                                                                                                                                                                                                                                                                                                      |
{%- if cookiecutter.connector_type == "external-import" %}
| Duration Period                       | duration_period             | `CONNECTOR_DURATION_PERIOD`             | /                                                                                                                                                                                                                                                                                                                                                                                                     | Yes         | The interval at which the connector runs, in ISO8601 format. Example: PT30M for 30 minutes.                                                                                                                                                                                                                                                                                                                                                                 |
{%- elif cookiecutter.connector_type == "internal-enrichment" %}
| Connector Auto                        | auto                        | `CONNECTOR_AUTO`                        | True                                                                                                                                                                                                                                                                                                                                                                                                  | Yes         | Must be `True` or `False` to enable or disable auto-enrichment of observables                                                                                                                                                                                                                                                                                                                                                                               |
{%- elif cookiecutter.connector_type == "stream" %}
| Connector Live Stream ID              | live_stream_id              | `CONNECTOR_LIVE_STREAM_ID`              | /                                                                                                                                                                                                                                                                                                                                                                                                     | Yes         | ID of the live stream created in the OpenCTI UI                                                                                                                                                                                                                                                                                                                                                                                                             |
| Connector Live Stream Listen Delete   | live_stream_listen_delete   | `CONNECTOR_LIVE_STREAM_LISTEN_DELETE`   | True                                                                                                                                                                                                                                                                                                                                                                                                  | Yes         | Listen to all delete events concerning the entity, depending on the filter set for the OpenCTI stream.                                                                                                                                                                                                                                                                                                                                                      |
| Connector Live Stream No dependencies | live_stream_no_dependencies | `CONNECTOR_LIVE_STREAM_NO_DEPENDENCIES` | True                                                                                                                                                                                                                                                                                                                                                                                                  | Yes         | Always set to True unless you are synchronizing 2 OpenCTI platforms and you want to get an entity and all context (relationships and related entity)                                                                                                                                                                                                                                                                                                        |
{%- endif %}

### Connector extra parameters environment variables

Below are the parameters you'll need to set for the connector:

| Parameter      | config.yml     | Docker environment variable   | Default   | Mandatory   | Description                                                                                                        |
| -------------- | -------------- | ----------------------------- | --------- | ----------- | -------------                                                                                                      |
| API base URL   | api_base_url   |                               | /         | Yes         | The base URL of the API to connect to.                                                                             |
| API key        | api_key        |                               | /         | Yes         | The API key to authenticate with the API.                                                                          |
{%- if cookiecutter.connector_type == 'external-import' or cookiecutter.connector_type == 'internal-enrichment' %}
| TLP Level      | tlp_level      |                               | /         | Yes         | The TLP level to assign to the imported data. Available values are: clear, white, green, amber, amber+strict, red. |
{%- endif %}


## Deployment

### Docker Deployment

Before building the Docker container, you need to set the version of pycti in `requirements.txt` equal to whatever
version of OpenCTI you're running. Example, `pycti==5.12.20`. If you don't, it will take the latest version, but
sometimes the OpenCTI SDK fails to initialize.

Build a Docker Image using the provided `Dockerfile`.

Example:

```shell
# Replace the IMAGE NAME with the appropriate value
docker build . -t [IMAGE NAME]:latest
```

Make sure to replace the environment variables in `docker-compose.yml` with the appropriate configurations for your
environment. Then, start the docker container with the provided docker-compose.yml

```shell
docker compose up -d
# -d for detached
```

### Manual Deployment

Create a file `config.yml` based on the provided `config.yml.sample`.

Replace the configuration variables (especially the "**ChangeMe**" variables) with the appropriate configurations for
you environment.

Install the required python dependencies (preferably in a virtual environment):

```shell
pip3 install -r requirements.txt
```

Then, start the connector from recorded-future/src:

```shell
python3 main.py
```

## Usage

After Installation, the connector should require minimal interaction to use, and should update automatically at a regular interval specified in your `docker-compose.yml` or `config.yml` in `duration_period`.

However, if you would like to force an immediate download of a new batch of entities, navigate to:

`Data management` -> `Ingestion` -> `Connectors` in the OpenCTI platform.

Find the connector, and click on the refresh button to reset the connector's state and force a new
download of data by re-running the connector.

## Behavior

<!--
Describe how the connector functions:
* What data is ingested, updated, or modified
* Important considerations for users when utilizing this connector
* Additional relevant details
-->


## Debugging

The connector can be debugged by setting the appropiate log level.
Note that logging messages can be added using `self.helper.connector_logger,{LOG_LEVEL}("Sample message")`, i.
e., `self.helper.connector_logger.error("An error message")`.

<!-- Any additional information to help future users debug and report detailed issues concerning this connector -->

## Additional information

<!--
Any additional information about this connector
* What information is ingested/updated/changed
* What should the user take into account when using this connector
* ...
-->

# COVID-19 ETL Pipeline

## Overview
This project implements a complete ETL pipeline that:
1. Extracts COVID-19 data from a public API
2. Transforms the data using Pandas
3. Loads the processed data into PostgreSQL
4. Orchestrates the process using Airflow
5. Containerizes the solution with Docker

## Data Source
Johns Hopkins University COVID-19 API:
https://corona.lmao.ninja/v3/covid-19/countries

## Transformation Steps
1. Flatten nested JSON structures
2. Select relevant columns
3. Convert timestamps to proper datetime format
4. Add processing metadata
5. Ensure consistent data types

## Data Destination
Processed data is loaded into a PostgreSQL database with the following structure:
- Table: `covid_stats`
- Columns: country info, case statistics, timestamps

## Pipeline Automation
The pipeline is automated using Airflow with:
- Daily scheduled runs
- Error handling and retries
- Email notifications on failure
- Dependency management between tasks

## Setup Instructions
1. Install Docker and Docker Compose
2. Clone this repository
3. Run `docker-compose up`
4. Access Airflow UI at http://localhost:8080
5. Trigger the `covid_etl_pipeline` DAG

## Future Enhancements
1. Add data quality checks
2. Implement incremental loading
3. Add analytics with DBT
4. Deploy to AWS using ECS/Fargate

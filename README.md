# ETL using Apache Airflow

This project demonstrates an ETL (Extract, Transform, Load) process using Apache Airflow to import data from CSV files, perform data transformation, and load it into a PostgreSQL database.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Tasks](#tasks)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The ETL process consists of the following tasks:

1. **Transform Data**: CSV files are loaded, and data is merged into one table using Python.
2. **Copy Data to Local**: The transformed data is copied to my local machine.
3. **Creating Table**: A PostgreSQL table is created with the appropriate columns.
4. **Insert Data to Table**: The merged data is inserted into the PostgreSQL table.

## Setup

### Prerequisites

- Docker
- Docker Compose
- Python (for data transformation)

### Docker Setup

1. Set up Docker as a container for my project.

### Airflow Setup

2. Set up Docker Compose to use the Apache Airflow web server, scheduler, and PostgreSQL database.  configured the environment in the `docker-compose.yaml` file.

3. Used the provided `Dockerfile` and `requirements.txt` to build your Airflow image.

### Configuration

Make sure to configure your Airflow environment, such as database connections and volumes, as needed in the `docker-compose.yaml` and `airflow.cfg` files.

## Tasks

### Task 1: Transform Data

- Python Operator: `transform_data`
- Description: Loads data from CSV files, merges tables, and saves the transformed data to a shared volume.

### Task 2: Copy Data to Local

- Python Operator: `copy_data_to_local`
- Description: Copies the transformed data to your local host.

### Task 3: Creating Table

- PostgreSQL Operator: `Creating_Table`
- Description: Creates a PostgreSQL table with columns matching the CSV file's structure.

### Task 4: Insert Data to Table

- PostgreSQL Operator: `Insert_Data_to_Table`
- Description: Inserts the transformed data from the CSV file into the PostgreSQL table.

## Usage

1. Start the Docker containers for Airflow and PostgreSQL using Docker Compose.

2. Access the Airflow web UI to trigger the DAG and monitor the ETL process.

3. Data transformation and loading into PostgreSQL will be automated based on your schedule settings.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [Your License Name] License - see the [LICENSE](LICENSE) file for details.

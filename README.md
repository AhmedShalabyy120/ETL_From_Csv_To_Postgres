# ETL using Apache Airflow

Hey there! This is my project showcasing an ETL (Extract, Transform, Load) process using Apache Airflow. It's all about taking data from CSV files, doing some cool transformations with Python, and then loading it into a PostgreSQL database.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Tasks](#tasks)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

So, here's what's happening in my ETL process:

1. **Transform Data**: We start by loading data from CSV files, and then we merge all the tables into one using Python magic.
2. **Copy Data to Local**: After that, we copy the transformed data to your local machine.
3. **Creating Table**: We create a PostgreSQL table with all the right columns to match our CSV data.
4. **Insert Data to Table**: Finally, we insert the transformed data from the CSV files into the PostgreSQL table.

## Setup

### Prerequisites

To get this show on the road, you'll need:

- Docker
- Docker Compose
- Python (for data transformation)

### Docker Setup

First, set up Docker as a container for the project.

### Airflow Setup

Then, let's get Apache Airflow in the mix:

1. Set up Docker Compose to use the Apache Airflow web server, scheduler, and PostgreSQL database. You can tweak the settings in the `docker-compose.yaml` file.

2. I've also provided a `Dockerfile` and `requirements.txt` to help you build your Airflow image.

### Configuration

Don't forget to configure your Airflow environment! Customize things like database connections and volumes in the `docker-compose.yaml` and `airflow.cfg` files to fit your needs.

## Tasks

Here's a quick rundown of the tasks that make up the ETL process:

### Task 1: Transform Data

- Python Operator: `transform_data`
- Description: Loads data from CSV files, merges tables, and saves the transformed data to a shared volume.

### Task 2: Copy Data to Local

- Python Operator: `copy_data_to_local`
- Description: Copies the transformed data to your local host.

### Task 3: Creating Table

- PostgreSQL Operator: `Creating_Table`
- Description: Creates a PostgreSQL table with columns that match the structure of the CSV files.

### Task 4: Insert Data to Table

- PostgreSQL Operator: `Insert_Data_to_Table`
- Description: Inserts the transformed data from the CSV files into the PostgreSQL table.

## Usage

Getting things rolling is easy:

1. Fire up the Docker containers for Airflow and PostgreSQL using Docker Compose.

2. Access the Airflow web UI to kick off the DAG (that's Airflow lingo for the ETL process) and keep an eye on how things are going.

3. The magic of data transformation and loading into PostgreSQL will happen automatically based on your schedule settings.

## Contributing

Got some ideas or improvements? I'm all ears! If you want to contribute to this project, here's how you can do it:

1. Fork the repository.

2. Create a fresh branch for your cool new feature or fix.

3. Make your changes and commit them.

4. Push your changes to your fork.

5. Then, send in a pull request to the main repository. Let's make this project even better together!

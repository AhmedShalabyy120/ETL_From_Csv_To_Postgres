from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
import pandas as pd
import shutil
import psycopg2

def transform_data():
    # Loading Data
    booking = pd.read_csv('/opt/airflow/data/booking.csv')
    client = pd.read_csv('/opt/airflow/data/client.csv')
    hotel = pd.read_csv('/opt/airflow/data/hotel.csv')
    
    # Merging Data
    data = pd.merge(booking, client, on="client_id")
    data.rename(columns={"Name": "Client_Name", 'type': 'Client_Type'}, inplace=True)

    data = pd.merge(data, hotel, on="hotel_id")
    data.rename(columns={'name': 'Hotel_Name'}, inplace=True)
    # Save the transformed data to a CSV file in a shared volume
    data.to_csv('/opt/airflow/data/generated_data.csv', index=False)

default_args = {
    "owner": 'airflow',
    "start_date": datetime(2023, 9, 7)
}

dag = DAG(
    dag_id='csv_to_postgressql',
    default_args=default_args,
    description="First Dag from flat file to postgres sql",
    catchup=False,
    schedule_interval=timedelta(days=1)
)

t1 = PythonOperator(
    task_id="transform_data",
    python_callable=transform_data,
    dag=dag
)

# Add a task to copy the generated data file to a shared volume
def copy_data_to_local():
    shutil.copy('/opt/airflow/data/generated_data.csv', 'E:\Data')

t2 = PythonOperator(
    task_id="copy_data_to_local",
    python_callable=copy_data_to_local,
    dag=dag
)

t3 = PostgresOperator(
    task_id='Creating_Table',
    postgres_conn_id='postgres',  
    sql="""
    CREATE TABLE IF NOT EXISTS Hotels_Data (
        client_id integer NOT NULL,
        booking_date text NOT NULL,
        room_type text NOT NULL,
        hotel_id integer NOT NULL,
        booking_cost numeric,
        currency text,
        age integer,
        client_name text,
        client_type text,
        hotel_name text
    );
    """,
    dag=dag,
)

# Add a task to insert data from CSV into the table
t4 = PostgresOperator(
    task_id='Insert_Data_to_Table',
    postgres_conn_id='postgres',
    sql="""
    INSERT INTO Hotels_Data (
        client_id, booking_date, room_type, hotel_id, booking_cost, currency, age, client_name, client_type, hotel_name, address
    )
    VALUES (
        4, '11/2/2016', 'first_class_2_bed', 6, 3140, 'GBP', 43, 'Bianca', 'VIP', 'The New View', 'address6'
    );
    """,
    dag=dag,
)


t1 >> t2 >> t3 >> t4

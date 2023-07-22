# Airflow Podcast Episodes

A data pipeline that can download and store podcast episodes using Airflow.

## _Create a virtual environment:_

```sh
python -m venv venv
```

## _Activate the virtual environment:_

```sh
source venv/bin/activate
```

## _Define a constraint URL:_

```sh
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.8.txt"
```

## _Install Airflow:_

```sh
pip install "apache-airflow==2.3.2" --constraint "${CONSTRAINT_URL}"
```

## _Setup Airflow database and user:_

```sh
airflow db init
airflow users create --username admin --password admin --firstname Teddy --lastname Mwangi --role Admin --email teddy@email.com
```

## _Run the Airflow webserver and scheduler:_

```sh
airflow webserver -D
airflow scheduler -D
```

## _Access the UI:_

```sh
http://localhost:8080
```

## _How to remove Airflow example DAGs:_

Open the airflow.cfg file and set load_examples = False. Then run:

```sh
airflow db reset
```

## _Tell airflow where we're storing our data pipelines:_

Open the airflow.cfg file and add the following in the core section:

```sh
dags_folder = /home/teddy/dev/inprogress/AirflowPodcastEpisodes
```

## _Create a .airflowignore file and add:_

```sh
venv/
```

## _How to create a SQLite database:_

```sh
sqlite3 episodes.db
# List the current databases.
.databases
.quit
```

## _Tell Airflow where the database is and how to access it:_

```sh
airflow connections add 'podcasts' --conn-type 'sqlite' --conn-host '/home/teddy/dev/inprogress/AirflowPodcastEpisodes/episodes.db'
```

## _Check that the database connection is configured correctly:_

```sh
airflow connections get podcasts
```

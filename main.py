from airflow.decorators import dag, task
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
import pendulum
import requests
import xmltodict

# Create a decorator for the data pipeline function.
@dag(
    dag_id="podcast_dag",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2023, 7, 21),
    catchup=False
)

def podcast_dag():
    create_database = SqliteOperator(
        task_id="create_table",
        sql=r"""
        CREATE TABLE IF NOT EXISTS podcast (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT
        )
        """
    )

    # Download podcast metadata (https://marketplace.org/feed/podcast/marketplace/).
    @task
    def get_episodes():
        data = requests.get("https://marketplace.org/feed/podcast/marketplace/")
        feed = xmltodict.parse(data.text)
        # Get the latest episodes.
        episodes = feed["rss"]["channel"]["item"]
        print(f"Found {len(episodes)} episodes.")
        return episodes

    podcast_episodes = get_episodes()
    create_database.set_downstream(podcast_episodes)

pod = podcast_dag()

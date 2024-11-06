from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta

# Funções de ETL
def extrair_dados(): # extração dos dados de uma fonte de uma ETL
    pass

def transformar_dados(): # manipular os dados extraídos
    pass

def carregar_dados(): #carregar dados na tabela de staging e nas tabelas de fato e dimensões
    pass

def criar_tabelas(): # criar as tabelas de staging e as tabelas de fato e dimensões
    pass

# Definindo parâmetros no DAG
default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 11, 6),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Pipeline ETL com Apache Airflow',
    schedule_interval=timedelta(days=1),  # Executar todos os dias
    catchup=False,  # Não executar datas anteriores
)

# Definindo as tarefas do DAG
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

criar_tabelas_task = PythonOperator(
    task_id='criar_tabelas',
    python_callable=criar_tabelas,
    dag=dag,
)

extrair_dados_task = PythonOperator(
    task_id='extrair_dados',
    python_callable=extrair_dados,
    dag=dag,
)

transformar_dados_task = PythonOperator(
    task_id='transformar_dados',
    python_callable=transformar_dados,
    dag=dag,
)

carregar_dados_task = PythonOperator(
    task_id='carregar_dados',
    python_callable=carregar_dados,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Definindo ordem das tarefas
start_task >> criar_tabelas_task >> extrair_dados_task >> transformar_dados_task >> carregar_dados_task >> end_task
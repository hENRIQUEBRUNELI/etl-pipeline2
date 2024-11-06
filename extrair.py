import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook

def extrair_dados(): # extração de dados da CSV
    df = pd.read_csv('data/raw/dados_vendas.csv')
    
    # Conectar o banco de dados para salvar na staging
    postgres_hook = PostgresHook(postgres_conn_id='meu_banco')
    conn = postgres_hook.get_conn()
    cursor = conn.cursor()
    
    # Inserindo dados extraídos na tabela de staging
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO staging_vendas (venda_id, cliente_id, produto_id, quantidade, valor, data)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row['venda_id'], row['cliente_id'], row['produto_id'], row['quantidade'], row['valor'], row['data']))
    
    conn.commit()
    cursor.close()
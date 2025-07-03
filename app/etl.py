import os
import duckdb
import pandas as pd
from pathlib import Path
import pandera.pandas as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine

#from app.schemas import ProdutoSchema, ProdutoSchemaKPI


def load_settings():
  """
  Load settings with environment variables
  """
  dotenv_path = Path.cwd() / '.env'
  load_dotenv(dotenv_path=dotenv_path)

  settings = {
    "db_host": os.getenv("POSTGRES_HOST"),
    "db_user": os.getenv("POSTGRES_USER"),
    "db_pass": os.getenv("POSTGRES_PASSWORD"),
    "db_name": os.getenv("POSTGRES_DB"),
    "db_port": os.getenv("POSTGRES_PORT"),
  }
  return settings

#@pa.check_output(ProdutoSchema.to_schema(), lazy=True)
def extrair_do_sql(query: str) -> pd.DataFrame:
    """
    Extrai dados do banco de dados SQL usando uma consulta fornecida.

    Args: 
      query: A consulta SQL para extrair dados.

    Returns: 
      Um DataFrame do Pandas contendo os dados extraidos.
    """
    
    settings = load_settings()

    #Criar a string de conexão com base nas configurações
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
          df_crm = pd.read_sql(query, conn)

    return df_crm          

#@pa.check_input(ProdutoSchema.to_schema(), lazy=True)
#@pa.check_output(ProdutoSchemaKPI.to_schema(), lazy=True)
def transformar(df: pd.DataFrame) -> pd.DataFrame:
     """
     Transforma dados da consulta SQL fornecida.

    Args: 
      DataFrame: O DataFrame da consulta fornecida.

    Returns: 
      Um DataFrame do Pandas contendo os dados transformados.
     """
     
     #Calcular valor_total_estoque
     df['valor_total_estoque'] = df['quantidade'] * df['preco']

     #Normalizar categoria para maiusculas
     df['categoria_normalizada'] = df['categoria'].str.upper()

     #Determinar disponibilidade (True se quantidade > 0)
     df['disponibilidade'] = df['quantidade'] > 0 

     return df

#@pa.check_input(ProdutoSchemaKPI.to_schema(), lazy=True)
def load_to_duckdb(df:pd.DataFrame, tablename:str, db_file:str = 'sql/my_duckdb.db'):
     """
     Carrega o DataFrame no DuckDB, criando ou substituindo a tabela especifica

     Args: 
        df: DataFrame do Pandas para ser carregado ao DuckDB
        table_name: Nome da tabela no DuckDB onde os dados serão inseridos.
        db_file: Caminho para o arquivo. Se não existir, será criado.     
     """
     #Conectar ao DuckDB. Se o arquivos não existir, ele será criado.
     con = duckdb.connect(database=db_file, read_only=False)

     #Registrar o DataFrame como uma tabela temporária
     con.register('df_temp', df)

     # Utilizar SQL para inserir os dados da tabela temporária em uma tabela
     # Se a tabela já existir, substitui.
     con.execute(f"CREATE OR REPLACE TABLE {tablename} AS SELECT * FROM df_temp")

     # Fechar a conexão
     con.close()

if __name__ == "__main__":

      query = "SELECT * FROM produtos_bronze_email"
      df_crm = extrair_do_sql(query=query)
      df_crm_kpi = transformar(df_crm)
      load_to_duckdb(df_crm_kpi,'tabela_kpi')
      print(df_crm)
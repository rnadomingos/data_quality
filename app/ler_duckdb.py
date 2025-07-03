import duckdb

def read_from_duckdb_and_print(tablename:str, db_file: str = 'sql/my_duckdb.db'):
    """
    Lê dados de uma tabela DuckDB e imprime os resultados.

    Parametros:
    - table name: Nome da tabela de onde os dados serão lidos.
    - db_file: Caminho paa o arquivo DuckDB.
    """
    #Conectar ao DuckDB
    con = duckdb.connect(database=db_file)

    #Executar consulta SQL
    query = f"SELECT * FROM {tablename}"
    result = con.execute(query).fetchall()

    con.close()

    # Imprimir os resultados
    for row in result:
        print(row)

    return result

if __name__ == '__main__':
    table_name = "tabela_kpi"
    read_from_duckdb_and_print(table_name)
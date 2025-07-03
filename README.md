# Workshop - Data Quality

Visite minha documentacao

[![image](/pic/fluxo_data_quality.png)](https://rnadomingos.github.io/data_quality/)


1. Clone o repositório:

```bash
git clone git@github.com:rnadomingos/data_quality.git
cd data_quality
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:

```bash
poetry env use 3.12.1
poetry shell
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
poetry run task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
poetry run task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
poetry run python app/etl.py
```
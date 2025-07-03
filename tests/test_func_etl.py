import pandas as pd
import pytest
from app.etl import transformar

def test_transformar():
    # Arrange: create test input DataFrame
    input_data = pd.DataFrame({
        'quantidade': [10, 0, 5],
        'preco': [2.5, 3.0, 4.0],
        'categoria': ['eletronico', 'livro', 'brinquedo']
    })

    # Act: apply the transformation
    result_df = transformar(input_data.copy())

    # Assert: check expected columns and values
    expected_valor_total_estoque = [25.0, 0.0, 20.0]
    expected_categoria_normalizada = ['ELETRONICO', 'LIVRO', 'BRINQUEDO']
    expected_disponibilidade = [True, False, True]

    pd.testing.assert_series_equal(
        result_df['valor_total_estoque'],
        pd.Series(expected_valor_total_estoque, name='valor_total_estoque'),
        check_dtype=False
    )

    pd.testing.assert_series_equal(
        result_df['categoria_normalizada'],
        pd.Series(expected_categoria_normalizada, name='categoria_normalizada')
    )

    pd.testing.assert_series_equal(
        result_df['disponibilidade'],
        pd.Series(expected_disponibilidade, name='disponibilidade')
    )

def test_transformar_normal_case():
    # Normal case with valid data
    input_data = pd.DataFrame({
        'quantidade': [10, 0, 5],
        'preco': [2.5, 3.0, 4.0],
        'categoria': ['eletronico', 'livro', 'brinquedo']
    })

    result_df = transformar(input_data.copy())

    expected_valor_total_estoque = [25.0, 0.0, 20.0]
    expected_categoria_normalizada = ['ELETRONICO', 'LIVRO', 'BRINQUEDO']
    expected_disponibilidade = [True, False, True]

    pd.testing.assert_series_equal(
        result_df['valor_total_estoque'],
        pd.Series(expected_valor_total_estoque, name='valor_total_estoque'),
        check_dtype=False
    )
    pd.testing.assert_series_equal(
        result_df['categoria_normalizada'],
        pd.Series(expected_categoria_normalizada, name='categoria_normalizada')
    )
    pd.testing.assert_series_equal(
        result_df['disponibilidade'],
        pd.Series(expected_disponibilidade, name='disponibilidade')
    )

def test_transformar_empty_dataframe():
    # Test empty DataFrame input
    input_data = pd.DataFrame(columns=['quantidade', 'preco', 'categoria'])
    result_df = transformar(input_data.copy())

    # Check the output still has the expected columns
    assert list(result_df.columns) == [
        'quantidade',
        'preco',
        'categoria',
        'valor_total_estoque',
        'categoria_normalizada',
        'disponibilidade'
    ]
    assert result_df.empty

def test_transformar_missing_values():
    # DataFrame with missing values
    input_data = pd.DataFrame({
        'quantidade': [10, None, 5],
        'preco': [2.5, 3.0, None],
        'categoria': ['eletronico', None, 'brinquedo']
    })

    result_df = transformar(input_data.copy())

    # Check calculations handle NaN properly
    assert pd.isna(result_df.loc[1, 'valor_total_estoque'])  # quantidade is NaN
    assert pd.isna(result_df.loc[2, 'valor_total_estoque'])  # preco is NaN
    assert pd.isna(result_df.loc[1, 'categoria_normalizada'])  # categoria is NaN
import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchemaEmail(pa.DataFrameModel):
    """
    Validation schema for product data using Pandera.

    This class defines validation rules for a DataFrame containing product
    information. Each column is typed and validated with specific constraints
    to ensure data integrity.

    Attributes:
        id_produto (int): Product identifier.
        nome (str): Product name. This field is required.
        quantidade (int): Product quantity in stock, must be between 20 and 200.
        preco (float): Product price, must be between 5.0 and 120.0. This field is required.
        categoria (str): Product category. This field is required.

    Config:
        coerce (bool): Automatically casts column types to those defined in the schema.
    """
       
    id_produto: Series[int]
    nome: Series[str] = pa.Field(nullable=False)
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=05.0, le=120.0, nullable=False)
    categoria: Series[str] = pa.Field(nullable=False)
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True


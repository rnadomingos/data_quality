import pandera as pa
from pandera.typing import Series


class ProdutoSchema(pa.DataFrameModel):
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

    class Config:
        coerce = True

class ProdutoSchemaKPI(ProdutoSchema):
    """
    Validation schema for product data KPI using Pandera.

    This class defines validation rules for a DataFrame containing product
    information. Each column is typed and validated with specific constraints
    to ensure data integrity.

    Attributes:
        valor_total_estoque (float): Store total values, must be start 0.0. This field is required.
        categoria_normalizada (str): Normalized Category. This field is required.
        disponibilidade (bool): Availability Status.

    Config:
        coerce (bool): Automatically casts column types to those defined in the schema.
    """

    valor_total_estoque: Series[float] = pa.Field(ge=0)
    categoria_normalizada: Series[str]
    disponibilidade: Series[bool]
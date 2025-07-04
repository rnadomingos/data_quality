from pandera import Check, Column, DataFrameSchema, Index, MultiIndex

schema = DataFrameSchema(
    columns={
        "id_produto": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=10.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "nome": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "quantidade": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=20.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=200.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "preco": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=5.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=120.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "categoria": Column(
            dtype="object",
            checks=None,
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(
                min_value=0.0, raise_warning=False, ignore_na=True
            ),
            Check.less_than_or_equal_to(
                max_value=9.0, raise_warning=False, ignore_na=True
            ),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=False,
    title=None,
    description=None,
)

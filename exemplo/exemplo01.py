from datetime import datetime

from pydantic import BaseModel, PositiveInt, validate_call

#import logfire


# logfire.configure()
# logfire.instrument_pydantic()  


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


# this will record details of a successful validation to logfire
#m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
#print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
#print(m.dimensions)
#> (10, 20)

#Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10'])

dado = {
    "timestamp": "2020-01-02T03:04:05Z",
    "dimensions": ["10","20"]
}

dado_delivery = Delivery(**dado)

class NumeroPositivo(BaseModel):
    numero: PositiveInt

@validate_call()
def calculadora(x:NumeroPositivo, y:NumeroPositivo) -> NumeroPositivo:
    return x+y

print(calculadora(10,4))
print(calculadora(6,7))
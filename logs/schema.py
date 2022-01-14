from logs.models import Log, LogBook
from ninja import Schema, ModelSchema


class LogBookSchemaIN(ModelSchema):
    owner_id: int

    class Config:
        model = LogBook
        model_fields = ['name', 'description']

class LogBookSchemaOUT(ModelSchema):
    class Config:
        model = LogBook
        model_fields = ['id', 'name', 'description', 'owner']

class LogSchemaIN(ModelSchema):
    book_id: int = None

    class Config:
        model = Log
        model_fields = ['mode', 'datetime', 'frequency', 'callsign', 'band']

class LogSchemaOUT(ModelSchema):
    class Config:
        model = Log
        model_fields = ['id', 'mode', 'datetime', 'frequency', 'callsign', 'band', 'book']

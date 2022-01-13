from django.conf import settings
from datetime import time, date
from ninja import Schema

class LogSchema(Schema):
    mode: str
    date: date
    frequency: float
    time: time
    callsign: str
    band: float

class LogBookSchema(Schema):
    owner: settings.AUTH_USER_MODEL
    name: str
    description: date

class NotFoundSchema(Schema):
    message: str

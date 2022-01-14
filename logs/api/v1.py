from logs.schema import LogSchemaIN, LogSchemaOUT, LogBookSchemaIN, LogBookSchemaOUT
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from logs.models import Log, LogBook
from typing import List, Optional
from ninja import NinjaAPI


api = NinjaAPI()

@api.get('/logbooks', response=List[LogBookSchemaOUT])
def logbooks(request):
    return LogBook.objects.all()

@api.get('/logs/{int:logbooks_id}', response={200: List[LogSchemaOUT]})
def log(request, logbooks_id: int, callsign: Optional[str] = None):
    book = get_object_or_404(LogBook, id=logbooks_id)
    
    if callsign:
        logs = Log.objects.filter(book=logbooks_id, callsign=callsign)
        return 200, logs

    logs = Log.objects.filter(book=logbooks_id)
    return 200, logs

@api.post("/logs", response={201: LogSchemaOUT})
def create_log(request, log: LogSchemaIN):
    book = get_object_or_404(LogBook, id=log.book_id)

    log = Log.objects.create(**log.dict())
    return log

@api.post("/logbooks", response={201: LogBookSchemaOUT})
def create_logbook(request, logbook: LogBookSchemaIN):
    user = get_object_or_404(get_user_model(), id=logbook.owner_id)

    logbook = LogBook.objects.create(**logbook.dict())
    return logbook

@api.put("/logs/{int:log_id}", response={200: LogSchemaOUT})
def update_log(request, log_id: int, data: LogSchemaIN):
    log = get_object_or_404(Log, id=log_id)
    
    if hasattr(data, "book_id") and data.book_id == None:
        setattr(data, "book_id", log.book_id)
    
    book = get_object_or_404(LogBook, id=data.book_id)
    
    for attr, value in data.dict().items():
        setattr(log, attr, value)
    log.save()
    
    return 200, log

@api.put("/logbooks/{int:logbook_id}", response={200: LogBookSchemaOUT})
def update_logbook(request, logbook_id: int, data: LogBookSchemaIN):
    logbook = get_object_or_404(LogBook, id=logbook_id)
    if hasattr(data, "owner_id"):
        delattr(data, "owner_id")
    
    for attr, value in data.dict().items():
        setattr(logbook, attr, value)
    logbook.save()
    
    return 200, logbook

@api.delete("/logs/{int:log_id}", response={200: None})
def delete_log(request, log_id: int):
    log = get_object_or_404(Log, id=log_id)
    
    log.delete()
    
    return 200

@api.delete("/logbooks/{int:logbook_id}", response={200: None})
def delete_logbook(request, logbook_id: int):
    logbook = get_object_or_404(LogBook, id=logbook_id)
    
    logbook.delete()
    
    return 200

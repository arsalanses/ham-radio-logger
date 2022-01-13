from logs.schema import LogSchema, LogBookSchema, NotFoundSchema
from logs.models import Log, LogBook
from ninja import NinjaAPI
from typing import List, Optional

api = NinjaAPI()

@api.get('/logbooks', response=List[LogBookSchema])
def logbooks(request):
    return LogBook.objects.all()

@api.get('/logs/{logbooks_id}', response={200: List[LogSchema], 404: NotFoundSchema})
def log(request, logbooks_id: int, callsign: Optional[str] = None):
    if callsign:
        logs = Log.objects.filter(book=logbooks_id, callsign=callsign)
        return 200, logs

    # try:
    logs = Log.objects.filter(book=logbooks_id)
    return 200, logs
    # except Log.DoesNotExist as e:
        # return 404, {"message": "LogBook does not exist"}

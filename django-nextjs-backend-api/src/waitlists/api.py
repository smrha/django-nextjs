from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404

from .models import WailtlistEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WailtlistEntry.objects.all()
    return qs

@router.get("{entry_id}", response=WaitlistEntryDetailSchema)
def list_waitlist_entries(request, entry_id:int):
    obj = get_object_or_404(WailtlistEntry, id=entry_id)
    return obj
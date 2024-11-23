#django-nextjs-backend-api\src\waitlists\api.py
from ninja import Router
from typing import List
import helpers
import json
from ninja_jwt.authentication import JWTAuth
from .models import WaitlistEntry
from .schemas import (
   WaitlistEntryListSchema, 
   WaitlistEntryDetailSchema,
   WaitlistEntryCreateSchema,
   ErrorWaitlistEntryCreateSchema)
from django.shortcuts import get_object_or_404 #very good when dealing with IDs in django
from .forms import WaitlistEntryCreateForm

router = Router()
#/api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema],
auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
   #qs = WaitlistEntry.objects.all()
   #can filter as below
   qs = WaitlistEntry.objects.filter(user=request.user)
   return qs

#/api/waitlists/
@router.post("",response={
   200: WaitlistEntryDetailSchema,
   400:ErrorWaitlistEntryCreateSchema},
   auth=helpers.api_auth_user_or_annon)
def create_waitlist_entry(request,data:WaitlistEntryCreateSchema): #schema validating against
   #print(data)
   #creating new object to store the data on the database
   form = WaitlistEntryCreateForm(data.dict())
   if not form.is_valid():
      #cleaned_data = form.cleaned_data
      #obj = WaitlistEntry.objects.create(**cleaned_data())
      #print(request.user)#gives AnonymousUser with no auth=JWTAuth()
      form.errors = json.loads(form.errors.as_json())
      print(form.errors)
      return 400, form.errors
   
   obj = form.save(commit=False)
   if request.user.is_authenticated:
      obj.user = request.user #way 1 or as below
      #obj.user_id = request.user
      obj.save()
   return obj



@router.get("{entry_id}", response=WaitlistEntryDetailSchema,
auth=helpers.api_auth_user_required)
def get_waitlist_entry(request,entry_id:int):
   obj = get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)#pass id as an argument
   return obj

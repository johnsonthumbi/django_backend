#django-nextjs-backend-api\src\waitlists\schemas.py
from typing import List, Any, Optional
from datetime import datetime
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data we want to send in
    # WaitlistEntryIn
    email: EmailStr #accepting emai itself

class ErrorWaitlistEntryCreateSchema(Schema):
    
    #email: List[dict]
    email: List[Any]
   # non_field_errors:List[dict]=[]

class WaitlistEntryDetailSchema(Schema):
    # Get method for he data-> Data
    # WaitlistEntryOut
    #id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
    #description: Optional[str] = ""
class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    #updated: datetime
    #timestamp: datetime
    #description: Optional[str] = ""



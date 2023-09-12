from requests import Response
from datetime import date, datetime
from dataclasses import dataclass,field
from typing import Union, TypedDict, Literal, Generic, TypeVar, List
from .user import TLUser
from dateutil import parser
from dataclasses_json import dataclass_json,config

@dataclass
class TLPage():
    size:int
    number:int

@dataclass
class TLFilter():
    user_id:str
    _started_after:date = field(kw_only=True,repr=False,metadata=config(exclude=lambda x:True))
    _ended_before:date = field(kw_only=True,repr=False,metadata=config(exclude=lambda x:True))
    started_after:str = field(init=False)
    ended_before:str = field(init=False)
    def __post_init__(self):
        self.started_after = self._started_after.strftime("%Y-%m-%dT%H:%M:%S+01:00")
        self.ended_before = self._ended_before.strftime("%Y-%m-%dT%H:%M:%S+01:00")

@dataclass_json
@dataclass
class TLBody():
    filter: TLFilter
    page:TLPage



@dataclass_json
@dataclass
class TLActivityType:
    id: str
    type: Literal["activityType"]

@dataclass_json
@dataclass
class TLSubject:
    activity_type: TLActivityType
    description: str
    type: any
    id:str
    has_access: bool
    related_customer: any

@dataclass_json
@dataclass
class TLWorkType:
    id: str
    type: Literal["workType"]

@dataclass_json
@dataclass
class TLTimeTracking:
    description: str
    duration: int
    date_ended_at:date = field(init=False,metadata=config(exclude=lambda x:True))
    ended_at: str 
    id: str
    invoiceable: bool
    date_started_at:date = field(init=False,metadata=config(exclude=lambda x:True))
    started_at: str 
    date_started_on:date = field(init=False,metadata=config(exclude=lambda x:True))
    started_on: str
    subject: Union[TLSubject,None]
    type: Union[Literal["start_stop"],None]
    user: TLUser
    work_type: Union[TLWorkType,None]
    def __post_init__(self):
        self.date_ended_at = parser.parse(self.ended_at,dayfirst=False)
        self.date_started_at = parser.parse(self.started_at,dayfirst=False)
        self.date_started_on = parser.parse(self.started_on,dayfirst=False)
        self.subject = TLSubject(**self.subject) if isinstance(self.subject, dict) else self.subject
        self.user =  TLUser(**self.user) if isinstance(self.user, dict) else self.user
        self.work_type = TLWorkType(**self.work_type) if isinstance(self.work_type, dict) else self.work_type


T = TypeVar('T')
@dataclass_json
@dataclass
class TLResponse(Generic[T]):
    data: List[T]
    raw: Response

class Proxy(TypedDict):
    protocol: str
    url: str
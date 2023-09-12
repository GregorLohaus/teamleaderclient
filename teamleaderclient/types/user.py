from dataclasses import dataclass,field;
from dataclasses_json import dataclass_json
from typing import List, Literal, TypedDict, Union
@dataclass_json
@dataclass
class TLAccount:
    type: Literal["account"]
    id: str

@dataclass_json
@dataclass
class TLPhone:
    type:Literal["mobile"]
    number: str
@dataclass_json
@dataclass
class TLUser:
    id: str
    type: Literal["user"]
    account: Union[TLAccount,None] = field(default=None)
    first_name: Union[str,None] = field(default=None)
    last_name: Union[str,None] = field(default=None)
    email: Union[str,None] = field(default=None)
    language: Union[str,None] = field(default=None)
    telephones: Union[List[TLPhone],None] = field(default=None)
    
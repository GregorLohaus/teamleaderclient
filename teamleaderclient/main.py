import requests
import json
from dataclasses import dataclass,field
from typing import Union
from .types import TLBody, TLResponse, TLTimeTracking, Proxy

@dataclass
class TLSession:
    session: requests.Session = field(init=False)
    auth_header: dict = field(init=False)
    email:str
    password:str
    proxy_url:Union[Proxy,None] = field(default=None)
    
    def __post_init__(self):
        self.session = requests.session()
        self.session.post("https://api.auth.focus.teamleader.eu/users.login",json={"email":self.email,"password":self.password})
        oauth_result = self.session.post("https://focus.teamleader.eu/oauth2/access_token", json={"grant_type":"TL.authentication.oauth2.session_grant","client_id":"web_app","client_secret":""})
        self.auth_header = {"Authorization": f"Bearer {json.loads(oauth_result.text)['access_token']}"}
        if self.proxy_url is not None:
            self.session.proxies.update(self.proxy_url)

    def get_user_id(self)->Union[str,any]:
        response =self.session.post(
            url="https://api.focus.teamleader.eu/customerMeetingUsers.me",
            headers=self.auth_header,
            proxies= self.session.proxies
        )
        try:
            result = json.loads(response.text)["data"]["id"]
            return result
        except Exception as e:
            print(e)
            exit(1)

    def get_time_tracking(self,body:TLBody)->TLResponse[Union[TLTimeTracking,any]]:
        response = self.session.post(
            url="https://api.focus.teamleader.eu/timeTracking.list",
            json=json.loads(body.to_json()),
            headers=self.auth_header,
            proxies= self.session.proxies
        )
        try:
            data = [TLTimeTracking(**x) for x in json.loads(response.text)["data"] ]
            response = TLResponse(data=data,raw=response)
            return response
        except Exception as e:
            print(e)
            exit(1)

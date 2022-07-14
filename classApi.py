from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import json


class Api:

    def __init__(self):
        self.urlPost = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/addSmart'
        self.urlDelete = 'https://dev.synerboard.com/serverBeer/rest/smartFinal/deleteAll'

    def metodoPost(self,request):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        response = requests.post(self.urlPost,json=request)
        return response.text

    def metodoDelete(self):
        try:
            response = requests.delete(self.urlDelete)
            return response.json()
        except:
            return "ocurrio un error"

    def getstatus(self):

        status = requests.get('https://dev.synerboard.com/serverBeer/rest/smartFinal/GetSet')
        return status.text

    def getUpdate(self):

        getData = requests.get('https://dev.synerboard.com/serverBeer/rest/smartFinal/GetUpdate')
        return getData.json()

    def UPdateStatus(self):

        getData = requests.get('https://dev.synerboard.com/serverBeer/rest/smartFinal/UpdateTrue')
        return getData.text



        
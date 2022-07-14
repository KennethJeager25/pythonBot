import json

class jsonFile:

    def __init__(self,filename):
        self.filename=filename if filename==None else 'temp_CH2.json'
    
    def getDataJson(self):
        try:
            with open(self.filename) as file:
                data=json.load(file)
                return data
        except:
            return "ocurrio un error"
        
    def toJson(self,listach1):
        try:
            with open(self.filename,"w") as data_json:
                data_json.write(json.dumps(listach1, indent=4))
        except:
            return "ocurrio un error"
from guardarCH2 import jsonFile
from classApi import Api

class temp_CH2(jsonFile):

    def __init__(self,name="",value="",sp="",lista=[]):
        super().__init__("temp_CH2.json")
        self.name = name
        self.value = value
        self.sp = sp
        self.namefile="temp_CH2.json"
        self.lista = lista
        self.api = Api()

    def addCh2(self,temp):
        try:
            self.lista.append(temp)
            return "dato guardado"
        except:
            return "error al guardar"

    def deleteAllTemp(self):
        try:
            self.lista = []
        except:
            return "lista vacia"

    def showData(self):
        try:
            return self.lista
        except:
            return "lista vacia"

    def guardarDatos(self):
        json_data={}
        json_data['Temp_CH2']=[]
        for x in self.lista:
            arreglo_Json={
                'name':f'{x.name}',
                'value':f'{x.value}',
                'sp':f'{x.sp}',
            }
            json_data['Temp_CH2'].append(arreglo_Json)
        self.toJson(json_data)


    def ApiRequest(self):
        file = self.getDataJson()
        for x in file['Temp_CH2']:
            data = {
                'name':x['name'],
                'value':x['value'],
                'sp':x['sp'],
            }
            self.api.metodoPost(data)

    def imprimirJson(self):
        file = self.getDataJson()
        for x in file['Temp_CH2']:
            print(x)

    def __str__(self):
        return f"name:{self.name},value:{self.value},sp:{self.sp}"
    
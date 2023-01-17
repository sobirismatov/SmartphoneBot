import json

class DB:
    def __init__(self,path):
        self.path = path
        # Read the data from the file
        self.data = {}
        with open(self.path,'r') as f:
            self.data = json.load(f)


    def getPhone(self,brand):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        data = {
            'model':'',
            'color':'',
            'ram':'',
            'price':'',
            'memory':'',
            'image':'',
        }

        

db = DB('db.json')
print(db.path)
print(db.data)
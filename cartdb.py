import json
class Cart:
    def __init__(self,path:str):
        self.path = path
        self.data = {
            'cart':[]
        }
        with open(self.path,'r') as file:
            self.data = json.load(file)

    def add(self,brand,model):
        self.data['cart'].append({
            'brand':brand,
            'model':model
        })
        self.save()

    def save(self):
        with open(self.path,'w') as file:
            json.dump(self.data,file,indent=4)


# cart = Cart('cartdb.json')
# cart.add('Redmi','Redmi 9')
# print(cart.data)


        
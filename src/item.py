
class Item:
    name, description = (str,)*2
   
    def __init__(self,name,description):
        self.name=name
        self.description = description

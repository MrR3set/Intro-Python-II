# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    name,description = (str,)*2
    inventory = ["1","2","3"]
    n_to, s_to, e_to, w_to = ({},)*4

    def __init__(self,name,description):
        self.name=name
        self.description=description

    def __str__(self):
        return f'{self.name}\n{self.description}'
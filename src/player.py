# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    name = str
    currentPos = {}
    inventory = ["nothing"]

    def __init__(self,name,currentPos):
        self.name=name
        self.currentPos = currentPos

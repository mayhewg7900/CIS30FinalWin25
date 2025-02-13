class Restaurant:
    def __init__(self, name, items):
        self.name = name
        self.items = items
    def getItem(self, item):
        for curItem in self.items.keys():
            if curItem == item:
                return item
        return False

class Appointments:
    def __init__(self):
        self.name = ''
        self.items = ['']
        self.total = 0.0
        self.date = ''
        self.time = ''
    def setDate(self, newDate):
        self.date = newDate
    def setName(self, newName):
        self.name = newName
    def setItems(self, newItems):
        self.items = newItems[:]
    def setTime(self, newTime):
        self.time = newTime
    def setTotal(self, newTotal):
        self.total = newTotal
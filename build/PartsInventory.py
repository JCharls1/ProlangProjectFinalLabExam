class PartsInventory:
    def __init__(self):
        self.Parts = {}
        self.numbers = {}
    
    def addPart(self, Parts, number):
        self.Parts[number] = Parts
        self.numbers[number] = number
    
    def updatePart(self, Parts, number):
        for num in self.numbers:
            if(num == number):
                self.Parts[number] = Parts
            print("nigga")
        
    def currNumber():
        return len(self.Parts)
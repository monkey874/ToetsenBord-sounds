import os

class loader:
    def __init__(self, AantalPads, file): 
        self.AantalPads = AantalPads
        self.files = file




    def LoadFile(self):
            aantalpaden = [];
            for i in range(self.AantalPads):
                while True:
                    inputFile = input("Voer het pad naar het mp3-bestand in: ")
                    if  os.path.isfile(inputFile):
                        if os.path.splitext(inputFile)[1] == self.files:
                            aantalpaden.append(inputFile)
                            break
                        else:
                            print("Het bestand is geen mp3-bestand. Probeer het opnieuw.")
                    else:
                        print("Het bestand bestaat niet. Probeer het opnieuw.")
            
            return aantalpaden
        

    
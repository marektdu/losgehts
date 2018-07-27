class Restaurant():

    def __init__(self, name = None, coordinates = None, openinghours = None, freeSeats = None
):

        self.name = name
        self.coordinates = coordinates
        self.openinghours = openinghours
        self.freeSeats = freeSeats



    def __repr__(self):
        ret = "der Name von Restaurant : " + self.name  +  " Koordinaten : " + str(self.coordinates)  #+  "Oefnungszeiten : " + self.openinghours +  "Anzahl von frei Plaetze : " + self.freeSeats

        return ret



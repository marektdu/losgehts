from math import sqrt
import AsimCanALKAN

class Distance():



    def __init__(self):
        self.Person_Distance_X=int(AsimCanALKAN.a)
        self.Person_Distance_Y=int(AsimCanALKAN.b)
        self.Restaurant_Distance_X=int(AsimCanALKAN.c)
        self.Restaurant_Distance_Y=int(AsimCanALKAN.d)


        self.Distance = sqrt((self.Person_Distance_X - self.Restaurant_Distance_X)**2+(self.Person_Distance_Y - self.Restaurant_Distance_Y)**2)

    @staticmethod
    def compute_distance(aa_xx, aa_yy, bb_xx, bb_yy ):

        distance = sqrt((aa_xx - bb_xx)**2+(aa_yy-bb_yy)**2)
        return distance


print("Distance = " + str(Distance.compute_distance(AsimCanALKAN.a,AsimCanALKAN.b,AsimCanALKAN.c,AsimCanALKAN.d)))


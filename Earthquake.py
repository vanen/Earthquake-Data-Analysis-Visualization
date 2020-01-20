import datetime, time

class Earthquake:
    def __init__(self, mag, time, depth, place, title, felt, region):
        self.mag = mag
        self.time = Time(time)
        self.depth = depth
        self.place = place
        self.title = title
        self.felt = felt
        self.region = region

    # returning a dictionary of earthquake data
    def eq_dict(self):
        return {
                'Magnitude': self.mag,
                'Time': self.time,
                'Depth': self.depth,
                'Place': self.place,
                'Title': self.title,
                'Felt': self.felt,
                'Region': self.region
                }

    # defining a property for mag
    @property
    def mag(self):
        return self.__mag

    # using setter to check if float, if not then it changes it to a float
    @mag.setter
    def mag(self, m):
        if not isinstance(m, float):
            m = float(m)
        self.__mag = m

    # string override to return a simple description of earthquake data; turning mag into a str to allow concatination
    def __str__(self):
        return 'A magnitude ' + str(self.mag) + ' earthquake located in ' + self.region + ' on ' + self.time.time

# creating a Time class to modify time to human readable and convert to isoformat remove T with a space as delimiter
class Time:
    def __init__(self, time):
        self.time = datetime.datetime.fromtimestamp(int(time/1000))

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, t):
        t = t.isoformat(" ","seconds")
        t = str(t)
        self.__time = t

    def __str__(self):
        return self.time
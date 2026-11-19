class Helicopter:
    def __init__(self, passengers=0, name="Unknown", max_speed=0, model="Unknown", year=0, manufacturer="Unknown"):
        self.__passengers = passengers
        self.__name = name
        self.__max_speed = max_speed
        self._model = model
        self.year = year
        self.manufacturer = manufacturer
    
    def get_passengers(self):
        return self.__passengers

    def get_name(self):
        return self.__name

    def get_max_speed(self):
        return self.__max_speed

    def __str__(self):
        return (f"{self.__name} ({self._model}): {self.__passengers} пас., "
                f"{self.__max_speed} км/год, {self.year}, {self.manufacturer}")

    def __repr__(self):
        return (f"Helicopter({self.__passengers!r}, {self.__name!r}, "
                f"{self.__max_speed!r}, {self._model!r}, {self.year!r}, "
                f"{self.manufacturer!r})")

    def __del__(self):
        name = getattr(self, "_Helicopter__name", "невідомий")
        print(f"Об'єкт {name} знищено")
        
    def check_model(self):
        if self._model == "Mi-8":
            print("Це вертоліт Мі-8")
        else:
            print(f"Модель: {self._model}")
    

def main():
    h1 = Helicopter()
    h2 = Helicopter("Mi-2T", 8, "Mi-2", 194, 1965, "PLZ")
    h3 = Helicopter("R44 Raven II", 5, "Bell 407", 259, 2014, "Bell")
    h4 = Helicopter("EC135", 6, "Eurocopter EC135", 254, 1996, "Airbus Helicopters")
    h5 = Helicopter("Mi-8")
    for h in (h1, h2, h3, h4, h5):
        
        print(h)
        print(repr(h))
        print(h.get_passengers(), h.get_name(), h.get_max_speed(),
        h._model, h.year, h.manufacturer)
        h.check_model()

if __name__ == "__main__":
    main()
    
#my coment
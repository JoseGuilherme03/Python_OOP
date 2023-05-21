from enum import Enum


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"


class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELETRIC = "eletric"


class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"


class Guitar:
    def __init__(self, serial_number, price, spec):
        self._serial_number = serial_number
        self._price = price
        self._spec = spec

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Preço não pode ser negativo")
        self._price = new_price

    @property
    def spec(self):
        return self._spec

    def __str__(self):
        return f"Serial Number: {self.serial_number}, Price: {self.price}, Builder: {self.spec.builder.value}, Model: {self.spec.model}, Type: {self.spec.typeg.value}, Back Wood: {self.spec.back_wood.value}, Top Wood: {self.spec.top_wood.value}"


class GuitarSpec:
    def __init__(self, typeg, back_wood, top_wood, builder, model):
        self._typeg = typeg
        self._back_wood = back_wood
        self._top_wood = top_wood
        self._builder = builder
        self._model = model

    @property
    def typeg(self):
        return self._typeg

    @property
    def back_wood(self):
        return self._back_wood

    @property
    def top_wood(self):
        return self._top_wood

    @property
    def builder(self):
        return self._builder

    @property
    def model(self):
        return self._model


class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, *args):
        for guitar in args:
            self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.serial_number == serial_number:
                print(guitar)
            else:
                print("Nenhum guitarra encontrada com esse serial number")

    def search_guitar(self, search_guitar):
        list_guitar = []
        if self.guitars:
            for guitar in self.guitars:
                if search_guitar.builder != guitar.builder:
                    continue

                model = search_guitar.model.lower()
                if model != "" and model != guitar.model.lower():
                    continue

                if search_guitar.typeg != guitar.typeg:
                    continue

                if search_guitar.back_wood != guitar.back_wood:
                    continue

                if search_guitar.top_wood != guitar.top_wood:
                    continue

                list_guitar.append(guitar)

        if list_guitar:
            print("Guitarra(s) encontrada(s): ")
            for guitar in list_guitar:
                print(guitar)
                print()

        else:
            print("Nenhuma guitarra encontrada")

inventory = Inventory()
inventory.add_guitar(
    Guitar(
        serial_number="1",
        price=1499.95,
        spec=GuitarSpec(
            typeg=TypeG.ELETRIC,
            back_wood=Wood.ALDER,
            top_wood=Wood.ALDER,
            builder=Builder.FENDER,
            model="Stratocastor",
        ),
    ),
    Guitar(
        serial_number="2",
        price=1549.95,
        spec=GuitarSpec(
            typeg=TypeG.ELETRIC,
            back_wood=Wood.ALDER,
            top_wood=Wood.ALDER,
            builder=Builder.FENDER,
            model="Stratocastor",
        ),
    ),
    Guitar(
        serial_number="3",
        price=1899.99,
        spec=GuitarSpec(
            typeg=TypeG.ELETRIC,
            back_wood=Wood.BRAZILIAN_ROSEWOOD,
            top_wood=Wood.BRAZILIAN_ROSEWOOD,
            builder=Builder.FENDER,
            model="Stratocastor",
        ),
    ),
)

for guitar in inventory.guitars:
    print(guitar)
from enum import Enum
from tabulate import tabulate


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
        data = [
            ["Serial Number", self.serial_number],
            ["Price", self.price],
            ["Builder", self.spec.builder.value],
            ["Model", self.spec.model],
            ["Type", self.spec.typeg.value],
            ["Back Wood", self.spec.back_wood.value],
            ["Top Wood", self.spec.top_wood.value],
        ]

        table = tabulate(data, headers=["Attribute", "Value"], tablefmt="fancy_grid")

        return table


class GuitarSpec:
    def __init__(self, typeg, back_wood, top_wood, builder, model, num_strings):
        self._typeg = typeg
        self._back_wood = back_wood
        self._top_wood = top_wood
        self._builder = builder
        self._model = model
        self._num_strings = num_strings

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

    @property
    def num_strings(self):
        return self._num_strings

    def matches(self, otherspec):
        if self.builder != otherspec.builder:
            return False
        if self.model and self.model.lower() != otherspec.model.lower():
            return False
        if self.typeg != otherspec.typeg:
            return False
        if self.back_wood != otherspec.back_wood:
            return False
        if self.top_wood != otherspec.top_wood:
            return False
        if self.num_strings != otherspec.num_strings:
            return False
        return True


class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, *args):
        for guitar in args:
            self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        if self.guitars:
            for guitar in self.guitars:
                if guitar.serial_number == serial_number:
                    return guitar
        return "Guitarra não encontrada"

    def search(self, searchguitar):
        matching_guitars = []
        for guitar in self.guitars:
            if guitar.spec.matches(searchguitar):
                matching_guitars.append(guitar)
        return matching_guitars


def main():
    inventory = Inventory()

    # Adicionando guitarras no inventário
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
                num_strings=6
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
                num_strings=12
            ),
        ),
        Guitar(
            serial_number="3",
            price=549.95,
            spec=GuitarSpec(
                typeg=TypeG.ACOUSTIC,
                back_wood=Wood.ALDER,
                top_wood=Wood.ALDER,
                builder=Builder.FENDER,
                model="Stratocastor",
                num_strings=6
            ),
        )
    )

    # Guitarra que o cliente está procurando
    guitar_erin_like1 = GuitarSpec(
        typeg=TypeG.ELETRIC,
        back_wood=Wood.ALDER,
        top_wood=Wood.ALDER,
        builder=Builder.FENDER,
        model="Stratocastor",
        num_strings=6,
    )

    matchingGuitars = inventory.search(guitar_erin_like1)

    if matchingGuitars:
        print("Erin, talvez você goste destas: ")
        for guitar in matchingGuitars:
            print(guitar)
    else:
        print("Desculpe Erin, não temos nada para você")


if __name__ == "__main__":
    main()

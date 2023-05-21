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
        if self.guitars:
            for guitar in self.guitars:
                if guitar.serial_number == serial_number:
                    return guitar
        return "Guitarra não encontrada"

    def search_guitar(self, search_guitar):
        list_guitar = []
        if self.guitars:
            for guitar in self.guitars:
                if search_guitar.builder != guitar.spec.builder:
                    continue

                model = search_guitar.model.lower()
                if model != "" and model != guitar.spec.model.lower():
                    continue

                if search_guitar.typeg != guitar.spec.typeg:
                    continue

                if search_guitar.back_wood != guitar.spec.back_wood:
                    continue

                if search_guitar.top_wood != guitar.spec.top_wood:
                    continue

                list_guitar.append(guitar)

        if list_guitar:
            print("\033[32mGuitarra(s) encontrada(s): \033[0m")
            for guitar in list_guitar:
                print(guitar)
                print()

        else:
            print("Nenhuma guitarra encontrada")


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

# Pesquisando por uma guitarra específica
guitar_erin_like1 = GuitarSpec(
    typeg=TypeG.ELETRIC,
    back_wood=Wood.ALDER,
    top_wood=Wood.ALDER,
    builder=Builder.FENDER,
    model="Stratocastor",
)

guitar_joe_like1 = GuitarSpec(
    typeg=TypeG.ELETRIC,
    back_wood=Wood.BRAZILIAN_ROSEWOOD,
    top_wood=Wood.BRAZILIAN_ROSEWOOD,
    builder=Builder.FENDER,
    model="Stratocastor",
)

# Pesquisando por guitarras que o Erin gosta
inventory.search_guitar(guitar_erin_like1)


# Outros testes #
# print(inventory.get_guitar("2"))
# print(inventory.get_guitar("4"))
# inventory.search_guitar(guitar_joe_like1)

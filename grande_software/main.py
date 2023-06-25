from enum import Enum
from tabulate import tabulate


class Style(Enum):
    A = "a"
    F = "f"


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


from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self, serial_number, price):
        self._serial_number = serial_number
        self._price = price

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

    @abstractmethod
    def __str__(self):
        pass


class Guitar(Instrument):
    def __init__(self, serial_number, price, spec):
        super().__init__(serial_number, price)
        self._spec = spec

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


class Mandolin(Instrument):
    def __init__(self, serial_number, price, spec):
        super().__init__(serial_number, price)
        self._spec = spec

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
            ["Style", self.spec.style.value],
        ]

        table = tabulate(data, headers=["Attribute", "Value"], tablefmt="fancy_grid")

        return table


class InstrumentSpec(ABC):
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

    @abstractmethod
    def matches(self):
        pass


class GuitarSpec(InstrumentSpec):
    def __init__(self, typeg, back_wood, top_wood, builder, model, num_strings):
        super().__init__(typeg, back_wood, top_wood, builder, model)
        self._num_strings = num_strings

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


class MandolinSpec(InstrumentSpec):
    def __init__(self, typeg, back_wood, top_wood, builder, model, style):
        super().__init__(typeg, back_wood, top_wood, builder, model)
        self._style = style

    @property
    def style(self):
        return self._style

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
        if self.style != otherspec.style:
            return False
        return True


class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, *args):
        for instrument in args:
            self.instruments.append(instrument)

    def get_instrument(self, serial_number):
        if self.instruments:
            for instrument in self.instruments:
                if instrument.serial_number == serial_number:
                    return instrument
        return "Instrumento não encontrado"

    def search(self, searchinstrument):
        matching_instruments = []
        for instrument in self.instruments:
            if instrument.spec.matches(searchinstrument):
                matching_instruments.append(instrument)
        return matching_instruments


def main():
    inventory_guitars = Inventory()
    inventory_mandolins = Inventory()

    # Adicionando guitarras no inventário
    inventory_guitars.add_instrument(
        Guitar(
            serial_number="1",
            price=1499.95,
            spec=GuitarSpec(
                typeg=TypeG.ELETRIC,
                back_wood=Wood.ALDER,
                top_wood=Wood.ALDER,
                builder=Builder.FENDER,
                model="Stratocastor",
                num_strings=6,
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
                num_strings=12,
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
                num_strings=6,
            ),
        ),
    )

    inventory_mandolins.add_instrument(
        Mandolin(
            serial_number="4",
            price=549.95,
            spec=MandolinSpec(
                typeg=TypeG.ACOUSTIC,
                back_wood=Wood.ALDER,
                top_wood=Wood.ALDER,
                builder=Builder.FENDER,
                model="Stratocastor",
                style=Style.A,
            ),
        )
    )

    # Instrumentos que os clientes está procurando
    guitar_erin_like1 = GuitarSpec(
        typeg=TypeG.ELETRIC,
        back_wood=Wood.ALDER,
        top_wood=Wood.ALDER,
        builder=Builder.FENDER,
        model="Stratocastor",
        num_strings=6,
    )

    mandolin_joseph_like1 = MandolinSpec(
        typeg=TypeG.ACOUSTIC,
        back_wood=Wood.ALDER,
        top_wood=Wood.ALDER,
        builder=Builder.FENDER,
        model="Stratocastor",
        style=Style.A,
    )

    matching_instrument_erin = inventory_guitars.search(guitar_erin_like1)

    matching_instrument_joseph = inventory_mandolins.search(mandolin_joseph_like1)

    if matching_instrument_erin:
        print("Erin, talvez você goste destas: ")
        for guitar in matching_instrument_erin:
            print(guitar)
    else:
        print("Desculpe Erin, não temos nada para você")
    
    if matching_instrument_joseph:
        print("Joseph, talvez você goste destas: ")
        for bandolin in matching_instrument_joseph:
            print(bandolin)
    else:
        print("Desculpe Joseph, não temos nada para você")


if __name__ == "__main__":
    main()

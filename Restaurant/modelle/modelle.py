from functools import reduce
class Id:
    # cnt = {}
    def __init__(self, id):
        # self.class_name = class_name
        self.id = id

    #     if type(self) == Id:
    #         raise NotImplementedError("Oops! This Class can't be instantiated")
    #
    # def generate_id(self):
    #     if self.class_name not in self.cnt:
    #         self.cnt[self.class_name] = 0
    #     self.cnt[self.class_name] += 1
    #     self.id = self.cnt[self.class_name]
    #     return self.id

class Gericht(Id):
    def __init__(self, id, name, portionsgrosse, preis):
        Id.__init__(self, id)
        self.name = name
        self.portionsgrosse = portionsgrosse
        self.preis = preis

        if type(self) == Gericht:
            raise NotImplementedError("Oops! This Class can't be instantiated")

    def __add__(self, other):
        return self.preis + other.preis

    def __str__(self):
        return f'Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}'

class GekochterGericht(Gericht):
    def __init__(self, id, name, portionsgrosse, preis, zubereitungszeit):
        Gericht.__init__(self, id, name, portionsgrosse, preis)
        self.zubereitungszeit = zubereitungszeit

    def __str__(self):
        return f'Id: {self.id}, Gericht: {self.name}, Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}, Zubereitungszeit: {self.zubereitungszeit}'

    def __add__(self, other):
        return self.preis + other.preis

    __repr__ = __str__
class Getrank(Gericht):
    def __init__(self, id, name, alkoholgehalt, portionsgrosse, preis):
        Gericht.__init__(self, id, name, portionsgrosse, preis)
        self.alkoholgehalt = alkoholgehalt

    def __str__(self):
        return f'Id: {self.id}, Getrank: {self.name}, Alkoholgehalt: {self.alkoholgehalt}, Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}'

    def __add__(self, other):
        return self.preis + other.preis
    __repr__ = __str__

class Kunde(Id):
    def __init__(self, name, address, id):
        Id.__init__(self, id)
        self.name = name
        self.address = address

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Address: {self.address}'

    __repr__ = __str__

    def __eq__(self, other):
        return self.id == other.id or self.name == other.name and self.address == other.address

    def __lt__(self, other):
        return self.id < other.id

class Bestellung():
    def __init__(self, kunden_id, liste_ids_gerichte, liste_ids_getranke, gesamtkosten):
        self.kunden_id = kunden_id
        self.liste_ids_gerichte = liste_ids_gerichte
        self.liste_ids_getranke = liste_ids_getranke
        self.gesamtkosten = gesamtkosten

    def total_cost(self, gerichte, getranke):
        def reducer(acc, item_id):
            return acc + gerichte[item_id] if item_id in gerichte else acc + getranke[item_id].preis
        result = reduce(reducer, self.liste_ids_gerichte + self.liste_ids_getranke, 0)

    def __str__(self):
        return f'Kunden Id: {self.kunden_id}, Gerichte: {self.liste_ids_gerichte}, Getranke: {self.liste_ids_getranke}, Gesamtkosten: {self.gesamtkosten}'

    __repr__ = __str__
    #liste = self.load
    #preturi = list(filter(lambda x: x.id in self.liste_ids_gerichte, liste))
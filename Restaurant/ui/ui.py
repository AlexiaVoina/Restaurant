from modelle.modelle import Kunde, GekochterGericht, Getrank, Bestellung
from controller.controller import Controller
class Ui():
    def __init__(self, controller: Controller):
        self.__controller = controller

    def menu(self):
        print("""
        0. Pa Pa
        1. Adauga un client
        2. Sterge un client
        3. Modifica un client
        4. Cauta un client
        5. Comanda noua
        6. Factura
        7. Meniu
        8. Lista clienti
        """)


    def run(self):
        # repo = Ui(Controller(CookedDishRepo("cooked_dish.pickle"), DrinkRepo("drink.pickle"),CustomerRepo("customer.pickle"), OrderRepo("order.pickle")))
        while True:
            opt = int(input('Optiunea dvs: '))
            if opt == 0:
                break
            if opt == 1:
                id = int(input("Id: "))
                name = input("Name: ")
                address = input("Address: ")
                new_obj = Kunde(name, address, id)
                self.__controller.add(new_obj)
            if opt == 2:
                id = int(input("Id client pentru stergere: "))
                new_obj = Kunde("name", "address", "id")
                self.__controller.delete_by_id(id, new_obj)
            if opt == 3:
                id = int(input("Id client pentru modificare: "))
                name = input("Name: ")
                address = input("Address: ")
                new_obj = Kunde(name, address, id)
                obj = Kunde("name", "address", "id")
                self.__controller.update_by_id(id, obj, new_obj)
            if opt == 4:
                id = int(input("Id client cautat: "))
                new_obj = Kunde("name", "address", "id")
                self.__controller.get_by_id(id, new_obj)
            if opt == 5:
                id = int(input("Id client care face comanda: "))
                gerichte = input("Id Mancare: ")
                gerichte.split(" ")
                getranke = input("Id Bauturi: ")
                getranke.split(" ")
                new_obj = Bestellung(id, gerichte, getranke, 0)
                self.__controller.add(new_obj)
                print("comanda facuta cu succes")
                new_obj2 = Bestellung(1, 1, 1, 0)
                self.__controller.load(new_obj2)
                print(self.__controller.get_all(new_obj2))

            if opt == 6:
                print("ALLES IST GRATIS!!! IA CAT POTI!!!")

            if opt == 7:
                print("""
                1. Vezi meniul
                2. Adauga
                """)
                opt2 = int(input("Optiune: "))
                if opt2 == 1:
                    new_obj = GekochterGericht("id", "name", "portionsgrosse", "preis", "zubereitungszeit")
                    self.__controller.load(new_obj)
                    print(self.__controller.get_all(new_obj))
                    new_obj2 = Getrank("id", "name", "1", "1", "1")
                    self.__controller.load(new_obj2)
                    print(self.__controller.get_all(new_obj2))
                if opt2 == 2:
                    print("""
                    1. Mancare
                    2. Bautura
                    """)
                    opt3 = int(input("Optiune: "))
                    if opt3 == 1:
                        id = input("Id: ")
                        name = input("Name: ")
                        portionsgrosse = input("Portionsgrosse:")
                        preis = int(input("Preis: "))
                        zubereitungszeit = input("Zubereitungszeit: ")
                        new_obj = GekochterGericht(id, name, portionsgrosse, preis, zubereitungszeit)
                        self.__controller.load(new_obj)
                        self.__controller.add(new_obj)
                    if opt3 == 2:
                        id = input("Id: ")
                        name = input("Name: ")
                        alkoholgehalt = input("Alkoholgehalt: ")
                        portionsgrosse = input("Portionsgrosse:")
                        preis = int(input("Preis: "))
                        new_obj = Getrank(id, name, alkoholgehalt, portionsgrosse, preis)
                        self.__controller.load(new_obj)
                        self.__controller.add(new_obj)

            if opt == 8:
                new_obj = Kunde("name", "address", "id")
                self.__controller.load(new_obj)
                print(self.__controller.get_all(new_obj))



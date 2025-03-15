from repository.repository import CustomerRepo, CookedDishRepo, DrinkRepo, OrderRepo
from modelle.modelle import GekochterGericht, Kunde, Getrank, Bestellung
# import pickle
class Controller:
    def __init__(self, cooked_dish_repo: CookedDishRepo, drink_repo: DrinkRepo,
                 customer_repo: CustomerRepo, order_repo: OrderRepo):
        self.__cooked_dish_repo = cooked_dish_repo
        self.__drink_repo = drink_repo
        self.__customer_repo = customer_repo
        self.__order_repo = order_repo

    def add(self, obj):
        if type(obj) == Kunde:
            self.__customer_repo.add(obj)
        elif type(obj) == GekochterGericht:
            self.__cooked_dish_repo.add(obj)
        elif type(obj) == Getrank:
            self.__drink_repo.add(obj)
        elif type(obj) == Bestellung:
            self.__order_repo.add(obj)

    # def save(self, obj):
    #     if type(obj) == Kunde:
    #         with open("kunde.pickle", "ab") as file:
    #             pickle.dump(self.get_all(), file)
    #     elif type(obj) == GekochterGericht:
    #         with open("cookeddish.pickle", "ab") as file:
    #             pickle.dump(self.get_all(), file)
    #     elif type(obj) == Getrank:
    #         with open("drinks.pickle", "ab") as file:
    #             pickle.dump(self.get_all(), file)
    #     elif type(obj) == Bestellung:
    #         with open("order.pickle", "ab") as file:
    #             pickle.dump(self.get_all(), file)
    def get_all(self, obj):
        list_of_obj = []
        if type(obj) == Kunde:
            list_of_obj = self.__customer_repo.get_all()
        elif type(obj) == GekochterGericht:
            list_of_obj = self.__cooked_dish_repo.get_all()
        elif type(obj) == Getrank:
            list_of_obj = self.__drink_repo.get_all()
        elif type(obj) == Bestellung:
            list_of_obj = self.__order_repo.get_all()
        return list_of_obj

    def get_by_id(self, id, obj):
        if type(obj) == Kunde:
            obj = self.__customer_repo.get_by_id(id)
        elif type(obj) == GekochterGericht:
            obj = self.__cooked_dish_repo.get_by_id(id)
        elif type(obj) == Getrank:
            obj = self.__drink_repo.get_by_id(id)
        elif type(obj) == Bestellung:
            obj = self.__order_repo.get_by_id(id)
        print(obj)

    def delete_by_id(self, id, obj):
        if type(obj) == Kunde:
            self.__customer_repo.delete_by_id(id)
        elif type(obj) == GekochterGericht:
            self.__cooked_dish_repo.delete_by_id(id)
        elif type(obj) == Getrank:
            self.__drink_repo.delete_by_id(id)
        elif type(obj) == Bestellung:
            self.__order_repo.delete_by_id(id)

    def update_by_id(self, id, obj, new_obj):
        if type(obj) == Kunde:
            self.__customer_repo.update_by_id(id, new_obj)
        elif type(obj) == GekochterGericht:
            self.__cooked_dish_repo.update_by_id(id, new_obj)
        elif type(obj) == Getrank:
            self.__drink_repo.update_by_id(id, new_obj)
        elif type(obj) == Bestellung:
            self.__order_repo.update_by_id(id, new_obj)

    def load(self, obj):
        if type(obj) == Kunde:
            self.__customer_repo.load()
        elif type(obj) == GekochterGericht:
            self.__cooked_dish_repo.load()
        elif type(obj) == Getrank:
            self.__drink_repo.load()
        elif type(obj) == Bestellung:
            self.__order_repo.load()

    # def write_to_file(self, obj):
    #     if type(obj) == Kunde:
    #         self.__customer_repo.write_to_file()
    #     elif type(obj) == GekochterGericht:
    #         self.__cooked_dish_repo.write_to_file()
    #     elif type(obj) == Getrank:
    #         self.__drink_repo.write_to_file()
    #     elif type(obj) == Bestellung:
    #         self.__order_repo.write_to_file()

    def find_by_name(self, name):
        return self.__customer_repo.find_by_name(name)

    def find_by_address(self, address):
        return self.__customer_repo.find_by_name(address)


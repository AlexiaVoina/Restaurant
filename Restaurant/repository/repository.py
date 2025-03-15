# from modelle.modelle import *
import pickle
class DataRepo:
    def __init__(self, file):
        self._data = []
        self._file = file

        if type(self) == DataRepo:
            raise NotImplementedError("Oops! This Class can't be instantiated")

        if type(self._file) == CookedDishRepo:
            self._file = "cooked_dish.pickle"
        if type(self._file) == DrinkRepo:
            self._file = "drink.pickle"
        if type(self._file) == CustomerRepo:
            self._file = "customer.pickle"
        if type(self._file) == OrderRepo:
            self._file = "order.pickle"

    def add(self, entity):
        self._data.append(entity)
        self.save()

    def save(self):
        with open(self._file, "wb") as file:
            pickle.dump(self._data, file)

    def get_all(self):
        return self._data

    def get_by_id(self, id):
        self.load()
        # print(self._data)
        return list(filter(lambda obj: str(obj.id) == str(id), self._data))

    def delete_by_id(self, id):
        self.load()
        self._data = list(filter(lambda obj: obj.id != id, self._data))
        self.save()

    def update_by_id(self, id, new_obj):
        self.load()
        self._data = [new_obj if obj.id == id else obj for obj in self._data]
        self.save()

    def convert_to_string(self):
        return list(map(lambda entity: pickle.dumps(entity), self._data))

    def convert_from_string(self):
        pass

    def load(self):
        with open(self._file, "rb") as file:
            self._data = (pickle.load(file))

    # def write_to_file(self):
    #     with open(self._file, "wb") as file:
    #         pickle.dump(self.get_all(), file)

class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def find_by_name(self, name):
        return list(filter(lambda customer: name.lower() in customer.name.lower(), self.get_all()))

    def find_by_address(self, address):
        return list(filter(lambda customer: address.lower() in customer.address.lower(), self.get_all()))



class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
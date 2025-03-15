from ui.ui import Ui
from controller.controller import Controller
from repository.repository import CookedDishRepo, DrinkRepo, CustomerRepo, OrderRepo

def main():
    # f = open("customer.pickle", "rb")
    # list = pickle.load(f)
    # print(list[0])
    my_ui = Ui((Controller(CookedDishRepo("cooked_dish.pickle"), DrinkRepo("drink.pickle"), CustomerRepo("customer.pickle"), OrderRepo("order.pickle"))))
    my_ui.menu()
    my_ui.run()

main()
from assets import *


class Player:

    def __init__(self, main):
        self.main = main
        self.funds = 10000

        self.income_sound = load_sound("money_collect.wav")

    def draw_funds(self, amount):
        if self.funds - amount < 0:
            return False
        else:
            self.funds = self.funds - amount
            return True


    def get_funds(self):
        return self.funds


    def on_day(self, month, day):
        if day == 30:
            self.draw_rent()

    def draw_rent(self):
        building = self.main.world.building
        income = building.get_total_rent()

        has_helipad = building.has_helipad()
        if has_helipad:
            income = int(income + income * 0.1)

        self.funds += income

        status_bar = self.main.interface.get_status_bar()
        status_bar.show_message("Income: $" + str(income))

        self.income_sound.play()


import pygame.font

from vectors import vec2
import assets
import gui


class Interface:

    def __init__(self, main):
        self.main = main

        self.upgrade_cost_txt = None
        self.upgrade_button_controls = []
        self.helipad_button_controls = []
        self.contentment_icon = None
        self.contentment_happy_icon = assets.load_image("happy.png")
        self.contentment_indifferent_icon = assets.load_image("indifferent.png")
        self.contentment_unhappy_icon = assets.load_image("unhappy.png")
        self.contentment_very_unhappy_icon = assets.load_image("very_unhappy.png")

        self.date_month_txt = None
        self.date_day_txt = None
        self.funds_gauge_txt = None
        self.rent_amount_text = None
        self.rent_slider = None
        self.status_bar = None

    def display(self):
        self.display_upgrade_button()
        self.display_helipad_button()
        self.display_funds_gauge()
        self.display_contentment()
        self.display_date_gauge()
        self.display_rent_slider()
        self.create_status_bar()

    def display_upgrade_button(self):
        thegui = self.main.gui
        world = self.main.world

        w, h = thegui.get_size()

        font = assets.load_font("Teko-Bold.ttf", 24)
        upgrade_text = gui.Text("Upgrade", font)
        upgrade_text.set_position(vec2(10, h - 120))
        thegui.add_widget(upgrade_text)

        self.upgrade_button_controls.append(upgrade_text)

        upgrade_button = gui.Button(assets.load_image("upgrade_button.png"), self.upgrade)
        upgrade_button.set_position(vec2(0, h - 130))
        thegui.add_widget(upgrade_button)

        self.upgrade_button_controls.append(upgrade_button)

        font2 = assets.load_font("Teko-Bold.ttf", 16)
        upgrade_cost_str = "$" + str(world.building.get_upgrade_cost())
        upgrade_cost_txt = gui.Text(upgrade_cost_str, font2, (255, 255, 255))
        upgrade_cost_txt.set_position(vec2(20, h - 95))
        self.upgrade_cost_txt = upgrade_cost_txt
        thegui.add_widget(upgrade_cost_txt)

        self.upgrade_button_controls.append(upgrade_cost_txt)

        upgrade_cost_bg = gui.ImageWidget(assets.load_image("upgrade_cost_bg.png"))
        upgrade_cost_bg.set_position(vec2(0, h - 100))
        thegui.add_widget(upgrade_cost_bg)

        self.upgrade_button_controls.append(upgrade_cost_bg)

    def display_helipad_button(self):
        thegui = self.main.gui
        world = self.main.world

        w, h = thegui.get_size()

        font = assets.load_font("Teko-Bold.ttf", 24)
        helipad_text = gui.Text("Helipad", font)
        helipad_text.set_position(vec2(10, h - 180))
        thegui.add_widget(helipad_text)

        self.helipad_button_controls.append(helipad_text)

        helipad_button = gui.Button(assets.load_image("helipad_button.png"), self.build_helipad)
        helipad_button.set_position(vec2(0, h - 190))
        thegui.add_widget(helipad_button)

        self.helipad_button_controls.append(helipad_button)

        font2 = assets.load_font("Teko-Bold.ttf", 16)
        helipad_cost_str = "$" + str(5000)
        helipad_cost_txt = gui.Text(helipad_cost_str, font2, (255, 255, 255))
        helipad_cost_txt.set_position(vec2(20, h - 155))
        thegui.add_widget(helipad_cost_txt)

        self.helipad_button_controls.append(helipad_cost_txt)

        helipad_cost_bg = gui.ImageWidget(assets.load_image("upgrade_cost_bg.png"))
        helipad_cost_bg.set_position(vec2(0, h - 160))

        self.helipad_button_controls.append(helipad_cost_bg)

        thegui.add_widget(helipad_cost_bg)

    def display_funds_gauge(self):
        '''
        Display the funds gauge, that is in the lower right corner
        :return:
        '''
        thegui = self.main.gui
        player = self.main.player

        w, h = thegui.get_size()

        font = assets.load_font("Teko-Bold.ttf", 16)
        funds = player.get_funds()
        self.funds_gauge_txt = gui.Text("Funds: $" + str(funds), font, (255, 255, 255))
        self.funds_gauge_txt.set_position(vec2(600 - 110, h - 22))
        thegui.add_widget(self.funds_gauge_txt)

        funds_gauge_bg = gui.ImageWidget(assets.load_image("funds_gauge_bg.png"))
        funds_gauge_bg.set_position(vec2(600 - 173, h - 31))
        thegui.add_widget(funds_gauge_bg)

    def display_contentment(self):
        thegui = self.main.gui

        w, h = thegui.get_size()

        font = assets.load_font("Teko-Regular.ttf", 16)
        contentment_txt = gui.Text("Contentment", font)
        contentment_txt.set_position(vec2(600 - 74, h - 114))
        thegui.add_widget(contentment_txt)

        self.contentment_icon = gui.ImageWidget(assets.load_image("happy.png"))
        self.contentment_icon.set_position(vec2(600 - 54, h - 96))
        thegui.add_widget(self.contentment_icon)

        contentment_bg = gui.ImageWidget(assets.load_image("contentment_bg.png"))
        contentment_bg.set_position(vec2(600 - 146, h - 116))
        thegui.add_widget(contentment_bg)

    def display_date_gauge(self):
        '''
        Display the date gauge, that is in the lower right corner, above the funds gauge
        '''
        thegui = self.main.gui

        w, h = thegui.get_size()

        date_font = assets.load_font("Teko-Regular.ttf", 14)

        self.date_month_txt = gui.Text("Month: 1", date_font)
        self.date_month_txt.set_position(vec2(600 - 50, h - 62))
        thegui.add_widget(self.date_month_txt)

        self.date_day_txt = gui.Text("Day: 1", date_font)
        self.date_day_txt.set_position(vec2(600 - 45, h - 48))
        thegui.add_widget(self.date_day_txt)

        date_bg_img = assets.load_image("date_bg.png")
        date_bg_widget = gui.ImageWidget(date_bg_img)
        date_bg_widget.set_position(vec2(600 - 146, h - 65))
        thegui.add_widget(date_bg_widget)

    def display_rent_slider(self):
        thegui = self.main.gui

        w, h = thegui.get_size()

        font = assets.load_font("Teko-Regular.ttf", 16)
        self.rent_amount_text = gui.Text("Rent: $1000", font)
        self.rent_amount_text.set_position(vec2(10, h - 56))
        thegui.add_widget(self.rent_amount_text)

        rail_img = assets.load_image("slider_rail.png")
        knob_img = assets.load_image("slider_knob.png")

        self.rent_slider = gui.Slider(rail_img, knob_img, self.rent_changed)
        self.rent_slider.set_position(vec2(70, h - 60))
        thegui.add_widget(self.rent_slider)

        rent_slider_bg = gui.ImageWidget(assets.load_image("rent_slider_bg.png"))
        rent_slider_bg.set_position(vec2(0, h - 64))
        thegui.add_widget(rent_slider_bg)


    def create_status_bar(self):
        '''
        Create the status bar.
        '''
        thegui = self.main.gui
        self.status_bar = StatusBar(thegui)


    def upgrade(self):
        '''
        Upgrade the main building
        '''
        world = self.main.world
        player = self.main.player

        cost = world.building.get_upgrade_cost()
        if world.building.can_upgrade():
            if player.draw_funds(cost):
                world.building.upgrade()
                if world.building.has_helipad():
                    world.building.destroy_helipad()
                    self.show_helipad_button_controls()

                self.update_funds_gauge()

                cost = world.building.get_upgrade_cost()
                self.upgrade_cost_txt.set_text("$" + str(cost))
            else:
                self.status_bar.show_message("Insufficient funds")

        if not world.building.can_upgrade():
            self.hide_upgrade_button_controls()

    def build_helipad(self):
        buiding = self.main.world.building
        player = self.main.player
        cost = buiding.get_helipad_cost()

        if player.draw_funds(cost) and not buiding.has_helipad():
            buiding.make_helipad()
            self.hide_helipad_button_controls()
        elif buiding.has_helipad():
            self.status_bar.show_message("Already built")
        else:
            self.status_bar.show_message("Insufficient funds")

    def rent_changed(self, percentage):
        building = self.main.world.building

        rent = int(percentage / 100 * 2000)
        self.rent_amount_text.set_text("Rent: $" + str(rent))

        building.set_rent(rent)

    def hide_upgrade_button_controls(self):
        thegui = self.main.gui

        for widget in self.upgrade_button_controls:
            thegui.remove_widget(widget)

    def hide_helipad_button_controls(self):
        thegui = self.main.gui

        for widget in self.helipad_button_controls:
            thegui.remove_widget(widget)

    def show_helipad_button_controls(self):
        thegui = self.main.gui

        for widget in self.helipad_button_controls:
            thegui.add_widget(widget)

    def update(self, clock):
        self.update_funds_gauge()
        self.status_bar.update(clock)
        self.update_contentment()
        self.update_date_gauge(clock)

    def update_funds_gauge(self):
        player = self.main.player
        funds = player.get_funds()
        self.funds_gauge_txt.set_text("Funds: $" + str(funds))

    def update_date_gauge(self, clock):
        world = self.main.world
        month = world.get_month()
        day = world.get_day()

        self.date_month_txt.set_text("Month: " + str(month))
        self.date_day_txt.set_text("Day: " + str(day))

    def update_contentment(self):
        building = self.main.world.building
        contentment = building.get_contentment()
        if contentment >= 0 and contentment < 20:
            self.contentment_icon.set_image(self.contentment_very_unhappy_icon)
        elif contentment >= 20 and contentment < 40:
            self.contentment_icon.set_image(self.contentment_unhappy_icon)
        elif contentment >=40 and contentment < 70:
            self.contentment_icon.set_image(self.contentment_indifferent_icon)
        elif contentment >= 70 and contentment <= 100:
            self.contentment_icon.set_image(self.contentment_happy_icon)

    def get_status_bar(self):
        return self.status_bar


class StatusBar:

    def __init__(self, thegui):
        self.gui = thegui

        w, h = thegui.get_size()

        background_img = assets.load_image("status_bar_bg.png")
        self.background = gui.ImageWidget(background_img)
        self.background.set_position(vec2(0, h - 20))

        font = assets.load_font("Teko-Regular.ttf", 18)
        self.text = gui.Text("Status bar", font)
        self.text.set_position(vec2(10, h - 18))

        self.message = None
        self.time = 0
        self.timeout = 0

    def display(self):
        self.gui.add_widget(self.text)
        self.gui.add_widget(self.background)

    def hide(self):
        self.gui.remove_widget(self.text)
        self.gui.remove_widget(self.background)

    def update(self, clock):
        if self.message is not None:
            if self.time > self.timeout:
                self.message = None
                self.hide()
            self.time += clock.get_time()



    def show_message(self, message):
        if self.message is None:
            self.message = message
            self.time = 0
            self.timeout = len(message) * 100
            self.text.set_text(message)
            self.display()

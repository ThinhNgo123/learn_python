# import random

# class Room:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)
# class Item:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

# class Clue(Item):
#     def __init__(self, name, description, location):
#         super().__init__(name, description)
#         self.location = location

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.current_room = None
#         self.inventory = []

#     def move(self, direction):
#         if direction in self.current_room.exits:
#             self.current_room = self.current_room.exits[direction]
#             print(self.current_room.description)
#         else:
#             print("Không thể di chuyển về hướng đó.")

#     def pick_up_item(self, item_name):
#         item = next((i for i in self.current_room.items if i.name == item_name), None)
#         if item:
#             self.current_room.items.remove(item)
#             self.inventory.append(item)
#             print("Bạn đã nhặt được một món đồ mới:", item.name)
#         else:
#             print("Không tìm thấy món đồ này trong phòng.")

#     def drop_item(self, item_name):
#         item = next((i for i in self.inventory if i.name == item_name), None)
#         if item:
#             self.inventory.remove(item)
#             self.current_room.items.append(item)
#             print("Bạn đã để lại một món đồ trong phòng:", item.name)
#         else:
#             print("Bạn không có món đồ này trong túi.")

#     def search_room(self):
#         clues = [i for i in self.current_room.items if isinstance(i, Clue)]
#         if clues:
#             print("Bạn tìm thấy một manh mối mới trong phòng.")
#             for clue in clues:
#                 print(clue.description)
#         else:
#             print("Không tìm thấy manh mối nào trong phòng này.")

# class PuzzleGame:
#     def __init__(self):
#         self.rooms = {}
#         self.current_room = None
#         self.player = None
#         self.clues = []
#         self.game_over = False

#     def create_rooms(self):
#         # Tạo các phòng và điểm nối giữa chúng
#         living_room = Room("Phòng khách", "Bạn đang đứng trong phòng khách.")
#         kitchen = Room("Phòng bếp", "Bạn đang đứng trong phòng bếp.")
#         bedroom = Room("Phòng ngủ", "Bạn đang đứng trong phòng ngủ.")
#         bathroom = Room("Phòng tắm", "Bạn đang đứng trong phòng tắm.")

#         living_room.exits = {"về phía bếp": kitchen}
#         kitchen.exits = {"về phía phòng khách": living_room, "về phía phòng ngủ": bedroom}
#         bedroom.exits = {"về phía phòng bếp": kitchen, "về phía phòng tắm": bathroom}
#         bathroom.exits = {"về phía phòng ngủ": bedroom}

#         self.rooms["living_room"] = living_room
#         self.rooms["kitchen"] = kitchen
#         self.rooms["bedroom"] = bedroom
#         self.rooms["bathroom"] = bathroom

#         # Thêm các món đồ và manh mối vào các phòng
#         living_room.add_item(Item("Đèn trần", "Một chiếc đèn trần rất cổ điển."))
#         kitchen.add_item(Item("Dao bếp", "Một cái dao bếp sắc nhọn."))
#         bedroom.add_item(Item("Chăn", "Một cái chăn ấm áp."))
#         bathroom.add_item(Item("Xà phòng", "Một thanh xà phòng thơm ngon."))

#         bedroom.add_item(Clue("Manh mối 1", "Bạn nhận thấy một chiếc khuy áo bị rớt trên sàn.", (1, 2)))
#         kitchen.add_item(Clue("Manh mối 2", "Bạn tìm thấy một tấm giấy gấp lại trong ngăn kéo.", (0, 3)))

#     def create_player(self):
# 	    # Tạo người chơi và đặt vị trí ban đầu của họ trong phòng khách
# 	    name = input("Nhập tên của bạn: ")
# 	    self.player = Player(name)
# 	    self.current_room = self.rooms["living_room"]
# 	    self.player.current_room = self.current_room
# 	    print("Chào mừng", name, "đến với trò chơi tìm manh mối trong căn phòng.")

#     def play(self):
# 	    self.create_rooms()
# 	    self.create_player()

# 	    # Vòng lặp chính của trò chơi
# 	    while not self.game_over:
# 	        command = input("Nhập lệnh của bạn: ")
# 	        if command == "di chuyển":
# 	            direction = input("Nhập hướng di chuyển của bạn: ")
# 	            self.player.move(direction)
# 	        elif command == "nhặt đồ":
# 	            item_name = input("Nhập tên món đồ bạn muốn nhặt: ")
# 	            self.player.pick_up_item(item_name)
# 	        elif command == "bỏ đồ":
# 	            item_name = input("Nhập tên món đồ bạn muốn bỏ: ")
# 	            self.player.drop_item(item_name)
# 	        elif command == "tìm kiếm":
# 	            self.player.search_room()
# 	        else:
# 	            print("Lệnh không hợp lệ.")

# 	        # Kiểm tra xem người chơi đã tìm thấy tất cả các manh mối chưa
# 	        if len(self.clues) == 2:
# 	            print("Chúc mừng bạn đã tìm thấy tất cả các manh mối! Bạn đã giải quyết được bí ẩn và hoàn thành trò chơi.")
# 	            self.game_over = True

# game = PuzzleGame()
# game.play()
# -------------------------------------------

# import pygame

# class Room:
#     def __init__(self, name, description, image):
#         self.name = name
#         self.description = description
#         self.image = image

# class Item:
#     def __init__(self, name, description, image):
#         self.name = name
#         self.description = description
#         self.image = image

# class PuzzleGame:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption("Trò chơi tìm manh mối trong căn phòng")

#         self.rooms = {
#             "living_room": Room("Phòng khách", "Một căn phòng rộng lớn với một chiếc ghế sofa và một chiếc bàn trà.", "living_room.jpg"),
#             "bedroom": Room("Phòng ngủ", "Một căn phòng với một chiếc giường và một tủ quần áo.", "bedroom.jpg"),
#             "kitchen": Room("Phòng bếp", "Một căn phòng với một bếp và một tủ lạnh.", "kitchen.jpg")
#         }

#         self.items = {
#             "key": Item("Chìa khóa", "Một chiếc chìa khóa bằng đồng.", "key.jpg"),
#             "note": Item("Tờ giấy", "Một tờ giấy với những dòng chữ viết tay.", "note.jpg")
#         }

#         self.clues = []
#         self.game_over = False

#     def create_rooms(self):
#         for room in self.rooms.values():
#             room.image = pygame.image.load(room.image).convert()

#     def create_player(self):
#         # Tạo người chơi và đặt vị trí ban đầu của họ trong phòng khách
#         name = input("Nhập tên của bạn: ")
#         self.player = Player(name)
#         self.current_room = self.rooms["living_room"]
#         self.player.current_room = self.current_room
#         print("Chào mừng", name, "đến với trò chơi tìm manh mối trong căn phòng.")

#     def draw_room(self):
#         room = self.current_room
#         self.screen.blit(room.image, (0, 0))

#         # Vẽ các đồ vật trong phòng
#         for item in self.current_room.items:
#             item_image = self.items[item].image
#             item_pos = (item.x, item.y)
#             self.screen.blit(item_image, item_pos)

#     def play(self):
#         self.create_rooms()
#         self.create_player()

#         # Vòng lặp chính của trò chơi
#         while not self.game_over:
#             # Vẽ hình ảnh của phòng và đồ vật
#             self.draw_room()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         self.player.move("lên")
#                     elif event.key == pygame.K_DOWN:
#                         self.player.move("xuống")
#                     elif event.key == pygame.K_LEFT:
#                         self.player.move("trái")
#                     elif event.key == pygame.K_RIGHT:
#                         self.player.move("phải")

#             # Kiểm tra xem người chơi đã tìm thấy tất cả các manh mối chưa
#             if len(self.clues) == 2:
#                 print("Chúc mừng bạn đã tìm thấy tất cả các manh mối! Bạn đã giải quyết được bí ẩn và hoàn thành trò chơi.")
#                 self.game_over = True

#             pygame.display.update()

#         pygame.quit()

# # Khởi chạy trò chơi
# game = PuzzleGame()
# game.play()
# #------------------------------------------------------------------------


# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.inventory = []

#     def move(self, direction):
#         # Di chuyển người chơi đến phòng mới nếu có thể
#         pass

#     def pick_up_item(self, item):
#         # Nhặt đồ vật lên và thêm vào túi xách của người chơi
#         self.inventory.append(item)
#         self.current_room.items.remove(item)

#     def use_item(self, item):
#         # Sử dụng đồ vật để giải quyết các câu đố hoặc mở khóa
#         pass

#     def show_inventory(self):
#         # Hiển thị các đồ vật trong túi xách của người chơi
#         pass
# #----------------------------------------------------------------


# class Item:
#     def __init__(self, name, description, image, clue=False):
#         self.name = name
#         self.description = description
#         self.image = image
#         self.clue = clue

# class PuzzleGame:
#     def __init__(self):
#         self.rooms = {
#             "living_room": Room("Phòng khách", "Một căn phòng rộng lớn với một chiếc ghế sofa và một chiếc bàn trà.", "living_room.jpg"),
#             "bedroom": Room("Phòng ngủ", "Một căn phòng với một chiếc giường và một tủ quần áo.", "bedroom.jpg"),
#             "kitchen": Room("Phòng bếp", "Một căn phòng với một bếp và một tủ lạnh.", "kitchen.jpg")
#         }

#         self.items = {
#             "key": Item("Chìa khóa", "Một chiếc chìa khóa bằng đồng.", "key.jpg"),
#             "note": Item("Tờ giấy", "Một tờ giấy với những dòng chữ viết tay.", "note.jpg", True)
#         }

#         self.clues = []

#     def create_items(self):
#         for item in self.items.values():
#             item.image = pygame.image.load(item.image).convert()

#     def create_clues(self):
#         for item in self.items.values():
#             if item.clue:
#                 self.clues.append(item)

#     def play(self):
#         self.create_items()
#         self.create_clues()
#         # ...
# #----------------------------------------------------------

# class PuzzleGame:
#     def __init__(self):
#         pygame.mixer.init()
#         self.pick_up_sound = pygame.mixer.Sound("pick_up.wav")
#         self.solve_sound = pygame.mixer.Sound("solve.wav")
#         # ...

#     def play(self):
#         # ...
#         while not self.game_over:
#             # ...
#             for item in self.current_room.items:
#                 item_image = self.items[item].image
#                 item_pos = (item.x, item.y)
#                 self.screen.blit(item_image, item_pos)

#                 # Kiểm tra xem người chơi có nhặt được đồ vật này không
#                 if self.player.collides_with(item):
#                     self.player.pick_up_item(item)
#                     self.pick_up_sound.play()

#             # Kiểm tra xem người chơi đã giải quyết được câu đố chưa
#             for clue in self.clues:
#                 if clue in self.player.inventory:
#                     self.solve_sound.play
# #----------------------------------------------------------

import pygame
from pygame.locals import *
from pygame.color import *
import pygame.network as pgn
class MultiplayerGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.server = pgn.Server()
        self.client = pgn.Client()
        self.players = {}

    def start_server(self):
        self.server.init()
        self.server.start()

    def connect_to_server(self, address):
        self.client.init()
        self.client.connect(address)

    def send_message(self, message):
        self.client.send(message)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_SPACE:
                    self.send_message("Hello world!")

    def update(self):
        self.players = self.server.get_clients()

    def draw(self):
        self.screen.fill(Color("white"))
        text = self.font.render("Number of players: {}".format(len(self.players)), True, Color("black"))
        self.screen.blit(text, (10, 10))
        pygame.display.update()

    def play(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

# Method Overriding: If the same method is defined in both base and derived classes, then the method of the derived class overrides the method of the base class.

# Video Game
class Character:
    
    def __init__(self, x, y, num_lives):
        self.x = x
        self.y = y
        self.num_lives = num_lives

    def show_info(self):
        print("Character Info")


class Player(Character):

    INITIAL_X = 0
    INITIAL_Y = 0
    INITIAL_NUM_LIVES = 10

    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.INITIAL_NUM_LIVES)
        self.score = score

    # Method Overriding
    def show_info(self):
        super().show_info()
        print("Player Info")


class Enemy(Character):

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        super().__init__(x, y, num_lives)
        self.is_poisonous = is_poisonous

    # Method Overriding
    def show_info(self):
        super().show_info()
        print("Enemy Info")


print("Player:")
player = Player()
print(player.x)
print(player.y)
print(player.num_lives)
print(player.score)
print(player.show_info())
print()

print("Easy Enemy:")
easy_enemy = Enemy(num_lives=1)
print(easy_enemy.x)
print(easy_enemy.y)
print(easy_enemy.num_lives)
print(easy_enemy.is_poisonous)
print(easy_enemy.show_info())
print()

print("Hard Enemy:")
hard_enemy = Enemy(num_lives=56, is_poisonous=True)
print(hard_enemy.x)
print(hard_enemy.y)
print(hard_enemy.num_lives)
print(hard_enemy.is_poisonous)
print(hard_enemy.show_info())
print()

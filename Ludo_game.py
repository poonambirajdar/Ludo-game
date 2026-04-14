class Player:
    def __init__(self,name):
        self.name = name
        self.position = 0

    def move(self,step):
        self.step = step
        if self.position + step <= 25:
            self.position += self.step
        else:
            print(self.name,"needs exact rolls/players to finish")

    def has_won(self):
        return self.position == 25

def get_dies_value():
    while True:
        try:
            value = int(input("Enter dies value 1 to 6 : "))
            if(1 <= value <= 6):
                return value
            else:
                print("Enter a number between 1 and 6.")
        except:
            print("Invalid input. Try again.")        
        
def display_position(player1, player2):
    print("\nBoard")
    for i in range(1, 26):
        if i == player1.position and i == player2.position:
            print("[Both]")
        elif i == player1.position: 
            print("[Player1]")
        elif i == player2.position:
            print("[Player2]")
        else:
            print("[ ]")
        if i % 5 == 0:
            print()    

def ludo_game():
    print("Welcome to Text-based Ludo Game...")

    name1 = input("Enter name for player 1:")
    name2 = input("Enter name for player 2:")

    Player1 = Player(name1)
    player2 = Player(name2)

    turn = 0
    while True:
        current_player = Player1 if turn % 2 == 0 else player2
        print(current_player.name , "'s turn")

        dies = get_dies_value()
        print(current_player.name, "rolled a", dies)

        current_player.move(dies)

        display_position(Player1, player2)

        if current_player.has_won():
            print(current_player.name, "has won the game!")
            break

        turn += 1

ludo_game()        




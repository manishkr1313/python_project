import random

def game_win(user, computer):
    if user == computer:
        return None
    
    #snake vs water
    if user == "s" and computer == "w":
         return True
    if user == "w" and computer  == "s":
        return False
    
    #water vs Gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer  == "w":
        return False
    
    #gun vs snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False




rand_no =random.randint(1,3)
# print(rand_no)
print("Computer turn: Snake(s), Water(w), Gun (g)")
if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer ="w"
else :
    computer ="g"
# print(computer)

user = input("Your turn: Snake (s), Water (w), Gun (g)").lower()

result = game_win(user , computer)# Returns True if you win, False for lose, none for draw
print(f"\nYou chose:{user}")
print(f"\nComputer chose:{computer}")

if result is None:
    print("Its a draw!")
if (result):
    print("You Win!")
else:
    print("You lose!")
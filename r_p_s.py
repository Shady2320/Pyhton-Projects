import random
def play():
	player1 = input("'st' for stone, 'p' for paper, 's' for scissors\n")
	player2 = random.choice(['st', 'p', 's'])
	if win(player1,player2):
		return "You won it!!"
	if player1 == player2:
		return 'Tie, try at least one more time.'
	
	return "You lose it!!"

def win(player1,player2):
	if(player1 == 'st' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'st'):
		return True


print("---------------------------Stone Paper Scissor---------------------------\n\n")
print("Choose any of the following three options:")
print(play())
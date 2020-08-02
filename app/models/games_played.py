from app.models.players import Player
from app.models.games import Game
import random

game_result=[]

def who_wins(player_1, player_2):
    if player_2.name=="computer":
        choice=random.randint(1,3)
        if choice==1:
            player_choice="rock"
        elif choice==2:
            player_choice="paper"
        else:
            player_choice="scissors"
    else:
        player_choice=player_2.choice
    
    if player_1.choice=="rock":
        if player_choice=="scissors":
            winner = player_1
        elif player_choice=="paper":
            winner = player_2
        else:
            winner=None
    elif player_1.choice=="paper":
        if player_choice=="rock":
            winner = player_1
        elif player_choice=="scissors":
            winner = player_2.name
        else:
            winner=None
    elif player_1.choice=="scissors":
        if player_choice=="paper":
            winner= player_1
        elif player_choice=="rock":
            winner=player_2
        else:
            winner = None
    
    if winner == None:      
        result= f"Neither player won as both players chose {player_1.choice}"
    elif winner.name==player_1.name :
        result = f"{player_1.name} wins by playing {player_1.choice} and {player_2.name} loses by playing {player_choice}"
    else:
        result= f"{player_2.name} wins by playing {player_choice} and {player_1.name} loses by playing {player_1.choice}"
    
    return result

def add_game(result):
    game_result.append(result)

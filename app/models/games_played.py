from app.models.players import Player

player_1 = Player("Joe","rock")
player_2 = Player("Fred","scissors")

def who_wins(player_1, player_2):
    if player_1.choice=="rock":
        if player_2.choice=="scissors":
            winner = player_1
        elif player_2.choice=="paper":
            winner=player_2
        else:
            winner=None
    elif player_1.choice=="paper":
        if player_2.choice=="rock":
            winner = player_1
        elif player_2.choice=="scissors":
            winner = player_2
        else:
            winner=None
    elif player_1.choice=="scissors":
        if player_2.choice=="paper":
            winner= player_1
        elif player_2.choice=="rock":
            winner=player_2
        else:
            winner = None
    
    if winner == None:      
        return "Neither player wins they both chose " + player_1.choice + "."
    elif winner.name==player_1.name :
        return winner.name + " wins as (s)he chose " + winner.choice + " and " + player_2.name + " lost and (s)he chose " + player_2.choice + "."
    else:
        return winner.name + " wins as (s)he chose " + winner.choice + " and " + player_1.name + " lost and (s)he chose " + player_1.choice + "."
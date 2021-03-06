from app import app
from flask import render_template, request, redirect
from app.models.players import Player
from app.models.games_played import who_wins, add_game
from app.models.games import Game


@app.route('/')
def index():
    return render_template("welcome.html", title = "Welcome")

@app.route('/results', methods=['POST'])
def take_turn():
    player_1_name = request.form['player_1']
    player_1_choice = request.form['choice_1']
    player_2_name= request.form['player_2']
    player_2_choice = request.form['choice_2']
    player_1 =Player(player_1_name,player_1_choice)
    player_2 = Player(player_2_name,player_2_choice)
    result = who_wins(player_1,player_2)
    add_game(result)
    return result
    

@app.route('/home')
def welcome():
    return render_template("index.html", title="Home")



from typing import Self
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def play_game():
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    return jsonify(choice)

if __name__ == '__main__':
    app.run(debug=True)

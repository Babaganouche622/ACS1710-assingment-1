import math
from random import randint

from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<favourite_dessert>')
def favourite_dessert(favourite_dessert):
    return f'How did you know I liked {favourite_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'Try {adjective} but {noun}.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    string = f'{number1} times {number2} is {int(number1) * int(number2)}.' if number1.isnumeric() and number2.isnumeric()  else "Invalid inputs. Please try again by entering 2 numbers!"
    return string

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    word = f"{word} "
    new_word = word * int(n) if n.isnumeric() else "Invalid input. Please try again by entering a word and a number!"

    return new_word

@app.route('/dicegame')
def dicegame():
   die = randint(1, 6)
   string = f"You rolled a {die}. You win!" if die == 6 else f"you rolled a {die}. You lose!"
   return string



if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, Flask, render_template, request, session, redirect, url_for
import time
import requests


game = Blueprint('game', __name__, template_folder='game_template')


@game.route('/typetest', methods=['GET', 'POST'])
def type_test():
    words = """When Mr. Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday."""
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_words = set(user_input.split())
        correct_words = set(words.split()).intersection(user_words)
        accuracy = len(correct_words) / len(words.split()) * 100 #divdes the length of the correct words by length of the whole sentence 
        end_time = time.time()
        total_time = end_time - float(request.form['start_time'])
        wpm = len(correct_words) / total_time * 60 
        return render_template('type.html', words=words, time_taken=round(total_time, 2), wpm=round(wpm, 2), accuracy=round(accuracy, 2))
    
    return render_template('type.html', words=words)


    
    
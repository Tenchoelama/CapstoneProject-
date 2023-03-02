from flask import Blueprint, Flask, render_template, request, redirect, url_for, session, flash
import requests
import random
from capstone_project.models import QuizResult
from flask_login import login_user,logout_user, login_required,current_user
from capstone_project.models import User, db
from datetime import date, datetime



quiz= Blueprint('quiz', __name__, template_folder='quiz_template')

#Calling the API and storing it in the variable data. 
response = requests.get('https://my-json-server.typicode.com/Tenchoelama/mockJSON/quiz')
data = response.json()




#defining quiz route and its methods
@quiz.route('/quiz', methods=['GET', 'POST'])
def quizy():
    #looping the thru the data and assigning the id to the 
    #difficulty list based on the category keys.
    easy = []
    moderate = []
    hard = []
    for i in range(len(data)):
        if data[i]['category'] == 'easy':
            easy.append(data[i]['id']-1)
        else:
            moderate.append(data[i]['id']-1)
            hard.append(data[i]['id']-1)
    
    #looping thru the list we had created above and storing 10 random question and 
    #options from the list to the corresponding question and option list. 
    
    category = request.form.get('category')
    if category == 'easy':
        difficulty = easy
    elif category in ('moderate', 'hard'):
        difficulty = moderate
        
        
    questions = []
    options = []
    answer = []
    
    
    for i in range(10):
        randoms = random.choice(difficulty)
        questions.append(data[randoms]['question'])
        options.append(data[randoms]['options'])
        answer.append(data[randoms]['answer'])
        difficulty.pop(difficulty.index(randoms))
        
    
    #return the template quiz_form and passes the args mentioned below so that the variables can be used in the form   
    return render_template('quiz_form.html', questions=questions, options=options ,easy=easy, answer=answer)

@quiz.route('/results', methods=['GET','Post'])    
def result():
    questions = [request.form.get(f"question{i+1}") for i in range(10)]
    selected_options = []
    correct_answers = []
    score = 0
    for i in range(10):
        
        selected_option = request.form[f'q{i+1}']
        correct_answer = request.form[f'answer{i+1}']
        
        selected_options.append(selected_option)
        correct_answers.append(correct_answer)
        if selected_option == correct_answer:
            score += 1
    
    return render_template('results.html', questions=questions, selected_options=selected_options, correct_answers=correct_answers, score=score)
            
          

@quiz.route('/category', methods=['GET','POST'])
def category():
     
    return render_template('category.html')


        
@quiz.route('/save_result', methods=['POST'])
@login_required
def save_result():
    
    score = int(request.form.get('score'))
    quiz_result = QuizResult(current_user.id,quiz_name='LOTR Quiz', score=score, attempts=1)
    db.session.add(quiz_result)
    db.session.commit()  
    
    # Retrieve all the quiz results for the current user
    quiz_results = QuizResult.query.filter_by(user_id=current_user.id).all()
    
    
    return render_template('profile.html', quiz_results=quiz_results,)



@quiz.route('/delete/<quiz_id>', methods =['POST'])
@login_required
def delete_quiz(quiz_id):
    
    quiz = QuizResult.query.filter_by(id=quiz_id, user_id=current_user.id).first()
    
    if quiz:
        db.session.delete(quiz)
        db.session.commit()
        flash('Quiz deleted successfully', 'success')
    else:
        flash('QUiz not found', 'error')
        
    return redirect(url_for('site.profile'))


        
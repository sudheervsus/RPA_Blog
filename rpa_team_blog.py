from flask import Flask, render_template, url_for, flash, logging, redirect, session, g, request
from data import Articles
import sqlite3
from forms import RegistrationForm, LoginForm
#import database


Articles=Articles()

app=Flask(__name__)
app.config.from_object('app_config.DevelopmentConfig')


@app.route('/')
def home():
    #flash("Thanks for Choosing")
    return render_template('index.html', title='Robotic Process Automation')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        flash("Thanks for registering")
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash("Login Successfully","success")
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()
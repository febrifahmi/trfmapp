from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    #return "Hello, World!"
    user = {'username': 'Febri'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
        	form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/about')
def about():
	user = {'username': 'Febri'}
	posts = [
		{
			'author': {'username': 'Admin'},
			'body': 'This is an about page!'
		}
	]
	return render_template('about.html', title='About', user=user, posts=posts)


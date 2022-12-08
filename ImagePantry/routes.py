from ImagePantry import (app, render_template, bcrypt, flash, redirect, url_for, abort)
from ImagePantry import (login_manager, login_user, logout_user, current_user, login_required)
from ImagePantry.forms import CreateAccountForm, LoginForm
from ImagePantry.models import User, users, photos, videos
import datetime, json

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/account/create', methods=['GET', 'POST'])
def account_create():
	form = CreateAccountForm()
	if form.validate_on_submit():
		try:
			hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user = {
			"name": form.name.data,
			"password": hashed_pw,
			"date_created": datetime.datetime.utcnow()
		}
			users.insert_one(user)
			print(f'Account created for {form.name.data}!', 'success')
			return redirect(url_for('login'))
		except Exception as e:
			print(e)
	print(form.errors)
	return render_template('account_create.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	if form.validate_on_submit():
		user_data = users.find_one({ "name": form.name.data })
		if user_data and bcrypt.check_password_hash(user_data['password'], form.password.data):		
			try:
				user = User(
					password = user_data['password'], 
					name     = user_data['name'],
					_id      = str(user_data['_id'])
					)
				login_user(user)
				return redirect(url_for('home'))

			except Exception as e:
				print(e)
				return redirect(url_for('login'))
	return render_template('login.html', form=form)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
	logout_user()
	print('Logout successful')
	return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
	return render_template('home.html')
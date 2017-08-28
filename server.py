from flask import Flask, session, request, redirect, render_template, Markup
import random
from datetime import datetime
time = datetime.now()
app = Flask(__name__)
app.secret_key = 'secretsarentfun'

@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold']=0
	try:
		session['mymessage']
	except:
		session['mymessage'] = []
	try:
		session['casino']
	except:
		session['casino'] = 0
	return render_template('index.html')

@app.route('/process_money', methods = ["POST"])
def process():

  	if request.form['action'] == 'farm_gold':
    		session['farm'] = random.randrange(10,21)
     		session['gold'] += session['farm']
    		log = "Earned " + str(session['farm']) + " from the farm! " + str(time)
    		session['mymessage'].insert(0,str(log))

  	elif request.form['action'] == 'cave_gold':
  		session['cave'] = random.randrange(5,11)
  		print session['cave']
  		session['gold'] += session['cave']
  		print session['gold']
  		log = "Earned " + str(session['cave']) + " from the cave! " + str(time)
  		session['mymessage'].insert(0,str(log))
  		print session['mymessage']

  	elif request.form['action'] == 'house_gold':
  		session['house'] = random.randrange(2,5)
  		session['gold'] += session['house']
  		log = "Earned " + str(session['house']) + " from the house! " + str(time)
  		session['mymessage'].insert(0,str(log))

  	elif request.form['action'] == 'casino_gold':
  		session['casino'] = random.randrange(-50,51)
  		session['gold'] += session['casino']

  	if session['casino'] < 0:
  			log = "Bad luck! Lost" + str(session['casino']) + " gold from the casino!" + str(time)
  			session['mymessage'].insert(0,str(log))
	else:
			log = "Earned " + str(session['casino']) + " from the casino!" + str(time)
  			session['mymessage'].insert(0,str(log))
	return redirect('/')

app.run(debug = True)

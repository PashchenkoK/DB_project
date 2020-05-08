from flask import Flask, render_template
import json
app = Flask(__name__)
with open("editions.json", "r") as edition:
	editions = json.load(edition)

with open("customers.json", "r") as customer:
	customers = json.load(customer)


@app.route('/api/<action>', methods = ['GET', 'POST'])
def apiget(action):
	if action == 'edition':
		return render_template('editions.html', edition = editions)
	elif action == 'customer': #замовник
		return render_template('customer.html', customer = customers)
	elif action == 'all':
		return render_template('all.html', edition = editions, customer = customers)
	else:
		return render_template('error.html')


if __name__ == '__main__':

	app.run(debug = True)
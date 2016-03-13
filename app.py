from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mocha')
def cakes():
	return 'mocha cokolade!'

@app.route(('/hello', defaults={'name': None})

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

if __name__ == '__main__':
	app.debug = True
    app.run(debug=True, host='0.0.0.0')



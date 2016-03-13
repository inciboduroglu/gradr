import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/note')
def note():
	return render_template('note.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['user_file']
        f.save('/var/www/uploads/uploaded_file.txt')

@app.route('/grade')
def cakes():
	return render_template('grade.html')

@app.route('/hello/')
def hello_empty():
	return 'isim yok :s'

@app.route('/team/<name>')
def hello(name):
	return render_template('team.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



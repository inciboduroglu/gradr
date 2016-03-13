import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/note')
def note():
	return render_template('note.html')

#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
    #if request.method == 'POST':
     #   f = request.files['user_file']
      #  f.save(os.path.join(app.config['UPLOAD_FOLDER']))
    #return 'OK'

@app.route('/grade')
def grade():
	return render_template('grade.html')

@app.route('/team/')
def team_empyt():
	return 'isim yok :s'

@app.route('/team/<name>')
def team(name):
	return render_template('team.html', name=name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload2', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['user_file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



from flask import Flask, render_template, request, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdwegiojwoeifja;wg'


@app.route('/')
def home():
    return '<h1>hello world!!!!</h1>'

@app.route('/user/<string:name>/')
def get_user(name):
    return '<h1>hello %s your age is %d</h1>' % (name,21)

@app.route('/songs')
def get_all_songs():
    songs = [
        'S.O.S',
        'Jesus Take the Wheel',
        'Help!'

    ]
    return render_template('songs.html')


if __name__ == '__main__':
    app.run()

@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
if request.method == 'GET':
first_name = request.args.get('first_name')
if first_name:
return render_template('form-demo.html', first_name=first_name)
else:
return render_template('form-demo.html', first_name=session.get('first_name'))
if request.method == 'POST':
session['first_name'] = request.form['first_name']
    # return render_template('form-demo.html', first_name=first_name)
return redirect(url_for('form_demo'))

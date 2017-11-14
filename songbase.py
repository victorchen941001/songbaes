from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dasdasda'

@app.route('/')
def home():
    #return '<h1>hello word!!!lala<h1>'
    return render_template('index.html')

# GET and POST
@app.route('/form-demo', methods=['GET','POST'])
def from_demo():
    if request.method == 'GET':

        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html',first_name=first_name)
        else:
            first_name = session.get('first_name')
            return render_template('form-demo.html',first_name=first_name)
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        #return render_template('form-demo.html',first_name=first_name)
        return redirect(url_for('form_demo'))
#Loop
@app.route('/songs')
def get_all_songs():
    songs =[
    'song1'
    'song2'
    'song3'
    ]
    return render_template('songs.html', songs=songs)




@app.route('/user/<string:name>')
def get_user(name):
    #return '<h1>hello %s your age is %d<h1>' % (name, 3)
    return render_template('user.html', user_name=name)





if __name__ =='__main__':
    app.run()

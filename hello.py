from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    food=['tomato','boatato','something else']
    fisrst_name='john'
    return render_template('index.html',food=food ,fisrst_name=fisrst_name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


#if __name__ == '__main__':
#    app.run(debug=True)
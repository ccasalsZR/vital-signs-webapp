from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():

    data = [
        ('01-01-2022',1597),
        ('01-02-2022',1496),
        ('01-03-2022',1908),
        ('01-04-2022',896),
        ('01-05-2022',755),
        ('01-06-2022',453),
        ('01-07-2022',1100),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    first_name = 'Carlos'
    stuff = 'This is <strong> Bold Text</strong>'
    return render_template('index.html',first_name=first_name
        ,stuff=stuff
        ,labels=labels
        ,values=values)

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name = name)


#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
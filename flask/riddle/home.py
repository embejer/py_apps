'''
imported Flask
'''
from flask import Flask, render_template

'''
imported a different module
riddle.py contains the function that requests riddles
'''
import riddle

'''
created a flask application
'''
app = Flask(__name__)


'''
these are the routes or endpoints that needs to be hit or access
'''
@app.route('/', defaults={'count': 0}, methods=['GET'])
@app.route('/<int:count>', methods=['GET'])
def show_riddles(count):

    '''
    we call on the get_riddles function from riddle.py
    get_riddles has (1) one argument.
    '''
    riddles = riddle.get_riddles(count)

    '''
    we then render the template called home.html
    all templates should be in `templates` folder a default for Flask
    '''
    return render_template('home.html', riddles=riddles)


'''
you can run the application using
- python home.py
or
- flask --app home run
'''
if __name__ == '__main__':
    app.run(debug=True)
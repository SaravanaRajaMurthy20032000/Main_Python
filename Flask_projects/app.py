from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def web():
    course = ['Python', 'HTML', 'CSS', 'Flask', 'GIT', 'Linux']
    return render_template('web.html',web_course=course)

@app.route('/about')
def about():
    return "<h2>Welcome to Erode,The Turmeric City of India</h2>"

@app.route('/users/<name>') #DYNAMIC ROUTING IN FLASK
def users(name):
    weapons = ['Necrosword', 'Arc Reactor', 'Shield']
    return render_template('users.html',user_name=name.title(),weapons_name=weapons)



if __name__ == '__main__':
    app.run(debug=True)
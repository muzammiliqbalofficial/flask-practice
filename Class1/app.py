from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask!"
@app.route('/contact')
def contact():
    return "Welcome to the contact page."
@app.route('/about')
def about():
    return "This is the about page."
@app.route('/profile')
def profile():
    return "This is the profile page."
@app.route('/profile/<name>')
def profile_name(name):
    return f"<h1>This is profile {name}</h1>."
if __name__ == '__main__':
    app.run(debug=True)
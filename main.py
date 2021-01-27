from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Im a paragraph</><br>'\
            '<img src="https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif" alt="kitten" width="300px">'



@app.route("/bye")
def bye():
    return "Good Bye mate!!"


# Variable Rules:
# 1. string
@app.route("/user/<string:user>")
def welcome_user(user):
    return f"Welcome, {user}!"


# 2. int
@app.route("/my_user_id/<my_user_id>")
def my_id(my_user_id):
    return f"My user ID is {my_user_id}"


# mix of both str and int in the same route:
@app.route("/username/<string:name>/<int:user_id>")
def greet(name, user_id):
    return f"Hello, {name}!  ID {user_id}."


# 3. float
@app.route("/my_height/<float:height>")
def my_height(height):
    return f"My height is {height}"


if __name__ == "__main__":
    app.run()

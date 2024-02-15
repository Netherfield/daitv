from flask import Flask
from controllers.all_controller import view_controller
from controllers.home_controller import home_controller

app = Flask(__name__)

app.register_blueprint(view_controller)
app.register_blueprint(home_controller)

if __name__ == "__main__":
    app.run(debug=True)

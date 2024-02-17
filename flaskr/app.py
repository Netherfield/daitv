from flask import Flask
from controllers.all_controller import view_controller
from controllers.home_controller import home_controller
from controllers.test_controller import test_controller

apx = Flask(__name__)

apx.register_blueprint(view_controller)
apx.register_blueprint(home_controller)
apx.register_blueprint(test_controller)

if __name__ == "__main__":
    apx.run(debug=True)

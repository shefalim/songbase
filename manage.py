from flask_script import Manager
from songbase.py import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()

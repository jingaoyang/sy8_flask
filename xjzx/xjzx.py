import app
from config import DevelopConfig
from flask_script import Manager
from models import db
from flask_migrate import Migrate,MigrateCommand


develop_app = app.create(DevelopConfig)
manager=Manager(develop_app)


Migrate(develop_app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
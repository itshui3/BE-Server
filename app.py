from src import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from src import db

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

ma = Marshmallow(app) # init marshmallow

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
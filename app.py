from src import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

ma = Marshmallow(app) # init marshmallow

# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'username')

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
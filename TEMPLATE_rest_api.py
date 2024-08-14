from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# Api = This wraps the Flask application to make it easy to 
# add resources and handle routing for a RESTful API.

# fields =  This is used to define how data will be serialized in the response. 
# It maps the data types to ensure the output is in the correct format.

# Resource = This is the base class for defining resources in Flask-RESTful. 
# A resource typically maps to a specific endpoint and handles HTTP methods like GET, POST, PUT, DELETE, etc.

# SQLAlchemy =  This imports the SQLAlchemy class from the flask_sqlalchemy extension. 
# SQLAlchemy is an ORM (Object-Relational Mapping) tool that allows you to interact with 
# the database using Python classes and objects rather than writing raw SQL queries.

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #This sets the configuration for the database URI. Here, SQLite is being used, and the database will be stored in a file named database.db.
db = SQLAlchemy(app) # ORM sql_alchemy object relational mapping use tot talk to the database
api = Api(app)

# This defines a database model named UserModel that 
# represents the structure of a users table in the database. 
# Each instance of UserModel corresponds to a row in this table.
# class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable = False)
    email = db.Column(db.String(80), unique=True, nullable = False)

    # This is a special method that returns a string representation 
    # of the UserModel instance, which is helpful for debugging.

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"


# This creates an instance of RequestParser, which 
# is used to parse and validate incoming request data.
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="name cannpt be blank")
user_args.add_argument('email', type=str, required=True, help="email cannpt be blank")

# This dictionary defines how the UserModel attributes 
# should be serialized when they are returned in the API 
# responses. Each attribute is mapped to its respective data type.
userFields = {
    'id': fields.Integer,
    'name':fields.String,
    'email':fields.String,
}

#  This class defines a resource that handles requests 
# related to multiple users (e.g., listing all users, creating a new user).
class Users(Resource):
    # This decorator automatically serializes the response 
    # data using the userFields dictionary, ensuring the 
    # response is in the correct format.
    @marshal_with(userFields) #serialize json
    def get(self):
        users = UserModel.query.all() #will be empty at first 
        return users , 200
    # the above This decorator automatically serializes the 
    # response data using the userFields dictionary, ensuring 
    # the response is in the correct format.
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201 #status CREATED 

# This class defines a resource that handles requests 
# related to a single user (e.g., getting, updating, 
# or deleting a specific user by ID).
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404)
        return user

    @marshal_with(userFields)
    # This method handles PATCH requests to update 
    # a user. It queries the user by id, and if found,
    # updates the user's name and email, commits the 
    # changes to the database, and returns the updated user.
    def patch(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404)
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404)
        db.session.delete(user)
        db.session.commit()
        return user


# api.add_resource: These lines add the Users and User 
# resources to the API. The Users resource is available 
# at /api/users/, and the User resource is available at /api/users/<int:id>, 
# where id is the user’s ID.
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')


@app.route('/')
def home():
    return '<h1> Flask rest api</h1>', 200

if __name__ == '__main__':
    # This ensures that the Flask application runs only 
    # if the script is executed directly (not when it is imported as a module).


    app.run(debug=True)
    # This starts the Flask development server with debugging enabled, 
    # which provides detailed error messages and auto-reloads the server on code changes.




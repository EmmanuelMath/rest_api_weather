from weather_rest_api import app, db

# this creates the database 

with app.app_context():
    db.create_all()

# BE-Server

To edit migrations on heroku, run the commands: 
python app.py db migrate
python app.py db upgrade

If you receive a message saying that something is not up to date, you may have to run: 
python app.py db stamp head

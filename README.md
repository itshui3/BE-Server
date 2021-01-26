<h2>Game of objectObject</h2>
<ins>Client Deploy:</ins><b>https://game-of-object-object.firebaseapp.com/</b>
<ins>API Deploy:</ins> <b><https://g-o-o-o.herokuapp.com/></b>

Game of objectObject is a Multi-User Dungeon game where users can create characters, move them around, run into/fight monsters, interact with merchants, pick-up/drop items. You can also chat with other users globally. 

<h2>What I learned</h2>

For this project our team chose to use the Flask API to support game mechanics on a react client app. I was able to support my team by learning a very basic level of Flask over the week-end and setting up boilerplate on which Robert and I built out mechanics and persistence. I was responsible for building things such as the random monster encounters, random flee messages, combat mechanics while Robert handled movement mechanics, item, and merchant interactions. 

This was the last build week project I worked on at Lambda School. Normally, for build weeks there's a lot of randomness in who we get teamed up with. For this project, we found a way to pre-form our group with overachievers in the same cohort. I learned what it's like to work with people who are both reliable and also challenge me by how hard they work and their strength of focus/ability to take an idea to completion. It was such a humbling/motivating experience then. Even now almost a year later, I look at some of the pieces built and realize how much I have to learn still. Especially with UI components that I'm not fully comfortable building as of yet. 

<h2>Technologies Used</h2>
flask = "*"<br/>
sqlalchemy = "*"<br/>
python-dotenv = "*"<br/>
flask-sqlalchemy = "*"<br/>
flask-marshmallow = "*"<br/>
marshmallow-sqlalchemy = "*"<br/>
gunicorn = "*"<br/>
psycopg2 = "*"<br/>
flask-migrate = "*"<br/>
flask-script = "*"<br/>
flask-login = "*"<br/>
pyjwt = "*"<br/>
aiohttp = "*"<br/>
flask-cors = "*"<br/>
pusher = "*"<br/>

<h2>Docs</h2>
To edit migrations on heroku, run the commands:
python app.py db migrate
python app.py db upgrade

If you receive a message saying that something is not up to date, you may have to run:
python app.py db stamp head

If other issues occur with migrations, try deleting database first and re-running commands.

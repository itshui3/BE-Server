import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir) 

# basedir = os.path.abspath(os.path.dirname(__file__))

# from app import Room

from ....models import Room

print(Room)
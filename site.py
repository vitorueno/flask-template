from app import app

#creating venv
'''
python -m venv env

*activate your venv and then:

python -m pip install -r requirements.txt
'''

#set up app
'''
linux:
export FLASK=site.py
flask run

windows:
set FLASK=site.py
flask run


extra:

debug mode:
set FLASK_ENV=development
'''

#generating BD tables from models  
'''
on terminal:

>>> from app import db
##create tables##
>>> db.create_all()
##delete tables##
db.drop_all()

##adding an occurrence##
>>> from app import db
>>> from app.models import User
>>> u1 = User(nome="joao")
>>> u1.set_senha("1234")
##add command##
>>> db.session.add(u1)
##delete command##
db.session.delete(u1)
##commit command##
>>> db.session.commit()
'''

#how to freeze your requirements (if needed)
'''
pip freeze [options]

example:
pip3 freeze requirements.txt
'''
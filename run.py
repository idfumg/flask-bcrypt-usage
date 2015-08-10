from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


pw_hash = bcrypt.generate_password_hash('hunter2')
print pw_hash
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True

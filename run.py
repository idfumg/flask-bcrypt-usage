from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# to generate bcrypt hash.
pw_hash = bcrypt.generate_password_hash('idfumg')

# to compare with an existing hash.
bcrypt.check_password_hash(pw_hash, 'idfumg')

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__, static_url_path='/static', instance_relative_config=False)
app.config['DEBUG'] = False


app.secret_key = 'development key'

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'nkrumahbot@gmail.com'
app.config["MAIL_PASSWORD"] = 'gvuunrxexqhgnwmi'

mail.init_app(app)

from FaridaAPP import routes

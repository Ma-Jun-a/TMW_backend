
from flask import Flask

from tester_web.user.api import api
from tester_web.user.project import project
from tester_web.user.scripts import scripts
from tester_web.user.test_results import results

app = Flask(__name__)

from tester_web.user.login import auth

app.register_blueprint(auth)

app.register_blueprint(scripts)

app.register_blueprint(project)
app.register_blueprint(results)
app.register_blueprint(api)
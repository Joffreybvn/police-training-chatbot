import os
from random import randint, choice
from werkzeug.middleware.proxy_fix import ProxyFix

from flask import Flask, request, jsonify, send_from_directory
from flask_restx import Api, Resource, abort, fields

from models.AddressModel import *
from models.PersonModel import *
from functions import *


# Init app
app = Flask(__name__)
api = Api(app, version='1.0', title='Story Variables API', description='API that return variables to make a story for the police')
basedir = os.path.abspath(os.path.dirname(__file__))

# Fix the Flask-RESTx https error
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@api.route('/story/<string:topic>', methods=['GET'])
@api.doc(description='Get story variables from a chosen topic')
class story(Resource):
    def get(self, topic):

        story = {}

        if topic == 'rape':
            story['victim'] = generate_person(True)
            story['rapist'] = generate_person(False)

        return jsonify(story)


# Run server
if __name__ == '__main__':
    app.run("0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
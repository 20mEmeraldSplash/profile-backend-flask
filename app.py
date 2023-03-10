from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

POLL_RESULTS = {
    'yes': 0,
    'no': 0,
}

# TodoList
class PollResults(Resource):
    def get(self):
        return POLL_RESULTS

# VoteYes
class VoteYes(Resource):
    def get(self):
        return POLL_RESULTS['yes']
    def put(self):
        POLL_RESULTS['yes'] += 1
        return POLL_RESULTS['yes'], 201

# VoteNo
class VoteNo(Resource):
    def get(self):
        return POLL_RESULTS['no']
    def put(self):
        POLL_RESULTS['no'] += 1
        return POLL_RESULTS['no'], 201

api.add_resource(PollResults, '/polls')
api.add_resource(VoteYes, '/polls/yes')
api.add_resource(VoteNo, '/polls/no')

if __name__ == '__main__':
    app.run(debug=True)
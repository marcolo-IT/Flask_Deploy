from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
api = Api(app)

account_post_args = reqparse.RequestParser()
account_post_args.add_argument("name", type=str, help="Name of account is required", required=True)
account_post_args.add_argument("employees", type=int, help="employees of account is required", required=True)

accounts = {}

class account(Resource):
    def get(self, account_id):
        return accounts[account_id]
    
    def post(self, account_id):
        args = account_post_args.parse_args()
        accounts[account_id] =args
        return accounts[account_id], 201

api.add_resource(account, "/account/<int:account_id>") #endPoint

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000,ssl_context='adhoc') #start our server
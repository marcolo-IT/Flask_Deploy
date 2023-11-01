from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

account_post_args = reqparse.RequestParser()
account_post_args.add_argument("name", type=str, help="Name of account is required", required=True)
account_post_args.add_argument("employees", type=int, help="employees of account is required", required=True)

accounts = {}
latest_data = {}  # Store the latest POST data

class account(Resource):
    def get(self, account_id):
        return accounts[account_id]
    
    def post(self, account_id):
        args = account_post_args.parse_args()
        accounts[account_id] =args
        latest_data["name"] = args["name"]
        latest_data["employees"] = args["employees"]
        return accounts[account_id], 201

api.add_resource(account, "/account/<int:account_id>") #endPoint

@app.route('/latest_data')
def display_latest_data():
    return render_template('display.html', latest_data=latest_data)

if __name__ == "__main":
    app.run(debug=True)
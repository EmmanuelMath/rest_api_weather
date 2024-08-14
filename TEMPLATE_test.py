from flask import Flask, request, jsonify

app = Flask(__name__)

# GET
@app.route('/get-user/<user_id>') #<path_parameter> dynamic value passed in url 
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name": "banukoreda",
        "email": "arobaser@gmail.com"
    }
    extra = request.args.get("extra")
    if extra: 
        user_data["extra"] = extra
    return jsonify(user_data), 200

@app.route("/create_user", methods=["POST"])
def create_user():
    # if request.method == "POST":
    data = request.get_data()
    return jsonify(data)
    



if __name__== "__main__":
    app.run(debug=True)

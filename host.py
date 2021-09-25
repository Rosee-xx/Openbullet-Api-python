from flask import Flask
from flask.app import Flask, request, jsonify
from flask.helpers import send_file
from werkzeug.datastructures import Headers
app = Flask(__name__)

@app.route("/api/configs", methods = ["GET", "POST"])
async def index():
    headers = request.headers
    key = headers.get("Authorization")
    ipnow = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ipcombo = f"{key}:{ipnow}"
    noip = f"{key}"
    print(ipnow)
    with open("./api/data.txt", "r") as databasefile:
        lolxdddd = databasefile.read()
        if ipcombo in lolxdddd:
            jsonify({"message": f"{key} iS Locked To {ipnow}"}), 200
            return send_file("configs.zip"), 200
        elif noip in lolxdddd:
            print("first time")
            writeout = lolxdddd.replace(f"{key}", f"{key}:{ipnow}\n")
            with open('./api/data.txt', 'w') as file:
                file.write(writeout)
            return jsonify({"message": f"Were Locking {key} to your ip: {ipnow}"})
        else: 
            print("wrong")
            return jsonify({"message": "ERROR: Incorrect Key"}), 401

@app.route("/api/users", methods = ["GET", "POST"])
async def users():
    Headers = request.headers
    key = Headers.get("secret_key")
    addthiskeyz = Headers.get("addthiskey")
    if key == "uiyawndiuawmndd":
        with open("./api/data.txt", "w") as file:
            file.write(addthiskeyz)
            return jsonify({"message": f"Your Key {addthiskeyz} Has Been Added To The Keys List \n First Time Connect Will Lock The Code To Your IP Share It And Youll Get Banned (:"}), 200
    else: 
        return jsonify({"message": "ERROR: You Have The Wrong Secret Key."}), 401

@app.route("/api/users/delete", methods = ["GET", "POST"])
async def delete_user():
    Headers = request.headers
    # coming soon cuties
        

app.run(host='put ip v4 here (:', port = 8000, threaded = True, debug = True)
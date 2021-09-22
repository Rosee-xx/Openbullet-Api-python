from flask.app import Flask, request, jsonify
from flask.helpers import send_file
app = Flask(__name__)

@app.route("/api/configs", methods = ["GET", "POST"])
async def index():
    headers = request.headers
    key = headers.get("Authorization")
    ipnow = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ipcombo = f"{key}:{ipnow}"
    noip = f"{key}:"
    print(ipnow)
    with open("./api/data.txt", "r") as databasefile:
        lolxdddd = databasefile.read()
        if ipcombo in lolxdddd:
            jsonify({"message": f"{key} iS Locked To {ipnow}"}), 200
            return send_file("configs.zip"), 200
        elif noip in lolxdddd:
            print("first time")
            writeout = lolxdddd.replace(f"{key}:", f"{key}:{ipnow}\n")
            with open('./api/data.txt', 'w') as file:
                file.write(writeout)
            return jsonify({"message": f"Were Locking {key} to your ip: {ipnow}"})
        else: 
            print("wrong")
            return jsonify({"message": "ERROR: Incorrect Key"}), 401

@app.route("/api/users",methods = ["GET", "POST"])
async def users():
    Headers = request.headers ## coming soon (; adding a feature to add users very nice ikr


app.run(host='PUT IPV4 HERE (:', port = 8000, threaded = True, debug = True)

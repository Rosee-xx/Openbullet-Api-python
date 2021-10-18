import sqlite3
import flask
from flask import Flask
from flask.app import Flask, request, jsonify
from flask.helpers import send_file
import sqlite3
import random
import string
con = sqlite3.connect("database1.db", check_same_thread = False)
cur = con.cursor()
app = Flask(__name__)


def keygen(size=20, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

@app.route("/api", methods = ["GET"])
def login():
  headers = request.headers
  key = headers.get("Authorization")
  ip =  request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  newkey = keygen()
  with open("blacklist.txt", "r") as f:
    if ip in f:
      return jsonify({"message": "ERROR: banned"}), 401
    else:
      cde = f"SELECT key from logins WHERE key='{newkey}' AND ip = '{key}';"
      cur.execute(cde)
      if not cur.fetchone():  # An empty result evaluates to False.
        ipcheck = f"SELECT ip from logins WHERE key='{key}' AND ip = 'NULL';"
        cur.execute(ipcheck)
        if not cur.fetchone():
            print("wrong key or ip")
            return jsonify({"message": "The Key Or Ip Is Incorrect"}), 400
        else:
            set_ip = f"SELECT ip from logins WHERE key='{key}' AND set ip='{ip}';"
            con.commit(set_ip)
            return jsonify({"message": "We're Locking Your Ip To This Key"}), 200
      else:
        return jsonify({"message": "You logged In Succesfully"}), 200

@app.route("/", methods = ["GET", "POST"])
def main():
  headers = request.headers
  secret_code = headers.get("secret_code")
  if secret_code == "THISCLASSISBORINGLOL":
    key = headers.get("Authorization")
    ip =  request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    newkey = keygen()
    with open("data.txt", "r") as r:
      e = r.readlines()
      if "1" in e:
        if request.method == 'POST':
          with open("blacklist.txt", "r") as f:
            if ip in f:
              return jsonify({"message": "ERROR: Incorrect Key"}), 401
            else:
              cde = f"SELECT key from logins WHERE key='{newkey}' AND ip = '{key}';"
              cur.execute(cde)
              if not cur.fetchone():  # An empty result evaluates to False.
                return jsonify({"message": "ERROR: Incorrect Key"}), 401
              else:
                return jsonify({"message": "well done you cunt"}), 200
        else:
          cur.executescript(f"INSERT INTO logins VALUES ('{key}','{ip}')")
          con.commit()
          print(f"key created key: {key} ip: {ip}")
          return(newkey)
  else:
    return jsonify({"message": "You must add your secret key to add a user to the database"})

app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)
import logging, itertools, sqlite3, os, base64, hashlib, time
from flask import Flask, request

if os.path.exists("./game.db"):
  conn = sqlite3.connect("game.db")
  cursor = conn.cursor()
version = "Alpha 0.0.3"
game_version = "2.1"

app = Flask(__name__)

logging.getLogger('werkzeug').disabled = True

# /===================================/
#                ROUTES
# /===================================/
@app.route('/')
def home():
  return "Server ran with GDServerPy"

@app.route('/accounts/registerGJAccount.php')
def register_account():
  payload = request.json
  username = payload["userName"]
  password = payload["password"]
  email = payload["email"]
  creation_date = int(time.time())
  if len(username) > 20:
    return -4
  if len(cursor.execute(f"SELECT * from accounts WHERE userName='{username}'")):
    return -2
  hashed_password = hashlib.sha256(password.encode())
  cursor.execute(f"INSERT INTO accounts (userName, password, email, registerDate, isActive) VALUES ({username},{hashed_password},{email},{creation_date},1)")
  return 1

# /===================================/
#           OPTION FUNCTIONS
# /===================================/
def start_server():
  app.run("0.0.0.0", port=80)

def reset_database():
  print("IF YOU ALREADY HAVE A DATABASE IT WILL BE CLEARED. DO YOU STILL WANT CONTINUE? [Y/N]")
  awnser = input()
  if awnser == "Y" or awnser == "y":
    if os.path.exists("./game.db"):
      print_info("Clearing Database...")
      with open("game.db","w") as f:
        f.write("")
      print_info("Cleared Database")
    else:
      print_info("Creating Database...")
      sqlite3.connect("game.db")
      print_info("Created Database")
    conn = sqlite3.connect("game.db")
    with open("data.sql","r") as f:
      conn.executescript(f.read())
  else:
    print_info("Exited")     

# /===================================/
#           HELPER FUNCTIONS
# /===================================/
def xor_cipher(string: str, key: str) -> str:
  return ("").join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))

def xor_and_base64(string: str, key: str):
  base64.b64encode(xor_cipher(string,key))

def print_info(text: str):
  print(f"[INFO] {text}")

# /===================================/
#                START
# /===================================/

print(f"""
   __________  _____                           ____       
  / ____/ __ \/ ___/___  ______   _____  _____/ __ \__  __
 / / __/ / / /\__ \/ _ \/ ___/ | / / _ \/ ___/ /_/ / / / /
/ /_/ / /_/ /___/ /  __/ /   | |/ /  __/ /  / ____/ /_/ / 
\____/_____//____/\___/_/    |___/\___/_/  /_/    \__, /   {version}
                                                 /____/         
made by mel0n7

version: {version}
game version: {game_version}
GitHub: https://github.com/mel0n7/GDServerPy""")
print("""
Type a number
1. Start Server
2. Server Prefrences/Settings
3. Create/Reset Database""")
option = int(input())
option_functions = {1: start_server,3:reset_database}
option_functions[option]()
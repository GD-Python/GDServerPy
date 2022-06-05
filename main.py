import logging, sys, itertools
from flask import Flask, render_template

version = "Alpha 0.0.1"
game_version = "2.1"
l = True # Turns Logging on and off

app = Flask(__name__)

logging.getLogger('werkzeug').disabled = True

# /===================================/
#                ROUTES
# /===================================/
@app.route('/')
def home():
  return "Server ran with GDServerPy"

# /===================================/
#           OPTION FUNCTIONS
# /===================================/
def start_server():
  app.run("0.0.0.0", port=80)

# /===================================/
#           HELPER FUNCTIONS
# /===================================/
def xor_cipher(string: str, key: str) -> str:
    return ("").join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))

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
2. Server Prefrences/Settings""")
option = int(input())
option_functions = {1: start_server}
option_functions[option]()
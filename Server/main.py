from flask import Flask, render_template, session, request
from flask_socketio import SocketIO

# Server Setup
app = Flask(__name__)
app.config["SECRET_KEY"] = 'key!'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name", "")
        code = request.form.get("code", "")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        # name empty
        if not name:
            print("Hello")
            print(code)
            return render_template("home.html", error="Please enter a name.", code=code, name=name)
        # code empty
        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)

        room = code
        # create was pressed
        if create != False:
            #create room
            pass
        
        # -> case for: code doesnt exist

        session["room"] = room
        session["name"] = name
        
        # -> send to room
    return render_template("home.html", name="", code="")

@app.route("/room")
def room():
    room = session.get("room")
    return render_template("room.html", room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)
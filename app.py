# app.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import stomp

app = Flask(__name__)
socketio = SocketIO(app)

# Connect to ActiveMQ Artemis broker
conn = stomp.Connection([('localhost', 61613)])
conn.start()
conn.connect(wait=True)

# Index route to render the chat room
@app.route('/')
def index():
    return render_template('index.html')

# Handle message from client and broadcast it to all users
@socketio.on('message')
def handle_message(msg):
    conn.send(body=msg['data'], destination='/queue/chat')

# Listen for messages from ActiveMQ Artemis broker
class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, body):
        socketio.emit('message', {'data': body}, broadcast=True)

listener = MyListener()
conn.set_listener('', listener)
conn.subscribe(destination='/queue/chat', id=1, ack='auto')

if __name__ == '__main__':
    socketio.run(app)

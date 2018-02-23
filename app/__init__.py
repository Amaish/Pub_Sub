from flask import Flask
from config import Config
import time
import socket

def create_socket():
    global s
    global socket_message
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_message = "Socket created"
    print socket_message



app = Flask(__name__)
create_socket()
app.config.from_object(Config)



from app import routes

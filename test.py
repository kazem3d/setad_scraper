import threading

def hello_world():
    threading.Timer(4.0, hello_world).start() # called every minute
    print("Hello, World!")

hello_world()
while True:
    print('kazem')
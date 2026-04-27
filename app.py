from flask import Flask
import redis
import os

redis_host = os.getenv('REDIS_HOST', 'localhost')
app = Flask(__name__)

# Connect to Redis
redis_host=os.getenv('REDIS_HOST')
redis_port=int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def home():
    count = r.incr('counter')
    return f'Hello! You visited {count} times 🚀'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
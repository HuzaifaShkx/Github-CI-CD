import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")

r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        count = r.incr("counter")
        return f"Visits: {count}"
    except:
        return "App running but Redis not connected"
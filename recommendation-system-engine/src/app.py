#!/usr/bin/env python
# coding=utf-8
from flask import Flask
app = Flask('recommendation-system-engine', instance_relative_config=True)
# Load the default configuration
app.config.from_object('config')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

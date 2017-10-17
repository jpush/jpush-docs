from github_webhook import Webhook
from flask import Flask
import os

app = Flask(__name__)
webhook = Webhook(app, "/")

REPOS = [
    'jpush-api-java-client',
    'jpush-api-csharp-client',
    'jpush-api-php-client',
    'jpush-api-python-client',
    'jpush-api-nodejs-client',
    'jpush-api-ruby-client',
    'jmessage-api-java-client',
    'jmessage-api-csharp-client',
    'jmessage-api-python-client',
    'jmessage-api-php-client',
    'jsms-api-java-client',
    'jsms-api-php-client',
    'jsms-api-csharp-client'
]
current = os.path.split(os.path.realpath(__file__))[0]
separator = "\n========================================================================\n"
log_file = "{0}/hooks.log".format(current)

def log_it(str):
    f = open(log_file,'a')
    f.write(str)
    f.close()

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook('ping')    # Defines a handler for the 'ping' event
def on_ping(data):
    log_it(separator + "Pong Pong\n\n")

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    branch = data['ref'].split('/', 2)[2];
    repo = data['repository']['name']
    greeting = separator + "Received Push Event From {repo}#{branch}..\n\n".format(repo=repo, branch=branch)

    if (repo == 'jpush-docs'):
        f = os.popen("{0}/depoly.sh {1}".format(current, branch))
        result = f.read()
    elif (branch == 'master' and repo in REPOS):
        f = os.popen("{0}/synreadme.sh {1}".format(current, repo))
        result = f.read()
    else:
        result = "But we will not handle it"

    log_it(greeting + result + "\n\n")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

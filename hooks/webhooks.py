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
log_file = "{0}/hooks.log".format(current)

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook('ping')    # Defines a handler for the 'ping' event
def on_ping(data):
    print('pong')


@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    branch = data['ref'].split('/', 2)[2];
    repo = data['repository']['name']

    app.logger.info('An error occurred')

    if (repo == 'jpush-docs'):
        result = os.popen("{0}/depoly.sh {1}".format(current, branch))
    if (branch == 'master' and repo in REPOS):
        result = os.popen("{0}/synreadme.sh {1}".format(current, repo))

    f = open(log_file,'a')
    f.write(result.read())
    f.close()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

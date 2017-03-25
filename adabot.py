import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get("BOT_ID")

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def post_dinner_poll():
    slack_client.api_call(
        "chat.postMessage",
        channel="bottest",
        as_user=True,
        text='/poll "Are you coming to dinner tonight at 6pm?" "Yes!" No"'
        )

if __name__ == "__main__":
    READ_WOBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print "Adabot connected and running!"
        post_dinner_poll()
        while True:
            time.sleep(READ_WOBSOCKET_DELAY)
    else:
        print "Connection failed. Invalid Slack token or Bot ID"

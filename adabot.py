import os
from slackclient import SlackClient

BOT_ID = os.environ.get("BOT_ID")
TEST_CHANNEL_ID = u'C4PPUR35J'
STUDENT_ONLY_CHANNEL_ID = 'C2APE9BJ9'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def post_dinner_msg(channel_id):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        as_user=True,
        text='Reminder: Dinner tonight at 6pm!'
        )


# TODO: Re-generate Auth token
def post_dinner_poll(channel_id):
    slack_client.api_call(
        "chat.command",
        token=os.environ.get('SLACK_BOT_TOKEN'),
        channel=channel_id,
        command='/poll',
        text='"Are you coming to dinner tonight at 6pm?" "Yes!" No"'
        )

if __name__ == "__main__":
    if slack_client.rtm_connect():
        print "Adabot connected and running!"
        post_dinner_msg(TEST_CHANNEL_ID)
        # print slack_client.api_call("channels.list")
        post_dinner_poll(TEST_CHANNEL_ID)
        print "post poll"
    else:
        print "Connection failed. Invalid Slack token or Bot ID"

import os
import sys
import json
from slackclient import SlackClient

class Slack:
    def __init__(self):
        with open('config.json') as json_data_file:
            data = json.load(json_data_file)
        self.slack_token = data["SLACK"]["TOKEN"]
        self.slack_channel = data["SLACK"]["CHANNEL"]
    
    def sendMsg(self,message):
        sc=SlackClient(self.slack_token)
        sc.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=message
        )


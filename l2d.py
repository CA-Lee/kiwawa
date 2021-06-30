from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import requests

import os
import json

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['LINEBOT_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['LINEBOT_SECRET'])

discord_webhook = os.environ['DISCORD_WEBHOOK']

@app.route("/")
def root():
    return 'OK'

@app.route("/callback",methods=['POST'])
def callback():
    sign = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, sign)
    except InvalidSignatureError:
        print("Invalid signature. Check token and/or secret")
        abort(400)

    return 'OK'


def create_request_data(event, text=None) -> dict:
    profile = line_bot_api.get_group_member_profile(event.source.group_id,event.source.user_id)
    
    request_data = {
        "content":text,
        "username":profile.display_name + " from LINE",
        "avatar_url":profile.picture_url
    }

    return request_data

def get_binary_data(event) -> str:
    content = line_bot_api.get_message_content(event.message.id)

    file = b""
    for chunk in content.iter_content():
        file += chunk

    return file


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    request_data = create_request_data(event, event.message.text)
    requests.post(url=discord_webhook, data=request_data)

@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    request_data = create_request_data(event)
    file = get_binary_data(event)
    requests.post(url=discord_webhook, data=request_data, files={'media.jpg':file})

@handler.add(MessageEvent, message=VideoMessage)
def handle_image(event):
    request_data = create_request_data(event)
    file = get_binary_data(event)
    requests.post(url=discord_webhook, data=request_data, files={'media.mp4':file})

@handler.add(MessageEvent, message=AudioMessage)
def handle_image(event):
    request_data = create_request_data(event)
    file = get_binary_data(event)
    requests.post(url=discord_webhook, data=request_data, files={'media.mp3':file})

@handler.add(MessageEvent, message=FileMessage)
def handle_image(event):
    request_data = create_request_data(event)
    file_name = event.message.file_name
    file = get_binary_data(event)
    requests.post(url=discord_webhook, data=request_data, files={file_name:file})


if __name__ == "__main__":
    app.run()

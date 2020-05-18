from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

line_bot_api = LineBotApi('BCm52q9Tinn9O8X/InnaEO2n5RC1wHHBuMCV7CJJCGxW4xFfEeUnR5LJQ1lBfOgkaCOGlOeeSJFQTq8CCRU6b0elB9TVq4N1oe0LMMs8Q5O6b92FeAKL+WTclw4RBbpOyBCWNuc114vZ0DXvX5JeXgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6c317257b7cb75fce536facab0c74fdb')

@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
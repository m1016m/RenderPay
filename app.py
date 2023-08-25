from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,FollowEvent,UnfollowEvent,
)
from linebot.models import *

app = Flask(__name__)


line_bot_api = LineBotApi('WP3l+IaLvwbZieLYtAZBX1ovU0kXCHPwNNxRWeSMD7Kz1BfsF0UJ1wb7H6xat4qXuC6PfxNyZZ9lF6uRgRnhJevRt84YIhGlHPCjdS+KKaDo7ipGTp0PvJC0x2XL2I6Vxef93vBkbSiti3cX8VNb2AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9adf1e3e91823a6cf44096f7cf71c90e')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

def handle_message(event):
    message_text = str(event.message.text).lower()
    message = None
    #event有什麼資料？詳見補充
    if message_text == "story":
        message = "story"
        line_bot_api.reply_message(
        event.reply_token,
        message)
    elif message_text =='add':
        message = 'list products'
    
    elif message_text =='cart':
        message = 'cart'

    if message:
        line_bot_api.reply_message(
        event.reply_token,
        message)



if __name__ == "__main__":
    app.run()
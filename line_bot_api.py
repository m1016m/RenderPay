
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, 
    StickerSendMessage, ImageSendMessage, LocationSendMessage,FlexSendMessage,
    TemplateSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackAction,
    PostbackEvent,QuickReply,QuickReplyButton,ConfirmTemplate,MessageAction,ButtonsTemplate
)

# Channel access token
line_bot_api = LineBotApi('WP3l+IaLvwbZieLYtAZBX1ovU0kXCHPwNNxRWeSMD7Kz1BfsF0UJ1wb7H6xat4qXuC6PfxNyZZ9lF6uRgRnhJevRt84YIhGlHPCjdS+KKaDo7ipGTp0PvJC0x2XL2I6Vxef93vBkbSiti3cX8VNb2AdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('9adf1e3e91823a6cf44096f7cf71c90e')
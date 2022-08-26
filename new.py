#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/P3U16D7.png",
                    action=URITemplateAction(
                        label="指令一覽1",
                        uri="https://i.imgur.com/P3U16D7.png"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/w8ZPJP0.png",
                    action=URITemplateAction(
                        label="指令一覽2",
                        uri="https://i.imgur.com/w8ZPJP0.png"
                    )
                ),
                
                
            ]
        )
    )
    return message
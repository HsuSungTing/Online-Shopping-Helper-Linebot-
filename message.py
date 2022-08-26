#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/hVlhu4f.jpg",
        alt_text='最新的合作銀行有誰呢？',
        base_size=BaseSize(height=1080, width=1080),
        actions=[
            URIImagemapAction(
                #花旗
                link_uri="https://shopping.pchome.com.tw/edm/card/021.htm",
                area=ImagemapArea(
                    x=0, y=0, width=540, height=540
                )
            ),
            URIImagemapAction(
                #玉山
                link_uri="https://shopping.pchome.com.tw/edm/card/808.htm",
                area=ImagemapArea(
                    x=540, y=0, width=540, height=540
                )
            ),
            URIImagemapAction(
                #中國
                link_uri="https://shopping.pchome.com.tw/edm/card/822.htm",
                area=ImagemapArea(
                    x=0, y=540, width=540, height=540
                )
            ),
            URIImagemapAction(
                #第一
                link_uri="https://shopping.pchome.com.tw/edm/card/007.htm",
                area=ImagemapArea(
                    x=540, y=540, width=540, height=540
                )
            ),
            
        ]
    )
    return message



#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="免費註冊享回饋",
                    uri="https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://a.ecimg.tw/css/2016/style/images/v201607/sitelogo/book.png',
                    title='PChome book store',
                    text='要進入PChome書香小天地嗎?',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='先不要啦',
                            text='先不要啦'
                        ),
                        URITemplateAction(
                            label='我要去PChome書店享受書香味',
                            uri='https://24h.pchome.com.tw/books/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://fastdealszone.com/wp-content/uploads/2021/05/54735548f4298920877419324dbc8d6b.png',
                    title='比比昂代購服務區',
                    text='國外好物代購交給比比昂搞定',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='先不要啦',
                            text='先不要啦'
                        ),
                        URITemplateAction(
                            label='進入比比昂代購區',
                            uri='https://www.pchomeec.tw/sites/overseasgoods'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://pchometravel.com/image/opengraph.jpg?v=20180712',
                    title='PChome旅遊',
                    text='想出去走走嗎?好好犒賞自己一下吧!',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='先不要啦',
                            text='先不要啦'
                        ),
                        URITemplateAction(
                            label='我要進入PChome旅遊逛逛',
                            uri='https://www.pchometravel.com/'
                        )
                    ]
                )
            ]
        )
    )
    return message
def Carousel2_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://82162.cdn.cke-cs.com/9Y74n6bfBJPEUdKxcnV0/images/a83b7e1ffbecd7df8a77ec152a1b6a400c35b42b84a25fa9.png',
                    title='PChome客服中心',
                    text='客服中心來拯救你了!',
                    actions=[
                       URITemplateAction(
                            label='新手上路',
                            uri='https://ecvip.pchome.com.tw/web/pages/newbie.htm'
                        ),
                        URITemplateAction(
                            label='購物流程',
                            uri='https://ecvip.pchome.com.tw/web/pages/shopprocess.htm'
                        ),
                        URITemplateAction(
                            label='訂單查詢與問題',
                            uri='https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fecvip.pchome.com.tw%2Fweb%2Forder%2Fall'
                        )
                    ]
               
               )
            ]   
        )
    )
    return message


#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
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

#關於LINEBOT聊天內容範例
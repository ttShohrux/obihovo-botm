import requests
from bs4 import BeautifulSoup as BS
from knopka import vloyatlar_knop



def start(update, context):
    user = update.message.from_user
    update.message.reply_html("Asalomu alekum bugungi ob hovoni biznig bota tanishin:".format(user.first_name), reply_markup=vloyatlar_knop)
    return 1



def toshkent(update,context):
    r=requests.get('https://sinoptik.ua/погода-ташкент')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Toshkent bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)

def toshkentvil (update,context):
    r=requests.get('https://sinoptik.ua/погода-кибрай')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Toshkent viloyatida bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)



def buxoro(update,context):
    r=requests.get('https://sinoptik.ua/погода-бухара')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Buxoroda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)


def srdaryo(update,context):
    r=requests.get('https://sinoptik.ua/погода-сырдарья')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Srdaryoda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)


def jizax(update,context):
    r=requests.get('https://sinoptik.ua/погода-джизак')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Jizaxda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)



def samarqand(update,context):
    r=requests.get('https://sinoptik.ua/погода-самарканд')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Samarqanda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)

def fargona(update,context):
    r=requests.get('https://sinoptik.ua/погода-фергана')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Farg'onada bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)



def namangan(update,context):
    r=requests.get('https://sinoptik.ua/погода-наманган')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Namanganda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)



def andijon(update,context):
    r=requests.get('https://sinoptik.ua/погода-андижан')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Andijon bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)




def qashqadaryo(update,context):
    r=requests.get('https://sinoptik.ua/погода-карши')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Qashqadaryoda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)


def surxandaryo(update,context):
    r=requests.get('https://sinoptik.ua/погода-термез')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Surxandaryo bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)



def xorazm(update,context):
    r=requests.get('https://sinoptik.ua/погода-ургенч')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text( f"Xorozimda bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)




def qoraqalpogistan(update,context):
    r=requests.get('https://sinoptik.ua/погода-нукус')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Qoraqalpog'istan bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)


def navoi(update,context):
    r=requests.get('https://sinoptik.ua/погода-навои')

    html = BS(r.content, 'html.parser')
    minium = html.findAll("div",{"class":"min"})
    maxinum = html.findAll("div",{"class":"max"})

    t_min = minium[0].text
    t_max = maxinum[0].text
    update.message.reply_text(f"Navoyidada bugungi ob hovo\nEng past Temperatura: {t_min}\nEng yuqori tempera tura: {t_max}\nEng past tempera tura",reply_markup=vloyatlar_knop)


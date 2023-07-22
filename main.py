import telebot
from telebot import types
from PIL import Image, ImageDraw, ImageFont



def draw(text):
    image = Image.open(r'img/image.png')
    font = ImageFont.truetype("impact.ttf", 45)
    drawer = ImageDraw.Draw(image)
    drawer.text((100, 100),text , font=font, fill='black')
    image.save(r'img/new_image.png')

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сдалать мем")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Ты мне фото с текстом, а я тебе мем", reply_markup=markup)
    bot.send_message(message.from_user.id, "Отправь сначала фотку, а потом текст", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def photo(message):   
     fileID = message.photo[-1].file_id   
     file_info = bot.get_file(fileID)
     downloaded_file = bot.download_file(file_info.file_path)
     with open(r'img/image.png', 'wb') as new_file:
         new_file.write(downloaded_file)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        draw(message.text)
        photo = open(r'img/new_image.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        

bot.polling(none_stop=True, interval=0)

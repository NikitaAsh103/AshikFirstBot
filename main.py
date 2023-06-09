import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open("facts.txt", 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список анекдотов
f = open('anecdot.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('Анекдот:')
f.close()
# Создаем бота
bot = telebot.TeleBot('6051502339:AAFO4ksMzDmrxbBX-RXXQda7dFFNzl5aQkA')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Анекдот")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Анекдот':
            answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)

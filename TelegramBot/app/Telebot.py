from telebot.async_telebot import AsyncTeleBot
from telebot import types
import logging
import asyncio

class Telebot:
    def __init__(self, api, chat_id):
        self.api = api
        self.bot = AsyncTeleBot(self.api)
        self.public_chat_id = chat_id
    
    async def start(self, message):
        try:
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Администратор домов 👩‍💼")
            btn2 = types.KeyboardButton("Администратор гостиницы 💁‍♂️")
            btn3 = types.KeyboardButton("Сделать заказ в ресторане 🍽️")
            btn4 = types.KeyboardButton("Записаться на массаж 💆‍♀️")
            btn5 = types.KeyboardButton("Прокат техники ✍️")
            text = "👋 Привет! Я твой бот-помошник!\nПожалуйста выберете с кем хотите связаться 😊"
            notification = (
            "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n" +
            "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n" +
            "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n" +
            "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n" +
            "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️") 
            markup.add(btn1, btn2, btn3, btn4, btn5)
            await self.bot.send_message(message.from_user.id, text, reply_markup=markup)
            await self.bot.send_message(message.from_user.id, notification, reply_markup=markup)
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
    

    async def house(self, message):
        try:
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            await self.bot.send_message(message.from_user.id, "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
        

    async def admin(self, message):
        try:
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            await self.bot.send_message(message.from_user.id, "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
            
    async def restourant(self, message):
        try:
        #is_user = await IsUser(message)
        #if (is_user == False):
        #    return
            await self.bot.send_message(message.from_user.id, "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")    


    async def message(self, message):
        try:
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            await self.bot.send_message(message.from_user.id, "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")

    async def admin(self, message):
        try:
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            await self.bot.send_message(message.from_user.id, "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")


    async def get_text_messages(self, message):
        try: 
            #is_user = await IsUser(message)
            #if (is_user == False):
            #    return
            if message.text == 'Администратор домов 👩‍💼':
                await self.bot.send_message(message.from_user.id, "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n")
            elif message.text == 'Администратор гостиницы 💁‍♂️':
                await self.bot.send_message(message.from_user.id, "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n")
            elif message.text == 'Сделать заказ в ресторане 🍽️':
                await self.bot.send_message(message.from_user.id, "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n")
            elif message.text == 'Записаться на массаж 💆‍♀️':
                await self.bot.send_message(message.from_user.id, "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n")
            elif message.text == 'Прокат техники ✍️':
                await self.bot.send_message(message.from_user.id, "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️")
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start(self, message)
            
        @self.bot.message_handler(commands=['house'])
        def handle_house(message):
            self.house(self, message)
            
        @self.bot.message_handler(commands=['admin'])
        def handle_admin(message):
            self.admin(self, message)
            
        @self.bot.message_handler(commands=['restaurant'])
        def handle_restaurant(message):
            self.restourant(self, message)
            
        @self.bot.message_handler(commands=['massage'])
        def handle_message(message):
            self.message(self, message)
            
        @self.bot.message_handler(commands=['rent'])
        def handle_rent(message):
            self.rent(self, message)
        
        @self.bot.message_handler(content_types=['text'])
        def handle_text(message):
            self.get_text_messages(self, message)
            
        asyncio.run(self.bot.polling())
        
    async def send_message(self, message_text=""):
        try: 
            await self.bot.send_message(self.public_chat_id, message_text)
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")

    def asyncSend_Message(self, message_text=""):
        try: 
            asyncio.run(self.send_message(message_text))
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
            
    async def MessageToChannel(self, message = ""):
        try:
            await self.bot.send_message(self.public_chat_id, message)
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
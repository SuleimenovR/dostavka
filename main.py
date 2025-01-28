import os.path
import config
import flask
import telebot
from telebot import types
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


bot = telebot.TeleBot(config.token)
server = flask.Flask(name)

cred = credentials.Certificate("bott.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'firebase'})




@bot.message_handler(commands=['start'])
def start (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Начать']])
    msg = bot.send_message(message.chat.id, 'Здравствуйте, что-бы пользоваться ботом нажмите кнопку НАЧАТЬ', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start2)


def start2 (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Сделать заказ']])
    msg = bot.send_message(message.chat.id, 'Что-бы сделать заказ нажмите СДЕЛАТЬ ЗАКАЗ', reply_markup=keyboard)
    bot.register_next_step_handler(msg, restaurant)


def restaurant(message):
    if message.text == 'Сделать заказ':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['KFC', 'McDonalds']])
        msg = bot.send_message(message.chat.id, 'Выберите ресторан', reply_markup=keyboard)
        bot.register_next_step_handler(msg, orderB)


def orderB(message):
    if message.text == 'KFC':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', 'Бургеры', 'Твистеры', 'Курица', "Баскеты", "Снэки", "Соусы", "Напитки", "Кофе и чай",
                        "Десерты", "Хиты по 50", "Ланч Баскеты", "Завтрак (до 11:00)"]])
        msg = bot.send_message(message.chat.id, 'Выберите категорию товара', reply_markup=keyboard)
        bot.register_next_step_handler(msg, KFC)
    elif message.text == 'McDonalds':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Сандвичи", "Картофель и стартеры", "Салаты и роллы", "Десерты и выпечка",
                        "Напитки и коктейли", "Кофе, чай", "Соусы"] ] )
        msg = bot.send_message(message.chat.id, 'Выберите категорию товара', reply_markup=keyboard)
        bot.register_next_step_handler(msg, McDonalds)


def KFC(message):
    if message.text == 'Бургеры':
        db.reference('/KFC').child(message.from_user.username).update({'Burgers':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Лонгер BBQ 50р", "Чизбургер 69р", "Шефбургер Де Люкс 144р",
                        "Шефбургер Де Люкс острый 144р", "Хот-дог куриный 79р", "Чизбургер Де Люкс 124р",
                        "Шефбургер 99р", "Шефбургер острый 99р", "Двойной Темный Бургер 259р", "Темный Бургер 179р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Твистеры':
        db.reference('/KFC').child(message.from_user.username).update({'Twister':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', 'Твистер оригинальный 159р', "Твистер острый 159р", "БоксМастер оригинальный 194р",
                        "БоксМастер острый 159р", "Ай-Твистер Чиз 55р", "Твистер Де Люкс острый 184р",
                        "Твистер Де Люкс оригинальный 194р", "Твистер Джуниор 99р", "Темный Твистер 194р",
                        "Темный БоксМастер 214р"] ] )
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Курица':
        db.reference('/KFC').child(message.from_user.username).update({'Chicken':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', 'Байтс от 94р', "Крылья острые от 104р", "Стрипсы острые от 114р",
                        "Стрипсы оригинальные от 114р", "Байтс Терияки 134р", "Ножки от 104р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Баскеты':
        db.reference('/KFC').child(message.from_user.username).update({'Baskets':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Баскет Дуэт с острыми стрипсами 409р", "Баскет Дуэт с оригинальными стрипсами 409р",
                        "Пати Баскет 104р", "Баскет S 389р", "Баскет M 509р", "Баскет  L 609р", "Сандерс Баскет 199р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Снэки':
        db.reference('/KFC').child(message.from_user.username).update({'Snacks':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Картофель фри от 50р", "Салат Цезарь Лайт 139р", "Картофель по-деревенски от 50р",
                        "Салат Коул Слоу 50р", "Сырные подушечки от 59р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Соусы':
        db.reference('/KFC').child(message.from_user.username).update({'Sauce':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Кетчуп томатный 27р", "Соус Барбекю 27р", "Соус Чесночный 27р",
                        "Соус Кисло-Сладкий Чили", "Соус Терияки 27р", "Соус Сырный оригинальный 27р",
                        "Соус клюквенный 27р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Напитки':
        db.reference('/KFC').child(message.from_user.username).update({'Drinks':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Pepsi от 50р", "7up от 50р", 'Mirinda от 50р', "Чай Липтон Лимон  от 50р",
                        "Чай Липтон Зеленый от 50р", "7up Мохито 89р", "Чай Липтон Зеленый Бутылка 0,5л 84р",
                        "Липтон Чай Лимон Бутылка 0,5л 84р", "Аква Минирале Актив Цитрус 0,6л 84р", "Шеф Лимонад 89р",
                        "Милкшейк Клубника от 39р", "Милкшейк Ваниль от 39р", "Милкшейк Шоколадно-Ореховый от 39р",
                        "Pepsi бутылка 0,5л 84р", 'Pepsi бутылка 1л 110р', "Аква Минирале газ. 0,5л 84р",
                        "Аква Минирале без газа 0,5л 84р", "Сок J7 апельсиновый 0,2л 59р, Сок J7 яблочный 0,2л 59р",
                        "Сок J7 вишневый 0,2л 59р", "Лимонад Барбарис 89р", "Милкшейк Пина Колада от 39р",
                        "Айс Кофе Миндаль 89р", "Пепси Макс бутылка 0,5р 84р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, KFCC)
    elif message.text == 'Кофе и чай':
        db.reference('/KFC').child(message.from_user.username).update({'Coffee and tea':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Кофе Двойной Эспрессо 0,1л 69р", "Кофе Американо от 49р", "Чай зеленый от 69р",
                        "Чай черный от 69р", "Кофе Латте от 59р", "Кофе Гяссе 0,2л 104р", "Кофе Капучино от 59р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, KFCC)
    elif message.text == 'Десерты':
        db.reference('/KFC').child(message.from_user.username).update({'Dessert':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton (name) for name in
                       ['Назад', "Тирамису 99р", "Маффин Тоффи 109р", "Мороженое рожок <<Летнее>> 29р",
                        "Пирожок Яблоко 50р", "Пирожок Малина-Черника 50р", "Мороженое Кит Кат 99р",
                        "Донат Яблоко-Корица 69р", "Мороженое Сникерс 109р", "шоколадный фондан с мороженым 109р",
                        "Шоколадный фондан 99р", "Тропический дисерт 99р", "Чизкйек New-York Карамель 125р",
                        "Чизкйек New-York Шоколад 125р", 'Чизкйек New-York Клубника 125р', "Мороженое шоколадное 70р",
                        "Мороженое карамельное 70р", "Мороженое клубничное 70р", "Рожок в глазури 39р",
                        "Пирожок тропический 50р", "Мороженое Кит Кат с топпингом клубника 99р",
                        "Мороженое Кит Кат с шоколадным топпингом  99р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Хиты по 50':
        db.reference('/KFC').child(message.from_user.username).update({'Hits 50 rubles':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "1 Ножка 50р", "Лонгер BBQ 50р", "2 стрипса оригинальные 50р", "2 стрипса острые 50р",
                        "Пирожок Яблоко 50р", "Пирожок Малина-Черника 50р", "Пирожок тропический 50р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'ЛанчБаскеты':
        db.reference('/KFC').child(message.from_user.username).update({'LunchBaskets':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "ЛанчБаскет 5 за 200 200р", "Ланч Баскет 5 за 250 250р", "ЛанчБаскет 5 за 300 300р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Завтрак (до 11:00)':
        db.reference('/KFC').child(message.from_user.username).update({ 'Breakfast until 11:00':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Джем клубничный 14р", "Джем персиковый 14р", "Твистер утренний 139р", "Блинчики 79р",
                        "Сырники 109р", "Яичница с байтсами 114р", "Хашбраун 50р", "БоксМастер утренний 159р",
                        "Тост с сыром 39р", "Райзер 89р", "Бустер 119р", "Брейкер 109р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, k)
    elif message.text == 'Назад':
        db.reference('/KFC').child(message.from_user.username).update({ 'Dish':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад']])
        msg = bot.send_message(message.chat.id, 'Назад', reply_markup=keyboard)
        bot.register_next_step_handler(msg, restaurant)

def k (message):
    if message.text == "Лонгер BBQ 50р" or "Чизбургер 69р" or "Шефбургер Де Люкс 144р" or "Шефбургер Де Люкс острый 144р" or "Хот-дог куриный 79р" or "Чизбургер Де Люкс 124р" or "Шефбургер 99р" or "Шефбургер острый 99р" or "Двойной Темный Бургер 259р" or "Темный Бургер 179р" or 'Твистер оригинальный 159р' or "Твистер острый 159р" or "БоксМастер оригинальный 194р" or"БоксМастер острый 159р" or "Ай-Твистер Чиз 55р" or "Твистер Де Люкс острый 184р" or"Твистер Де Люкс оригинальный 194р" or "Твистер Джуниор 99р" or "Темный Твистер 194р" or"Темный БоксМастер 214р"or 'Байтс от 94р' or "Крылья острые от 104р" or "Стрипсы острые от 114р" or "Стрипсы оригинальные от 114р" or "Байтс Терияки 134р" or "Ножки от 104р"or"Баскет Дуэт с острыми стрипсами 409р" or "Баскет Дуэт с оригинальными стрипсами 409р" or "Пати Баскет 104р" or "Баскет S 389р" or "Баскет M 509р" or "Баскет  L 609р" or "Сандерс Баскет 199р"or "Картофель фри от 50р" or "Салат Цезарь Лайт 139р" or "Картофель по-деревенски от 50р" or "Салат Коул Слоу 50р" or"Сырные подушечки от 59р"or "Кетчуп томатный 27р" or "Соус Барбекю 27р" or "Соус Чесночный 27р" or "Соус Кисло-Сладкий Чили" or "Соус Терияки 27р" or "Соус Сырный оригинальный 27р" or"Соус клюквенный 27р"or"Тирамису 99р" or  "Маффин Тоффи 109р" or  "Мороженое рожок <<Летнее>> 29р" or "Пирожок Яблоко 50р" or "Пирожок Малина-Черника 50р" or "Мороженое Кит Кат 99р" or "Донат Яблоко-Корица 69р" or  "Мороженое Сникерс 109р" or  "шоколадный фондан с мороженым 109р" or "Шоколадный фондан 99р" or  "Тропический дисерт 99р" or  "Чизкйек New-York Карамель 125р" or  "Чизкйек New-York Шоколад 125р" or  'Чизкйек New-York Клубника 125р' or "Мороженое шоколадное 70р" or "Мороженое карамельное 70р" or  "Мороженое клубничное 70р" or  "Рожок в глазури 39р" or "Пирожок тропический 50р" or  "Мороженое Кит Кат с топпингом клубника 99р" or "Мороженое Кит Кат с шоколадным топпингом  99р""1 Ножка 50р" or "Лонгер BBQ 50р" or "2 стрипса оригинальные 50р" or "2 стрипса острые 50р" or "Пирожок Яблоко 50р" or"Пирожок Малина-Черника 50р" or "Пирожок тропический 50р" or "ЛанчБаскет 5 за 200 200р" or "Ланч Баскет 5 за 250 250р" or "ЛанчБаскет 5 за 300 300р" or "Джем клубничный 14р" or "Джем персиковый 14р" or "Твистер утренний 139р" or "Блинчики 79р" or"Сырники 109р" or "Яичница с байтсами 114р" or "Хашбраун 50р" or "БоксМастер утренний 159р" or"Тост с сыром 39р" or "Райзер 89р" or "Бустер 119р" or "Брейкер 109р":
        db.reference('/KFC').child(message.from_user.username).update({ 'Dish':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
    elif message.text == 'Назад':
        db.reference('/KFC').child(message.from_user.username).update({ 'Dish':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
        

def KFCC (message):
    if message.text == 'Pepsi от 50р' or '7up от 50р' or 'Mirinda от 50р' or 'Чай Липтон Лимон от 50р':
        db.reference('/KFC').child(message.from_user.username).update({'Drinks':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,3 50р', '0,4 65р', '0,5 75р', '0,8 105р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drinksK)
    elif message.text == "Милкшейк Клубника от 39р" or "Милкшейк Ваниль от 39р" or 'Милкшейк Шоколадно-Ореховый от 39р' or 'Милкшейк Пина Колада от 39р':
        db.reference('/KFC').child(message.from_user.username).update({'Milkshakes':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,25 39р', '0,4 99р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drinksK)
    elif message.text == 'Американо от 49р':
        db.reference('/KFC').child(message.from_user.username).update({'Americano':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,2 49р', '0,3 79р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drinksK)
    elif message.text == 'Чай черный от 69р'or 'Чай зеленый от 69':
        db.reference('/KFC').child(message.from_user.username).update({'Tea':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(namberK) for name in ['Назад', '0,3 69р', '0,4 79р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drinksK)
    elif message.text == 'Кофе Латте от 59р' or 'Кофе Капучино от 59р':
        db.reference('/KFC').child(message.from_user.username).update({'Latte and Cappuccino':message.text})
        keyboard = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True)
        keyboard.add (*[types.KeyboardButton (name) for name in ['Назад', '0,2 59р', '0,3 99р', '0,4 109р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler (msg, drinksK)
    elif message.text == 'Назад':
        db.reference('/KFC').child(message.from_user.username).update({'Latte and Cappuccino':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад']])
        msg = bot.send_message(message.chat.id, 'Назад', reply_markup=keyboard)
        bot.register_next_step_handler(msg, restaurant)

def drinksK (message):
    if message.text == '0,3 50р' or '0,4 65р' or '0,5 75р' or '0,8 105р':
        db.reference('/KFC').child(message.from_user.username).update({ 'Liter of drinks':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
    elif message.text == '0,25 39р' or '0,4 99р':
        db.reference('/KFC').child(message.from_user.username).update({ 'Liter of milkshakes':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
    elif message.text == '0,2 49р' or '0,3 79р':
        db.reference('/KFC').child(message.from_user.username).update({ 'Liter Americano':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
    elif message.text == '0,3 69р' or '0,4 79р':
        db.reference('/KFC').child(message.from_user.username).update({ 'Liter of tea':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)
    elif message.text == '0,2 59р' or '0,3 99р' or '0,4 109р':
        db.reference('/KFC').child(message.from_user.username).update({ 'Liter Latte and Cappuccino':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitK)


def dobavitK (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Да', 'Нет']])
    msg = bot.send_message(message.chat.id, 'Хотите дополнить заказ?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, dobavitK2)
    dobavitK2 (message)

def dobavitK2(message):
    if message.text == 'Да':
        KFC(message)
    elif message.text == 'Нет':
        Number (message)
        


def McDonalds (message):
    if message.text == 'Сандвичи':
        db.reference('/McDonalds').child(message.from_user.username).update({'Sandwich':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', 'Вестерн Гурмэ 209р', "Двойной Роял 235р", "Чизбургер 50р", "Гамбургер 48р",
                        "Двойной Филе-О-Фиш 169р", "Пирожек по-итальянски 59р", "Двойной Чизбургер 125р", "Роял 139р",
                        "Филе-О-Фиш 145р", "Макчикен 100р", "Гриль Гурмэ 265р", "Биг Мак 135р", "Роял Де Люкс 159р",
                        "Чикенбургер с беконом 75р", "Чизбургер фреш 75р", "Чикенбургер 50р", "Панини Тоскана 179р",
                        "Роял Бекон 169р", "Чикен Премьер 139р", "Биг Тейсти 249р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, m)
    elif message.text == 'Картофель и стартеры':
        db.reference('/McDonalds').child(message.from_user.username).update({'Potatoes and starters':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', 'Картофель фри Средняя 59р', "Картофель фри Большая 77р",
                        "Большие креветки (6 шт.) 229р", "Большие креветки (9 шт.) 325р",
                        "Большие креветки 20 (шт.) 689р", "Куриные крылышки (6 шт.) 182р",
                        "Куриные крылышки (9 шт.) 258р", "Куриные крылышки (20 шт.) 550р",
                        "Чикен Макнаггетс (6шт.) 105р", "Чикен Макнаггетс (9 шт.) 275р",
                        "Картофель по-деревенски 77р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, m)
    elif message.text == 'Салаты и роллы':
        db.reference('/McDonalds').child(message.from_user.username).update({'Salads and rolls':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Фиш Ролл 169р", "Салат Цезарь 269р", "Шримп Ролл 209р", "Морковные палочки 48р",
                        "Яблочные дольки 48р", "Цезарь Ролл 163р", "Салат овощной 205р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, m)
    elif message.text == 'Десерты и выпечка':
        db.reference('/McDonalds').child(message.from_user.username).update({'Desserts and Baking':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Мороженое карамельное 70р", "Мороженое клубничное 70р", "Вафельный рожок 19р",
                        "Чизкейк по-американски 129р", "Мусс с бельгийским шоколадом 145р", "Пирожок Вишневый 50р",
                        "Пирожок Клубника и сливочный сыр 50р", "Макфлурри Де Люкс Клубнично-Шоколадное 99р",
                        "Мороженое шоколадное 70р", "Макфлурри Де Люкс Клубничный Бискотти 105р",
                        "Макфлурри Де Люкс Карамалень-Шоколадное 99р", "Донат 79р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, m)
    elif message.text == 'Напитки и коктейли':
        db.reference('/McDonalds').child(message.from_user.username).update({'Drinks and Cocktails':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Кофе Айс 109р", "Кока-Кола МакФизз Ваниль 75р", "Коктейл Молочный Дольче Малина 99р",
                        "Кока-Кола от 65р", "Липтон Айс Ти - Зеленый Чай от 65р", 'Молочный Коктейль Клубничный от 99р', "Молоко 55р",
                        "Молочный Коктейль Шоколадный от 99р", "Фанта от 65р", "Апельсиновый сок 80р",
                        "Липтон Айс Ти - Лимон от 65р", "Кока-Кола Зеро от 65р", "Спрайт от 65р",
                        "Питьевая вода Аква Минирале 75р", "Молочный Коктейль Ванильный от 99р", "Яблочный сок 80р",
                        "Мохито Итальано 89р", "Дикая Клюква 75р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, napitki)
    elif message.text == 'Кофе, чай':
        db.reference('/McDonalds').child(message.from_user.username).update({'Coffee and tea':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Чай черный 70р", "Капучино от 99р", 'Кофе от 80р', "Чай черный Эрл Грей 70р",
                        "Чай зеленый 70р", "Латте от 99р", "Двойной Эспрессо 65р", "Кофе Глясе 109р"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler(msg, napitki)
    elif message.text == 'Соусы':
        db.reference('/McDonalds').child(message.from_user.username).update({'Sauces':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in
                       ['Назад', "Соус Барбекю 25р", "Соус Горчичный 25р", "Соус Сладкий Чили 25р", "Соус Сырный 25р",
                        "Кетчуп 25р", "Соус Сальса 25р", "Соус Кисло-Сладкий 25р", "Соус Карри 25р",
                        "Соус 1000 Островов"]])
        msg = bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyboard)
        bot.register_next_step_handler (msg, m)

def m (message):
    if message.text == 'Вестерн Гурмэ 209р' or "Двойной Роял 235р" or"Чизбургер 50р" or "Гамбургер 48р" or "Двойной Филе-О-Фиш 169р" or"Пирожек по-итальянски 59р" or "Двойной Чизбургер 125р" or "Роял 139р" or "Филе-О-Фиш 145р" or"Макчикен 100р" or "Гриль Гурмэ 265р" or "Биг Мак 135р" or "Роял Де Люкс 159р" or "Чикенбургер с беконом 75р" or "Чизбургер фреш 75р" or"Чикенбургер 50р" or "Панини Тоскана 179р" or"Роял Бекон 169р" or "Чикен Премьер 139р" or "Биг Тейсти 249р" or 'Картофель фри Средняя 59р' or "Картофель фри Большая 77р" or"Большие креветки (6 шт.) 229р" or "Большие креветки (9 шт.) 325р" or"Большие креветки 20 (шт.) 689р" or "Куриные крылышки (6 шт.) 182р" or"Куриные крылышки (9 шт.) 258р" or "Куриные крылышки (20 шт.) 550р" or"Чикен Макнаггетс (6шт.) 105р" or "Чикен Макнаггетс (9 шт.) 275р" or"Картофель по-деревенски 77р" or"Фиш Ролл 169р" or "Салат Цезарь 269р" or "Шримп Ролл 209р" or "Морковные палочки 48р" or"Яблочные дольки 48р" or "Цезарь Ролл 163р" or "Салат овощной 205р" or"Мороженое карамельное 70р" or"Мороженое клубничное 70р" or "Вафельный рожок 19р" or"Чизкейк по-американски 129р" or "Мусс с бельгийским шоколадом 145р" or "Пирожок Вишневый 50р" or"Пирожок Клубника и сливочный сыр 50р" or "Макфлурри Де Люкс Клубнично-Шоколадное 99р" or"Мороженое шоколадное 70р" or "Макфлурри Де Люкс Клубничный Бискотти 105р" or"Макфлурри Де Люкс Карамалень-Шоколадное 99р" or "Донат 79р"or"Соус Барбекю 25р" or "Соус Горчичный 25р" or "Соус Сладкий Чили 25р" or "Соус Сырный 25р" or"Кетчуп 25р" or "Соус Сальса 25р" or "Соус Кисло-Сладкий 25р" or "Соус Карри 25р" or "Соус 1000 Островов":
        db.reference('/McDonalds').child(message.from_user.username).update({'Dish':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitM)

def napitki (message):
    if message.text == 'Кока-Кола от 65р' or "Липтон Айс Ти - Зеленый Чай от 65р"or 'Фанта от 65р' or "Липтон Айс Ти - Лимон от 65р" or "Кока-Кола Зеро от 65р" or "Спрайт от 65р":
        db.reference('/McDonalds').child(message.from_user.username).update({'Drinks':message.text})
        keyboard = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,4 65р', '0,5 75р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, Number)
    elif message.text == "Молочный Коктейль Шоколадный от 99р" or "Молочный Коктейль Ванильный от 99р" or 'Коктейл Молочный Дольче Малина 99р' or 'Молочный Коктейль Клубничный от 99р':
        db.reference('/McDonalds').child(message.from_user.username).update({'Cocktails':message.text})
        keyboard = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,47 99р', '0,6 109р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, Number)
    elif message.text == 'Капучино от 99р' or 'Латте от 99р':
        db.reference('/McDonalds').child(message.from_user.username).update({'Cappuccino and Latte':message.text})
        keyboard = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,3 99р', '0,4 109р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, Number)
    elif message.text == 'Кофе от 80р':
        db.reference('/McDonalds').child(message.from_user.username).update({'Coffee':message.text})
        keyboard = types.ReplyKeyboardMarkup (row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Назад', '0,3 80р', '0,4 95р']])
        msg = bot.send_message(message.chat.id, 'Выберите размер стакана', reply_markup=keyboard)
        bot.register_next_step_handler(msg, Number)
    else:
        McDonalds (message)

def drinksM (message):
    if message.text == '0,4 65р' or '0,5 75р':
        db.reference('/McDonalds').child(message.from_user.username).update({ 'Liter of drinks':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitM)
    elif message.text == '0,47 99р' or '0,6 109р':
        db.reference('/McDonalds').child(message.from_user.username).update({ 'Liter of cocktails':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitM)
    elif message.text == '0,3 99р'or '0,4 109р':
        db.reference('/McDonalds').child(message.from_user.username).update({ 'Liter Cappuccino and Latte':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitM)
    elif message.text == '0,3 80р' or '0,4 95р':
        db.reference('/McDonalds').child(message.from_user.username).update({ 'Liter of coffee':message.text})
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Далее']])
        msg = bot.send_message(message.chat.id, 'Хороший выбор, нажмите ДАЛЕЕ', reply_markup=keyboard)
        bot.register_next_step_handler(msg, dobavitM)

def dobavitM (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in['Да', 'Нет']])
    msg = bot.send_message(message.chat.id, 'Хотите дополнить заказ?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, dobavitM2)

def dobavitM2 (message):
    if message.text == 'Да':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in['Дополнить заказ']])
        msg = bot.send_message(message.chat.id, 'Нажмите кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, McDonalds)
        McDonalds (message)
    elif message.text == 'Нет':
        Number (message)


@bot.message_handler(content_types=['contact'])
def Number (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Нажмите на кнопку отправить номер телефона, и ожидайте звонка. Для повторного заказа нажмите /start" , reply_markup=keyboard)
    db.reference ("/Number").child (message.from_user.username).update({'phone': message.contact.phone_number})




@server.route('/' + config.token, methods=['POST'])
def get_message():
     bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
     return "!", 200

@server.route('/', methods=["GET"])
def index():
     print("hello webhook!")
     bot.remove_webhook()
     bot.set_webhook(url=f"https://{config.appName}.herokuapp.com/{config.token}")
     return "Hello from Heroku!", 200
     
print(f"https://{config.appName}.herokuapp.com/{config.token}")
print(f"PORT: {int(os.environ.get('PORT', 5000))}")
if __name__ == "__main__":
     print("started")
     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

import telebot
from telebot import types

bot = telebot.TeleBot('1812117806:AAH5ycKcbZ6ES7Cj7VVbZ_xy0V0fmjA5CTM')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Пройти наш бесплатный профориентационный тест')
	btn2 = types.KeyboardButton('Узнать о наших услугах и курсах')
	btn3 = types.KeyboardButton('Узнать о наших мероприятиях')
	btn4 = types.KeyboardButton('Узнать какие есть консультации')
	btn5 = types.KeyboardButton('Перейти на нашу страницу в инстаграм')
	btn6 = types.KeyboardButton('Перейти на наш YouTube канал ЦОПП Якутия')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
	send_mess = f"<b>Привет! {message.from_user.first_name} {message.from_user.last_name}</b>!\nЯ чат-бот дирекции карьерной навигации Центра опережающей профессиональной подготовки. " \
                f"\n\nНаша дирекция обучает и помогает по профориентации и самоопределению всех желающих, независимо от возраста, статуса и профессионального направления." \
                f"\nМы проводим разные мероприятия, конкурсы, тренинги, семинары и встречи. А также профориентационные, карьерные консультации. " \
				f"\n\nВыбери снизу, что тебя интересует:"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

    # Назад
	if get_message_bot == "назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Пройти наш бесплатный профориентационный тест')
		btn2 = types.KeyboardButton('Узнать о наших услугах и курсах')
		btn3 = types.KeyboardButton('Узнать о наших мероприятиях')
		btn4 = types.KeyboardButton('Узнать какие есть консультации')
		btn5 = types.KeyboardButton('Перейти на нашу страницу в инстаграм')
		btn6 = types.KeyboardButton('Перейти на наш YouTube канал ЦОПП Якутия')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

		final_message = "Выбери снизу, что тебя интересует:"
	# Тест
	elif get_message_bot == "пройти наш бесплатный профориентационный тест":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Тест на предпочитаемый вид деятельности')
		btn2 = types.KeyboardButton('Тест на профессиональной направленности личности')
		btn3 = types.KeyboardButton('Тест выявление локуса контроля респондентов')
		btn4 = types.KeyboardButton('Методика диагностики ориентаций в карьере')
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Отлично, выбери тест и переходи по ссылке"
	elif get_message_bot == "тест на предпочитаемый вид деятельности" or get_message_bot == "тест на профессиональной направленности личности" or get_message_bot == "тест выявление локуса контроля респондентов" or get_message_bot == "методика диагностики ориентаций в карьере" :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к тесту", url="http://copp-sakha.ru/careertest"))
		final_message = "Переходи по ссылке, чтобы пройти тест"
	# Услуги
	elif get_message_bot == "узнать о наших услугах и курсах":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Наши курсы для школьников')
		btn2 = types.KeyboardButton('Наши курсы для педагогов')
		btn3 = types.KeyboardButton('Наши курсы для всех')
		btn4 = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3, btn4)
		final_message = "Отлично, выбери услугу и переходи по ссылке"
	elif get_message_bot == "наши курсы для школьников" :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к услуге", url="https://project1954784.tilda.ws/dlyshcolnikov"))
		final_message = "Переходи по ссылке, чтобы узнать подробнее"
	elif get_message_bot == "наши курсы для педагогов" :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к услуге", url="https://copp14.ru/pedagogi"))
		final_message = "Переходи по ссылке, чтобы узнать подробнее"
	elif get_message_bot == "наши курсы для всех" :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к услуге", url="https://project1954784.tilda.ws/dlyav"))
		final_message = "Переходи по ссылке, чтобы узнать подробнее"
	# Мероприятия
	elif get_message_bot == "узнать о наших мероприятиях":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Республиканское профориентационное мероприятие "День профессий будущего"')
		btn2 = types.KeyboardButton('Абитуриент 2021: Поступай правильно')
		btn3 = types.KeyboardButton("Назад")
		markup.add(btn1, btn2, btn3)
		final_message = "Отлично, выбери мероприятие и переходи по ссылке"
	elif get_message_bot == 'республиканское профориентационное мероприятие "день профессий будущего"' :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к мероприятию", url="https://copp14.ru/lidovayastranica"))
		final_message = "Переходи по ссылке, чтобы узнать подробнее"
	elif get_message_bot == 'абитуриент 2021: поступай правильно' :
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти к мероприятию", url="http://abiturient.copp-sakha.ru/"))
		final_message = "Переходи по ссылке, чтобы узнать подробнее"
	# Консультации
	elif get_message_bot == "узнать какие есть консультации":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Профориентационная индивидуальная консультация для подростков", url="https://copp14.ru/viborprepodavateliya"))
		final_message = "Отлично, для записи на консультацию перейдите по ссылке"
	# Инстаграм
	elif get_message_bot == "перейти на нашу страницу в инстаграм":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Наша страница", url="https://www.instagram.com/life_n_job/?hl=ru"))
		final_message = "На нашей странице делимся актуальной информацией по мероприятиям, проводим прямые эфиры, конкурсы, розыгрыши и т.д."
	# Ютуб
	elif get_message_bot == "перейти на наш youtube канал цопп якутия":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Наш канал", url="https://www.youtube.com/channel/UCJdINszkIEF8QCnkfUdQ36w/videos"))
		final_message = "Вы найдете много интересных видео по профориентации, образованию, поступлению и так далее."


	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Пройти наш бесплатный профориентационный тест')
		btn2 = types.KeyboardButton('Узнать о наших услугах и курсах')
		btn3 = types.KeyboardButton('Узнать о наших мероприятиях')
		btn4 = types.KeyboardButton('Узнать какие есть консультации')
		btn5 = types.KeyboardButton('Перейти на нашу страницу в инстаграм')
		btn6 = types.KeyboardButton('Перейти на наш YouTube канал ЦОПП Якутия')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
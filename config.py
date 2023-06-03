
file_settings = open('my_token.ini', mode='r', encoding='utf-8')
token = file_settings.read()
file_settings.close()

# MySQL Database
mysql_host = 'localhost'
mysql_db   = 'TelegramSupportBot'
mysql_user = 'SupportBotUser'
mysql_pw   = '123'

# Support Chat (Chat ID)
support_chat = 694846592

# Разное
time_zone           = 'GMT+3'   # Временная зона поддержки - москва
bad_words_toggle    = True      # Enable / disable фильтра плохих слов
spam_toggle         = True      # Enable / disable фильта спама
spam_protection     = 5         # Сколько последовательных сообщений может быть отправлено без ответа от команды
open_ticket_emoji   = 24        # По истечении X часов на странице /tickets появится эмодзи

# Сообщение
text_messages = {
    'start': 'Привет {}, чем мы можем Вам помочь?',
    'faqs': 'Текст часто задаваемых вопросов находится здесь.',
    'support_response': 'От: {}'                  # Support response is being added automatically. {} = refers to the staffs first name.
}

# Регулярки (https://regex101.com/)
regex_filter = {
    'bad_words': r'(?i)^(.*?(\b\w*fuck|shut up|dick|bitch|bastart|cunt|bollocks|bugger|rubbish|wanker|twat|suck|ass|pussy|arsch\w*\b)[^$]*)$'
}

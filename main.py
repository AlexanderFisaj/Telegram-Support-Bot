# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# File Name             : main.py               #
# --------------------------------------------- #

import config
from resources import mysql_handler as mysql
from resources import markups_handler as markup
from resources import msg_handler as msg

import telebot
from datetime import datetime
import arrow

bot = telebot.TeleBot(config.token)

mysql.createTables


# Обработчики обратного вызова
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "faqCallbackdata":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text=config.text_messages['faqs'], parse_mode='Markdown',
                                        disable_web_page_preview=True)


# Команда запуска
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id,
                         config.text_messages['start'].format(message.from_user.first_name) + msg.repo(),
                         parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup.faqButton())
        mysql.start_bot(message.chat.id)
    else:
        bot.reply_to(message, 'Пожалуйста, напишите мне в личку, если вы хотите поговорить со службой поддержки.')


# FAQ Command
@bot.message_handler(commands=['faq'])
def start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, config.text_messages['faqs'], parse_mode='Markdown', disable_web_page_preview=True)
    else:
        pass


# Get All Open Tickets
@bot.message_handler(commands=['tickets', 't'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if not mysql.open_tickets:
            bot.reply_to(message, "ℹ️ Отличная работа, вы ответили на все вопросы!")
            return

        ot_msg = '📨 *Open tickets:*\n\n'
        for user in mysql.open_tickets:
            bot.send_chat_action(message.chat.id, 'typing')
            ot_link = mysql.user_tables(int(user))['open_ticket_link']

            now = arrow.now()
            diff = datetime.now() - mysql.user_tables(int(user))['open_ticket_time']
            diff.total_seconds() / 3600  # seconds to hour
            time_since_secs = float(diff.seconds)
            time_since = now.shift(seconds=-time_since_secs).humanize()

            # Bring attention to 1 day old tickets
            if time_since_secs > config.open_ticket_emoji * 3600:
                alert = ' ↳ ⚠️ '
            else:
                alert = ' ↳ '

            ot_msg += "• [{0}{1}](tg://user?id={2}) (`{2}`)\n{5}_{3}_ [➜ Go to msg]({4})\n".format(
                bot.get_chat(int(user)).first_name,
                ' {0}'.format(bot.get_chat(int(user)).last_name) if bot.get_chat(int(user)).last_name else '',
                int(user), time_since, ot_link, alert)

        bot.send_message(message.chat.id, ot_msg, parse_mode='Markdown')
    else:
        pass


# Close a ticket manually
@bot.message_handler(commands=['close', 'c'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if message.reply_to_message and '(#id' in message.reply_to_message.text:
            bot.send_chat_action(message.chat.id, 'typing')
            user_id = int(message.reply_to_message.text.split('(#id')[1].split(')')[0])
            ticket_status = mysql.user_tables(user_id)['open_ticket']

            if ticket_status == 0:
                bot.reply_to(message, '❌ У этого пользователя нет open ticket...')
            else:
                # Reset Open Tickets as well as the Spamfilter
                mysql.reset_open_ticket(user_id)
                bot.reply_to(message, '✅ Ок, закрыл этот пользовательский тикет!')
        else:
            bot.reply_to(message, 'ℹ️ Вы должны были бы ответить на сообщение')
    else:
        pass


# Get Banned User
@bot.message_handler(commands=['banned'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if not mysql.banned:
            bot.reply_to(message, "ℹ️ Отличная новость, никого не забанили... Еще.")
            return

        ot_msg = '⛔️ *Banned users:*\n\n'
        for user in mysql.banned:
            bot.send_chat_action(message.chat.id, 'typing')
            ot_link = mysql.user_tables(int(user))['open_ticket_link']

            ot_msg += "• [{0}{1}](tg://user?id={2}) (`{2}`)\n[➜ Go to last msg]({3})\n".format(
                bot.get_chat(int(user)).first_name,
                ' {0}'.format(bot.get_chat(int(user)).last_name) if bot.get_chat(int(user)).last_name else '',
                int(user), ot_link)

        bot.send_message(message.chat.id, ot_msg, parse_mode='Markdown')
    else:
        pass


# Ban User
@bot.message_handler(commands=['ban'])
def ot_handler(message):
    try:
        if message.chat.id == config.support_chat:
            if message.reply_to_message and '(#id' in msg.msgCheck(message):
                user_id = msg.getUserID(message)
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    bot.reply_to(message, '❌ Этот пользователь уже забанен...')
                else:
                    mysql.ban_user(user_id)
                    try:
                        # Reset Open Tickets as well as the Spamfilter
                        mysql.reset_open_ticket(user_id)
                    except Exception as e:
                        pass
                    bot.reply_to(message, '✅ Ок, забанили этого пользователя!')

            elif msg.getReferrer(message.text):
                user_id = int(msg.getReferrer(message.text))
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    bot.reply_to(message, '❌ Этот пользователь уже забанен...')
                else:
                    mysql.ban_user(user_id)
                    try:
                        # Reset Open Tickets as well as the Spamfilter
                        mysql.reset_open_ticket(user_id)
                    except Exception as e:
                        pass
                    bot.reply_to(message, '✅ Ок, забанили этого пользователя!')
        else:
            bot.reply_to(message, 'ℹ️ Вам нужно будет либо ответить на сообщение, либо указать `Users ID`.',
                         parse_mode='Markdown')
    except TypeError:
        bot.reply_to(message, '❌ Вы уверены, что я взаимодействовал с этим пользователем ранее...?')


# Un-ban Useer
@bot.message_handler(commands=['unban'])
def ot_handler(message):
    try:
        if message.chat.id == config.support_chat:
            if message.reply_to_message and '(#id' in msg.msgCheck(message):
                user_id = msg.getUserID(message)
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 0:
                    bot.reply_to(message, '❌ Этот пользователь уже не заблокирован...')
                else:
                    mysql.unban_user(user_id)
                    bot.reply_to(message, '✅ Хорошо, снимите бан с этого пользователя!')

            elif msg.getReferrer(message.text):
                user_id = int(msg.getReferrer(message.text))
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 0:
                    bot.reply_to(message, '❌ Этот пользователь уже не заблокирован...')
                else:
                    mysql.unban_user(user_id)
                    bot.reply_to(message, '✅ Хорошо, снимите бан с этого пользователя!')
            else:
                bot.reply_to(message, 'ℹ️ Вам нужно будет либо ответить на сообщение, либо указать `Users ID`.',
                             parse_mode='Markdown')
    except TypeError:
        bot.reply_to(message, '❌ Вы уверены, что я взаимодействовал с этим пользователем ранее...?')


# Message Forward Handler (User - Support)
@bot.message_handler(func=lambda message: message.chat.type == 'private', content_types=['text', 'photo', 'document'])
def echo_all(message):
    while True:
        mysql.start_bot(message.chat.id)
        user_id = message.chat.id
        message = message
        banned = mysql.user_tables(user_id)['banned']
        ticket_status = mysql.user_tables(user_id)['open_ticket']
        ticket_spam = mysql.user_tables(user_id)['open_ticket_spam']

        if banned == 1:
            return
        elif msg.spam_handler_warning(bot, user_id, message):  # Первое предупреждение о спаме
            return
        elif msg.bad_words_handler(bot, message):
            return
        elif msg.spam_handler_blocked(bot, user_id, message):  # Последнее предупреждение о спаме // пользователь больше не может отправлять сообщения
            return
        elif ticket_status == 0:
            mysql.open_ticket(user_id)
            continue
        else:
            msg.fwd_handler(user_id, bot, message)
            return


# Обработчик пересылки сообщений (поддержка - пользователь)
@bot.message_handler(content_types=['text', 'photo', 'document'])
def echo_all(message):
    while True:
        try:
            try:
                user_id = msg.getUserID(message)
                message = message
                text = message.text
                msg_check = msg.msgCheck(message)
                ticket_status = mysql.user_tables(user_id)['open_ticket']
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    # If User is banned - un-ban user and sent message
                    mysql.unban_user(user_id)
                    bot.reply_to(message, 'ℹ️ *К вашему сведению: этот пользователь был забанен.*\n_Разбанен и отправил сообщение!_',
                                 parse_mode='Markdown')

                elif ticket_status == 1:
                    # Reset Open Tickets as well as the Spamfilter
                    mysql.reset_open_ticket(user_id)
                    continue

                else:
                    if message.reply_to_message and '(#id' in msg_check:
                        msg.snd_handler(user_id, bot, message, text)
                        return

            except telebot.apihelper.ApiException:
                bot.reply_to(message, '❌ Я не смог отправить это сообщение...\nПользователь, возможно, заблокировал меня.')
                return

        except Exception as e:
            bot.reply_to(message, '❌ Недопустимая команда!')
            return


print("Запущен бот поддержки Telegram...")
bot.polling()

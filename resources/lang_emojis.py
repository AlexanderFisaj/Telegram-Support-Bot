# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# File Name             : lang_emojis.py        #
# --------------------------------------------- #

def lang_emoji(lang):
    if lang == 'en':
        emoji = '🇺🇸'
    elif lang == 'ru':
        emoji = '🇷🇺'
    else:
        emoji = lang

    return emoji
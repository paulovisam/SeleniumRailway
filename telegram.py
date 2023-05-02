import json
import requests
import os
from dotenv import load_dotenv
import telebot
from datetime import datetime
import socks
import socket


class TelegramBot:
    def __init__(self, demo: bool = False):
        load_dotenv()
        self.demo = demo
        self.token = os.getenv("TOKEN")
        self.chat_id = os.getenv("CHAT_ID")
        self.base_url = f"https://api.telegram.org/bot{self.token}/"
        self.id_last_msg = 0
        self.id_gale = 0
        self.bot = telebot.TeleBot(self.token, parse_mode='Markdown')


    def send_message(self, text: str, reply: int = None):
        try:
            print(text)
            if not self.demo:
                return self.bot.send_message(self.chat_id, text, reply_to_message_id=reply)
            return
        except:
            pass

    def send_message_by_id(self, chat_id, text):
        try:
            if not self.demo:
                return self.bot.send_message(chat_id, text)
            print(text)
        except:
            pass
    
    def delete_menssage(self, message_id):
        try:
            if not self.demo:
                self.bot.delete_message(chat_id=self.chat_id, message_id=message_id)
            return
        except:
            pass
    def tiger(self):
        try:
            text = """🎯 Entre agora\n🐅 Aposte no TIGRE 🟡\n🟢 Proteção no Empate
            """
            result = self.send_message(text)
            if not self.demo:
                self.id_last_msg = result.id
            return result
        except:
            pass
    def dragon(self):
        try:
            text = "🎯 Entre agora\n🐉 Aposte no DRAGÃO 🔴\n🟢 Proteção no Empate"
            result = self.send_message(text)
            if not self.demo:
                self.id_last_msg = result.id
            return result
        except:
            pass

    def green(self, level_gale, tie=False):
        try:
            if tie:
                print('empate true')
                tie_text = 'NO EMPATE 11X'
            else:
                tie_text = ''
            if level_gale < 1:
                text = f"GREEN {tie_text} 🙅🏻‍♂️✅🔥"
            else:
                trophy = "🏆" * (level_gale)
                text = f"GREEN {tie_text} 🙅🏻‍♂️✅ {trophy}"
                self.delete_menssage(self.id_gale)
            result = self.send_message(text, reply=self.id_last_msg)
            if not self.demo:
                self.id_last_msg = result.id
            return result
        except:
            pass
    def red(self, level_gale):
        try:
            text = "❌ RED, NÃO FOI DESSA VEZ 😭"
            result = self.send_message(text, reply=self.id_last_msg)
            for i in range(level_gale):
                self.delete_menssage(self.id_last_msg+i+1)
            if not self.demo:
                self.id_last_msg = result.id
            return result
        except:
            pass  
    def gale(self, level_gale: int):
        try:
            if level_gale >= 1:
                text = f"⚙️ Gale {level_gale}"
                result = self.send_message(text)
                self.id_gale = result.id
            if level_gale > 1:
                self.delete_menssage(result.id-1)
                return result
        except:
            pass
    def consecutive_gains(self, len_gain):
        try:
            text = f"🥇 Estamos a {len_gain} GREENS SEGUIDOS ✅"
            result = self.send_message(text)
            if not self.demo:
                self.id_last_msg = result.id
            return result
        except:
            pass
    def report(self, greens: int, ties: int, reds: int, consecutive: int):
        try:
            hit_rate = round(((greens+ties)/(greens+ties+reds))*100, 2)
            text = f"📄🖊 *RELATORIO ATUAL* 📄🖊\n\n🟢_GREEN_🟢 = {greens}\n🟠_EMPATE_🟠 = {ties}\n🔴_RED_🔴 = {reds}\n\n📈 *Consecutivas* 📈 = {consecutive}\n\n🎯 _Assertividade_ 🎯 = {hit_rate}%"
            result = self.send_message(text)
            return result
        except:
            pass




# tg = TelegramBot()
# tg.dragon()
# tg.report(252,53,17, 12)

# tg.tiger()
# tg.gale(1)
# tg.gale(2)
# tg.gale(3)
# tg.green(3)
# tg.red()


# tg.green(1)
# tg.green(0)
# tg.consecutive_gains(5)

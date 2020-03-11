from tinder_bot import TinderBot

bot = TinderBot()
bot.login()
bot.handle_aferlogin_popups()
bot.autolike()

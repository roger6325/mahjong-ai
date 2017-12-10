import TGBotServer
from telegram.ext import Updater, CommandHandler, ChosenInlineResultHandler, CallbackQueryHandler

HANDLERS = {
	"start": TGBotServer.TGActionHandlers.start,
	"new_game": TGBotServer.TGActionHandlers.new_game
}

INLINE_REPLY_HANDLER = TGBotServer.TGActionHandlers.inline_reply_handler

updater = Updater(token = TGBotServer.get_tg_bot_token())
for command, handler in HANDLERS.items():
	updater.dispatcher.add_handler(CommandHandler(command, handler))
updater.dispatcher.add_handler(CallbackQueryHandler(INLINE_REPLY_HANDLER))
updater.start_polling()
updater.idle()
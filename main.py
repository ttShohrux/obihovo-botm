from telegram.ext import Updater,CommandHandler, MessageHandler,ConversationHandler,Filters
from funksiya import *
updater = Updater(token = '5026402674:AAGQkWmRo2wE-s5lHiVfVkmELSweeIX25iE')


distpatcher = updater.dispatcher


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        1:[MessageHandler(Filters.regex("^Namangan👈$"), namangan),
           MessageHandler(Filters.regex("^Toshkent👈$"), toshkent),
           MessageHandler(Filters.regex("Toshkent viloyati👈"),toshkentvil),
           MessageHandler(Filters.regex("^Buxoro👈$"), buxoro),
           MessageHandler(Filters.regex("^Sirdaryo👈$"), srdaryo),
           MessageHandler(Filters.regex("^Jizah👈$"), jizax),
           MessageHandler(Filters.regex("^Samarqand👈$"), samarqand),
           MessageHandler(Filters.regex("^Farg'ona👈$"), fargona),
           MessageHandler(Filters.regex("^Andijon👈$"), andijon),
           MessageHandler(Filters.regex("^Qashqidaryo👈$"), qashqadaryo),
           MessageHandler(Filters.regex("^Surhandaryo👈$"), surxandaryo),
           MessageHandler(Filters.regex("^Xorazim👈$"), xorazm),
           MessageHandler(Filters.regex("^Qoraqalpog'ston👈$"), qoraqalpogistan),
           MessageHandler(Filters.regex("^Navoyi👈$"), navoi),


]
        },
    fallbacks=[MessageHandler(Filters.text, start)]

)
distpatcher.add_handler(conv_handler)

updater.start_polling()

print("ok bot ishlavoti")

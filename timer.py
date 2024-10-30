import os
import time
import threading
from plyer import notification
from pynput import keyboard
from tabdil import tabdil

# حالت انتخاب
faal = 1
startCountDown = False
stopTimer = False

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

# تابع برای متوقف کردن شمارش معکوس با فشردن کلید Enter
def on_press2(key):
    global startCountDown
    global stopTimer
    if key == keyboard.Key.enter:
        startCountDown = False
        stopTimer = False
        return False

# تابع تایمر
def run_timer():
    input()
    global stopTimer
    getThings = input("how many seconds you want this timer work (e.g., 10 s, 1 m, 2 h): ")
    getThingsTrue = getThings.split(" ")
    timer = 0
    stopTimer = True
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
    listener_thread = threading.Thread(target=start_countdown_listener)
    listener_thread.start()
    if timer >= 0:
        while timer >= 0 and stopTimer == True:
            tabdil(timer)
            time.sleep(1)
            os.system("clear")
            timer -= 1

        if timer < 0:
            notification.notify(
                title='Timer Finished',
                message='Your time is up!',
                app_name='Timer App',
                timeout=10
            )
    else:
        print("Invalid time format.")

# تابع شمارش معکوس
def run_countdown():
    global startCountDown
    countdown = 0
    startCountDown = True

    # شروع لیسنر در یک ترد جداگانه
    listener_thread = threading.Thread(target=start_countdown_listener)
    listener_thread.start()

    # حلقه شمارش معکوس
    while startCountDown:
        print("your countdown: ", end="")
        tabdil(countdown)
        print("\nfor exit clik the Enter")
        countdown += 1
        time.sleep(1)
        os.system("clear")
    print("Your CountDown End With: ", end="")
    tabdil(countdown)

# تابع برای لیسنر شمارش معکوس
def start_countdown_listener():
    with keyboard.Listener(on_press=on_press2) as listener2:
        listener2.join()

# نمایش منو اولیه و شروع لیسنر منو
display_menu()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# شروع برنامه تایمر یا شمارش معکوس بر اساس انتخاب
if faal == 1:
    run_timer()
elif faal == 2:
    run_countdown()
    input()
    input()

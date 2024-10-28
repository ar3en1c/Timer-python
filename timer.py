import os
import time
os.system(
    """
if ! pip show plyer >/dev/null 2>&1; then
  pip install plyer
fi
"""
)
from plyer import notification
from tabdil import tabdil
try:
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
        # Send notification when time is up
        notification.notify(
            title='Timer Finished',
            message='Your time is up!',
            app_name='Timer App',
            timeout=10  # Notification will stay for 10 seconds
        )
    else:
        print("Invalid time format.")
except:
    print("\nThank you For Using This Application\n")
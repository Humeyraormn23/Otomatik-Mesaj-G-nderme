import pywhatkit
import datetime
import time

to_number = "+number"
send_time = ("07:00")
msg = ("AUTOMATED MESSAGE")

send_time_hour = int(send_time.split(":")[0])
send_time_minute = int(send_time.split(":")[1])

send_time_ = datetime.datetime.now().replace(hour=send_time_hour, minute=send_time_minute, second=0, microsecond=0)

if send_time_ < datetime.datetime.now():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    send_time_ = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour, send_time_minute))

later_1min = send_time_ + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    if now.hour == send_time_hour and now.minute == send_time_minute and now.day == send_time_.day:
        pywhatkit.sendwhatmsg(to_number, msg, send_time_hour, send_time_minute + 1)
        print(f"mesaj gönderildi - {now}")

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        send_time_ = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour, send_time_minute))
    later_1min = send_time_ + datetime.timedelta(minutes=1)

    time.sleep(5)

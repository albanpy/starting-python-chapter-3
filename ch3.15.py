#Time Calculator
sec=int(input("Enter Number of Seconds:"))
#1 minute=60 seconds, 1 hour=3600 seconds and 1 day=86400 seconds
#convert the number of seconds to minutes and seconds.
if sec>=60 and sec<3600:
    mins=sec//60
    ss=sec%60
    print(f'Time 00:{mins}:{ss}')
#convert the number of seconds to hours, minutes, and seconds
elif sec>=3600 and sec<86400:
    hour=sec//3600
    minh=(sec%3600)//60
    ssh=(sec%3600)%60
    print(f'Time {hour}:{minh}:{ssh}')
    #convert the number of seconds to days, hours, minutes, and seconds.
elif sec>=86400:
    day=sec//86400
    hourd=(sec%86400)//3600
    mind=((sec%86400)%3600)//60
    ssd=((sec%86400)%3600)%60
    print(f'{day} days:Time {hourd}:{mind}:{ssd}')
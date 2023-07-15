import re

def solution(s):
    hour = s[0:2]
    if s[-2:] == 'AM':
        if int(hour) == 12:
            s = s.replace(hour, '00')
            print(s)
        else:
            print(s)
    else:
        if hour[0] == 0:
            int_hour = int(hour[1])
            int_hour = int_hour + 12
            s = s.replace(hour, str(int_hour))
            print(s)
        elif int(hour) >= 12:
            print(s)
        else :
            s = s.replace(hour, str(int(hour)+ 12))
            print(s)
        
         

solution('09:01:21PM')


#Create a class Time with private attributes hour, minute and second. Overload '+' operator to find sum of 2 time.

class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        sec = self.__second + other.__second
        min = self.__minute + other.__minute 
        hr = self.__hour + other.__hour

        min += sec // 60
        sec = sec % 60

        hr += min // 60
        min = min % 60

        return Time(hr, min, sec)

    def display(self):
        print(f"Time: {self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

t1 = Time(2, 45, 50)
t2 = Time(4, 20, 30)
t3 = t1 + t2
t3.display()   

def convert(seconds):
    seconds=seconds%(24*3600)
    hours = seconds//3600
    seconds %= 3600
    minutes = seconds//60
    seconds%= 60

    return "%d:%02d:%02d" % (hours,minutes,seconds)

n = int(input("enter number of seconds :"))
print(convert(n))

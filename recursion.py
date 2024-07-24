def countdown(num):
    print(str(num) + "...")
    if (num <= 1):
        return
    else:
        countdown(num-1)

countdown(3)
    
def ft_water_reminder():
    print("Days since last watering: ", end="")
    num_days = int(input())
    if num_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

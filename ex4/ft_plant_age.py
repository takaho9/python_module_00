def ft_plant_age():
    print("Enter plant age in days: ", end="")
    num_days = int(input())
    if num_days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

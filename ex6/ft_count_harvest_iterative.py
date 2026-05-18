def ft_count_harvest_iterative():
    print("Days until harvest: ", end="")
    num_days = int(input())
    for i in range(1, num_days + 1):
        print(f"Day {i}")
    print("Harvest time!")

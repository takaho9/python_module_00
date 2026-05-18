def ft_harvest_total():
    total = 0
    for i in [1, 2, 3]:
        print(f"Day {i} harvest: ", end="")
        total += int(input())
    print(f"Total harvest: {total}")

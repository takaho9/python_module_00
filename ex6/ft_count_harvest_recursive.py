def ft_count_harvest_recursive():
    def helper(start: int, end: int) -> None:
        print(f"Day {start}")
        if start < end:
            helper(start + 1, end)
    print("Days until harvest: ", end="")
    num_days = int(input())
    helper(1, num_days)
    print("Harvest time!")

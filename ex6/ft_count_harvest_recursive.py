def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_days(n: int) -> None:
        if n <= 0:
            return
        count_days(n - 1)
        print("Day", n)

    count_days(days)
    print("Harvest time!")


ft_count_harvest_recursive()

def vacuum_cleaner(location, status):
    if status[location] == "dirty":
        print(f"Cleaning {location}")
        status[location] = "clean"
    if location == "A":
        print("Moving to B")
        location = "B"
    else:
        print("Moving to A")
        location = "A"
    if status[location] == "dirty":
        print(f"Cleaning {location}")
        status[location] = "clean"
    print("Final status:", status)
status = {"A": "dirty", "B": "dirty"}
vacuum_cleaner("A", status)

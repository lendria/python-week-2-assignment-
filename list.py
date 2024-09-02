def manipulate_list():
    # Step 1: Create an empty list
    my_list = []

    # Step 2: Append elements
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    print(f"After appending: {my_list}")

    # Step 3: Insert a value
    my_list.insert(1, 15)

    print(f"After inserting 15: {my_list}")

    # Step 4: Extend the list
    my_list.extend([50, 60, 70])

    print(f"After extending: {my_list}")

    # Step 5: Remove the last element
    my_list.pop()

    print(f"After removing the last element: {my_list}")

    # Step 6: Sort the list
    my_list.sort()

    print(f"After sorting: {my_list}")

    # Step 7: Find and print the index of 30
    index_of_30 = my_list.index(30)
    print(f"The index of 30 is: {index_of_30}")

manipulate_list()

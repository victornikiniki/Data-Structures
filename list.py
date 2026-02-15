inventory_items = [5, 6, 7, 3, 6, 2, 6, 3, 6, 7, 7]

inventory_items[3] = 4
inventory_items[-1] = 8
inventory_items[2] = 2

# print(inventory_items)

types_of_items = len(inventory_items)
# print(types_of_items)

total_items = 0

for i in inventory_items:
    total_items += i

# print(total_items)

average_number_of_items_per_type = total_items / types_of_items
print(f"the average number of items per type is {average_number_of_items_per_type:.2f}")
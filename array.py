games = ['god of war', 'spiderman', 'valorant', 'silent hill', 'silent hill f']
# item = str(input("enter a game: "))

# index_game = games.index(item)
# print(index_game)

def search_item(lst, element): 
    for element in lst: 
        if element == lst: 
            print(lst[element])

# sorted_list= sorted(games)
# print(sorted_list)

# search_item(games, item)

classroom = [('valorant', 1), ('gta 5', 2), ('black myth wukong', 4), ('red dead redemption 2', 3)]
# print(sorted(classroom, key=lambda x: x[1], reverse=True))

lst = [1, 2, 3, 4]


def find_second_smallest_int(lst):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in lst: 
        if i < smallest: 
            second_smallest = smallest
            smallest = i
        elif smallest < i < second_smallest: 
            second_smallest = i
    if second_smallest == float('inf'): 
        return None
    return second_smallest

print(find_second_smallest_int(lst))
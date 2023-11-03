def find_item_index(item_list, item):
    if item in item_list:
        return item_list.index(item)
    else:
        return None


items = ["Товар 1", "Товар 2", "Товар 3", "Товар 2", "Товар 4"]
search_item = "Товар 2"

index = find_item_index(items, search_item)
print(index)
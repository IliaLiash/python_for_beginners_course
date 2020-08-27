def merge(list1, list2):
    my_list = list1 + list2
    return sorted(my_list)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

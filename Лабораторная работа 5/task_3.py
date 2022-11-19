from random import randint, sample
def get_unique_list_numbers() -> list[int]:
    list_ = list()
    collection = list(range(-10, 10))
    '''while len(list_) < 15:
        num = randint(0, len(collection)-1)
        list_.append(collection[num])
        collection.pop(num)'''
    list_ = sample(collection, 15)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


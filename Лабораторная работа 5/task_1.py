from pprint import pprint
def trans(num: int) -> dict:
    return {'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)}
my_dict = [trans(num) for num in range(16)]
pprint(my_dict)
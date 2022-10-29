def get_count_char(str_):
    dic = dict()
    str_ = str_.lower()
    for i in str_:
        if i.isalpha():
            dic[i] = dic.get(i, 0) + 1
    return dic


def second(dic):
    for i, value in dic.items():
        dic[i] = int(round(value/sum(dic.values()), 3)*1000)/10
    return dic
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(second(get_count_char(main_str)))

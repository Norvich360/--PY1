src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = not False and True or False and False # избавляемся от отрицания
# result = not False and True or False # избавляемся от логического "и"
# result = not False and True # избавляемся от логическоо "или"
# result = not False # избавляемся от логического "и"
# result = True # избавляемся от отрицания
result = True  # TODO подставить результат выражения

print(src == result)

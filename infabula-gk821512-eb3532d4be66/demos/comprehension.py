items = [[1, 2, 3],
         [4, 5, 6]]

mixed = (num for item in items for num in item)

dict_items = [{'numbers': item} for item in items]

double = [ for d in dict_items for num in d['numbers']  ]


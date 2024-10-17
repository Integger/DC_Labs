# TODO Найдите количество книг, которое можно разместить на дискете

capacity = 1.44 * 1024 * 1024
lists_per_book = 100
strings_per_list = 50
characters_per_string = 25
char_bytes_size = 4

bytes_per_book = lists_per_book * strings_per_list * characters_per_string * char_bytes_size

result = int(capacity) // bytes_per_book

print("Количество книг, помещающихся на дискету:", result)

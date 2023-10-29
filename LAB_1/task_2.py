capasity_disk = 1.44 * 1024 * 1024
pages_book = 100
line_page = 50
symbols_line = 24
safe_symbol = 4

count_books = capasity_disk / (pages_book * line_page * symbols_line * safe_symbol)
print("Количество книг, помещающихся на дискету:", round(count_books))

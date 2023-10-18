# TODO Найдите количество книг, которое можно разместить на дискете
count_pages=100
count_str=50
count_char=25
total_memory= 1.44*1024*1024    #Мб перевожу в байты
memory_char=4 #байт на один символ
memory_str=count_char*memory_char #байт на одну строку
memory_page=count_str*memory_str #байт на одну страницу
memory_book=memory_page*count_pages
count_book=total_memory//memory_book
print("Количество книг, помещающихся на дискету:", int(count_book))

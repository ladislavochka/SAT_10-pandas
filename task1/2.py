import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', None)

book = ["1984", "Лісова пісня", "Кайдашева сім'я",
        "Гаррі Поттер і філософський камінь", "Володар перснів"]
author = ["Джордж Оруелл", "Леся Українка", "Іван Нечуй-Левицький",
          "Дж. К. Роулінг", "Дж. Р. Р. Толкін"]
year = [1949, 1911, 1879, 1997, 1954]
genre = ["Антиутопія", "Драма", "Реалізм", "Фентезі", "Фентезі"]
df = pd.DataFrame({
    "Book" : book,
    "Author" : author,
    "Year" : year,
    "Genre" : genre
})
print(df)



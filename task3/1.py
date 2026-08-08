import pandas as pd

df = pd.read_csv('GoogleApps.csv')
# Як називається програма, розташована першим у наборі даних?
first_name = df.iloc[0]['App']
print(first_name)
# До якої категорії відноситься додаток, розташований останнім у наборі даних?
last_app_category = df.iloc[-1]['Category']
print(last_app_category)
# Скільки стовпців міститься у наборі даних?
# Дані якого типу зберігаються у кожному зі стовпців?
num_columns = df.shape[1]
print(num_columns)
# Вкажи середнє арифметичне та медіану розміру додатків (Size)
# Скільки коштує найдорожчий додаток?
# *Вкажи середнє арифметичне та медіану кількості установок додатків (Installs)
df['Size'] = pd.to_numeric(df['Size'], errors = 'coerce')
mean_size = round(df["Size"].mean(), 2)
median_size = int(df["Size"].median())
print(mean_size)
print(median_size)
df['Price'] = pd.to_numeric(df['Price'], errors = 'coerce')
max_price = int(df["Price"].max())
print(max_price)

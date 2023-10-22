import random
from random import randint


random_number = random.randint(1, 10)


print('Случайное число:', random_number)


fruits = ['Банан', 'Мандарин', 'Ананас', 'Груша', 'Арбуз']
to_buy = random.choice(fruits)
print(f'Сегодня я куплю {to_buy}')

to_buy_tomorrow = random.sample(fruits, k=3)
print('А завтра куплю', ', '.join(to_buy_tomorrow))
random.shuffle(to_buy_tomorrow)
print(', '.join(to_buy_tomorrow))
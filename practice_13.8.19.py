count_tickets = int(input("Укажите количество билетов : "))
price_tickets = 0
for i in range(count_tickets):
    age = int(input("Укажите ваш возраст : "))
    i += 1
    if age < 18:
        print("Билет бесплатно")
    elif age >= 18 and age <= 25:
        price_tickets += 990
        print("Стоимость билета : 990")
    elif age > 25:
        price_tickets += 1390
        print("Стоимость билета : 1390")
if count_tickets > 3:
        price_tickets = price_tickets * 0.9
        print("Сумма к оплате с учетом скидки :", price_tickets)
else:
    print("Сумма к оплате :", price_tickets)
print("Добро пожаловать на онлайн-конференцию !")


salary = float(input("Введите зарплату за месяц: "))
credit_payment = float(input("Введите сумму платежа по кредиту: "))
utilities = float(input("Введите задолженность за коммунальные услуги: "))

remainder = salary - credit_payment - utilities

print(f"\nПосле всех выплат у вас останется: {remainder:.2f} рублей")
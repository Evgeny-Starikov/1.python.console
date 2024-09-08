# Задача 3.

salary = int(input('Введите заработную плату в месяц: '));
mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '));
spendingOnLife = int(input('Введите, какой процент(%) уходит на жизнь: '));

yearMortgage = salary * mortgage / 100 * 12;
yearSpendingOnLife = salary * spendingOnLife / 100 * 12;
annualSavings = salary * 12 - yearMortgage - yearSpendingOnLife;

print('На ипотеку было потрачено: ', yearMortgage, 'рублей');
print('Было накоплено: ',  annualSavings, 'рублей');


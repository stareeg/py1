#1 пункт
age = 20
sex = 'M'
print (age, sex)
age1 = int(input("Введите возраст"))
print (age1)

#2 пункт
seconds = int(input ("Введите количество секунд: "))
hour1 = seconds / 3600
min1 = (60*hour1) % 60
sec1 = (3600*min1) % 60
print ("%d %d %d" % (hour1, min1, sec1))

#3 пункт
n = int(input ("Введите число n: "))
num = str(n)
num1 = num+num
num2 = num+num+num
sum = n + int(num1) + int(num2)
print ("Сумма: ", sum)

#4 пункт
f = int(input ("Введите целое положительное число: "))
m = f%10
f = f//10
while f > 0:
    if f%10 > m:
        m = f%10
    f = f // 10
print (m)

#5 пункт
income = float(input ("Введите выручку"))
costs = float(input ("Введите издержки"))
if income > costs:
    print ("Ваша фирма работает в прибыль")
else:
    print ("Ваша фирма работает в убыток")
efficiency: float = income / costs
print ("Рентабельность: ", efficiency)
employees = int(input("Введите кол-во сотрудников: "))
payment = income / employees
print ("Прибыль фирмы в расчете на сотрудника: ", payment)

#6 пункт
a = float(input("Введите кол-во километров первого дня: "))
b = float(input("Введите целевое кол-во километров: "))
i = 1
while a<b:
    a = a + a*0.1
    i += 1
print("Кол-во дней: ", i)
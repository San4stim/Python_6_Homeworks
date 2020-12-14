x = [10, 20, 50, 100, 200, 500, 1000]
q1, q2, q3, q4, q5, q6, q7, q8 = 0, 0, 0, 0, 0, 0, 0, 0
print("How much money is needed?")
sum = int(input())
sum1 = sum%500 
sum2 = sum-sum1
if sum%10==0:
	while sum2>=100:
		q4 +=1
		sum2 -= 100
	print('Количество банкнот: ', q4, '\n', 'Номинал: ', x[3])
	while sum2>=200:
		q5 +=1
		sum2 -= 200
	print('Количество банкнот: ', q5, '\n', 'Номинал: ', x[4])
	while sum2>=500:
		q6 +=1
		sum2 -= 500
	print('Количество банкнот: ', q6, '\n', 'Номинал: ', x[5])
	while sum2>=1000:
		q7 +=1
		sum2 -= 1000
	print('Количество банкнот: ', q7, '\n', 'Номинал: ', x[6])
	while sum1 >= 10 and q1<10:
		q1 +=1
		sum1 -= 10
		if sum%20!=0 and q1==9: break
	print('Количество банкнот: ', q1, '\n',  'Номинал: ', x[0])
	while sum1 >= 20 and q2<10:
		q2 +=1
		sum1 -= 20
	print('Количество банкнот: ', q2, '\n',  'Номинал: ', x[1])
	while sum1 >= 50 and q3<10:
		q3 +=1
		sum1 -= 50
	print('Количество банкнот: ', q3, '\n',  'Номинал: ', x[2])
else:
	print('Введите сумму кратную 10 грн!')

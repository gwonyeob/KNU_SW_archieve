#1번 문제
num_list = []
sum=0
x=int(input('x를 입력하세요 >> '))
for i in range(1,x+1):
    num_list.append(i)
special_num_list = [] #4의 배수가 아닌 수를 저장할 리스트 생성
for num in num_list:
    if num % 4 != 0:
        special_num_list.append(num)
        sum+=num
print(special_num_list)
print(sum)
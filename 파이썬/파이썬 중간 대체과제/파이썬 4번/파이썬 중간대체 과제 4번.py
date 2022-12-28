import sys
max=int(input("생성할 큐의 크기를 설정해주세요 >> "))
queque=[]
while True:
    x=0
    command = input("명령을 입력하세요 >> ").split(" ")
    def data_In(x):
        y=0
        y=len(queque)
        if(y<max):
            queque.append(command[1])
            print("현재 큐 현황: ", end="")
            print(queque)
        else:
            print("오버플로우입니다!!! 큐가 꽉 찼습니다!")
    def data_pop():
        z=len(queque)
        if z==0:
            print("언더플로우입니다! 큐가 없습니다!!!")
        else:
            print("현재 큐 현황: ", end="")
            print(queque)
            print("출력된 데이터", z)
    if command[0] == "입력":
        data_In(x)
    elif command[0] == "출력":
        data_pop()
    elif command[0] == "exit":
        break
    else:
        print("잘못된 입력입니다")



    

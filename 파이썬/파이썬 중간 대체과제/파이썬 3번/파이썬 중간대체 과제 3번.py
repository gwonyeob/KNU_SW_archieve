import sys
command = input("명령을 입력하세요 >> ").split(", ")
now=[0,0]

def Current_position(command):
    for i in range(len(command)):
        if(command[i][0]) == 'U':
            now[1]+=int(command[i][1:])
        elif(command[i][0]) == 'D':
            now[1]-=int(command[i][1:])
        elif(command[i][0]) == 'L':
            now[0]-=int(command[i][1:])
        elif(command[i][0]) == 'R':
            now[0]+=int(command[i][1:])
        else:
            print("알 수 없는 명령이 존재합니다.")
            sys.exit()
Current_position(command)
print("로봇의 좌표는 현재: ", end="")
print(now, end="")
print(" 입니다")



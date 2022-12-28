global Boolean
class Air:
    def Control_Boolean(self):
        Boolean=input('전원 On/Off 중에 골라주세요: ')
        self.Boolean=Boolean

    def power(self):
        if  self.Boolean== '전원 On':
            self.Boolean=True
            return self.Boolean

        elif self.Boolean == '전원 Off':
            self.Boolean=False
            return self.Boolean

    def Control_Temp(self):
        self.temp=int(input('온도를 입력하세요: '))

    def up(self):
        self.temp+=1
        print(self.temp)

    def down(self):
        self.temp-=1
        print(self.temp)

    def re(self):
        temp=self.temp
        return temp

    def present(self):
        print('현재 온도는 {}도입니다'.format(self.temp))

a = Air()
while True:

    print('에어컨 리모콘 기본 설정입니다' +'\n')
    print('1. 전원 on/off'+ '\n')
    print('2. 온도 입력'+ '\n')
    print('3. 온도 증가'+ '\n')
    print('4. 온도 감소'+ '\n')
    print('5. 온도 반환'+ '\n')
    print('6. 현재 온도'+ '\n')

    num=int(input('원하는 기능을 선택하세요: '))

    if num==1:
        a.Control_Boolean()
        power=a.power()

    elif num==2:
        if power == True:
            a.Control_Temp()
        else:
            print('전원이 꺼져있습니다')

    elif num==3:
        if power == True:
            a.up()
        else:
            print('전원이 꺼져있습니다')

    elif num==4:
        if power == True:
            a.down()
        else:
            print('전원이 꺼져있습니다')

    elif num==5:
        if power == True:
            power=a.re()
            print(power)
        else:
            print('전원이 꺼져있습니다')

    elif num==6:
        if power == True:
            a.present()
        else:
            print('전원이 꺼져있습니다')
        







1
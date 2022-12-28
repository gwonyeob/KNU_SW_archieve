class Author:
    def get_name(self,name):
        self.name=name
    def get_email(self, email):
        for i in range(len(email)):
            global count
            count=0
            if(email[i]=='@'):
                self.email=email
                count+=1
                break
            else:
                continue
        if count==0:
            print('잘못된 입력입니다 강제종료합니다')
            exit()
    def set_email(self, email):
        self.email=email
    def get_gender(self, gender):
        if(gender == 'm' or 'f'):
            self.gender=gender
        else:
            gender='u'
            self.gender=gender
    def print(self):
        print('{0} {1} at {2}'.format(self.name, self.gender, self.email))
a=Author()
a.get_name('나권엽')
a.get_email('peter261104@naver.com')
a.get_gender('m')
a.print()

class Book(Author): 
    def __init__(self, name, price, QtyInStock):
        self.name=name
        self.price=price
        self.QtyInStock=QtyInStock
    def get_name(self, name):
        self.name=name
    def get_Author(self):
        a.print()
    def get_price(self, price):
        self.price=price
    def set_price(self):
        return self.price
    def get_QtyInStock(self, QtyInStock):
        self.QtyInStock=QtyInStock
    def set_QtyInStock(self):
        return self.QtyInStock
    def print(self):
        print(f"책 이름: {self.name}, 가격: {self.price}, 판매부수: {self.QtyInStock}")
b=Book(name='다람쥐 요들레이', price=10000, QtyInStock=1234567)
b.print()
b.get_Author()




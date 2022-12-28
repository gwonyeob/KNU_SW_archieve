import numpy as np
from numpy import dot
from numpy.linalg import norm

list=[]
compare_list=[]
recall_list=[]
obtion=0
compared= ''

class Music:
    def set_Title(self):
        title=input('노래 제목을 입력하세요: ')
        self.title = title

    def set_Artist(self):
        artist=input('아티스트 이름을 입력하세요: ')
        self.artist = artist

    def set_Genre(self):
        try:
            genre=input('장르를 입력하세요: ')
            if genre != '발라드' or '댄스' or '힙합' or '록' or '트로트':
                raise Exception('지원하지 않는 장르입니다')
            self.genre = genre
        except Exception as e:
            print('예외가 발생했습니다.', e)

    def set_Language(self):
        try:
            language=input('언어를 입력하세요: ')
            if language != '한국어' or '영어' or '일본어':
                raise Exception()
            self.language=language
        except Exception as e:
            print('예외가 발생했습니다', e)

    def save(self):
        list=[]
        list.append(self.title)
        list.append(self.genre)
        list.append(self.artist)
        list.append(self.language)
        with open("D:\파이썬 기말고사\music.dat", mode='a') as file:
            file.write('\n{}, {}, {}, {}'.format(list[0], list[1], list[2], list[3]))
            file.close()

    def recall(self):
        print('음원 조회를 시작합니다'+'\n')
        print('1. 음원 제목' + '\n')
        print('2. 음원 장르' + '\n')
        print('3. 음원 아티스트' + '\n')
        print('4. 음원 언어' + '\n')
        obtion=int(input('조회할 음원의 옵션을 선택해주세요: '))
        if obtion == 1:
            compared=input('조회할 음원 제목을 입력하세요: ')
        elif obtion == 2:
            compared=input('조회할 음원 장르를 입력하세요: ')
        elif obtion == 3:
            compared=input('조회할 음원 아티스트를 입력하세요: ')
        elif obtion == 4:
            compared=input('조회할 음원 언어를 입력하세요: ')
        else:
            print('잘못된 입력입니다')

        with open("D:\파이썬 기말고사\music.dat", mode='r', encoding='UTF-8') as file:
            while True:
                line=file.readline()
                print(line)
                if not line:
                    break
                list.append(line.strip())
            file.close()

        for i in range(len(list)):
            compare=list[i]
            compare_list = compare.split(', ')
            if compare_list[obtion-1] == compared:
                print(compare_list)

    def input(self):
        print('수정할 음원의 정보를 입력하세요' + '\n')
        m.set_Title()
        m.set_Genre()
        m.set_Artist()
        m.set_Language()
        list=[]
        list.append(self.title)
        list.append(self.genre)
        list.append(self.artist)
        list.append(self.language)
        compare=(', '.join(list))
        self.compare=compare

    def input_re(self):
        print('\n')
        print('수정 정보를 입력하세요' +'\n')
        m.set_Title()
        m.set_Genre()
        m.set_Artist()
        m.set_Language()
        modify_list=[]
        modify_list.append(self.title)
        modify_list.append(self.genre)
        modify_list.append(self.artist)
        modify_list.append(self.language)
        modified=(', '.join(modify_list))
        self.modified=modified

    def modify(self):
        with open("D:\파이썬 기말고사\music.dat", mode='r') as file:
            lines = file.readlines() 
        with open("D:\파이썬 기말고사\music.dat", mode='w') as file:
            for line in lines:
                if line.strip("\n") != self.compare:
                    file.write(line)
                else:
                    file.write(self.modified)
                    file.write('\n')

    def delate(self):
        list=[]
        list.append(self.title)
        list.append(self.genre)
        list.append(self.artist)
        list.append(self.language)
        compare=(', '.join(list))
        with open("D:\파이썬 기말고사\music.dat", mode='r') as file:
            lines = file.readlines() 
        with open("D:\파이썬 기말고사\music.dat", mode='w') as file:
            for line in lines:
                if line.strip("\n") != compare:
                    file.write(line)
    def cosine(self):
        list_h=[]
        with open("D:\파이썬 기말고사\history.dat", encoding= 'UTF-8',mode='r') as file:
            while True:
                line=file.readline()
                if not line:
                    break
                list_h.append(line.strip())
            file.close()
        h_list=[]
        hh_list=[]
        for i in range(len(list_h)):
            h_list=list_h[i].split(', ')
            h_list.pop(0)
            hh_list.append(h_list)
        print(hh_list)

        with open("D:\파이썬 기말고사\music.dat", mode='r') as file:
            while True:
                line=file.readline()
                if not line:
                    break
                list.append(line.strip())
            file.close()
        dat_list=[]
        for i in range(len(list)):
            dat_list=list[i].split(', ')
            dat_list.pop(0)
            print(dat_list)
        file.close()


    
while True:
    m=Music()
    print('1. 음원 저장' + '\n')
    print('2. 음원 조회' + '\n')
    print('3. 음원 수정' + '\n')
    print('4. 음원 삭제' + '\n')
    print('5. 음원 추천' + '\n')
    num=int(input('원하는 기능을 선택하세요: '))

    if num == 1:
        print('음원 저장을 시작합니다'+ '\n')
        m.set_Title()
        m.set_Genre()
        m.set_Artist()
        m.set_Language()
        m.save()

    elif num == 2:
        m.recall()

    elif num == 3:
        print('음원 수정을 시작합니다' +'\n')
        m.input()
        m.input_re()
        m.modify()
        
    elif num == 4:
        print('삭제할 음원의 정보를 입력하세요' + '\n')
        m.set_Title()
        m.set_Genre()
        m.set_Artist()
        m.set_Language()
        m.delate()
        print('음원이 삭제되었습니다')
    elif num == 5:
        m.cosine()
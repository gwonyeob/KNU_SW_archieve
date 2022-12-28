import sys
def atbash(message):
    translated= ""
    for ch in message:
        if ch >='a' and ch<='z':
            translated=translated+chr(219-ord(ch))
        elif ch>='A' and ch<='Z':
            translated=translated+chr(155-ord(ch))
        elif ch>='0' and ch<='9':
            translated=translated+chr(105-ord(ch))
        else:
            print("입력은 알파벳과 숫자로만 입력하세요!!!")
            sys.exit()
    return translated
text=list(map(str, input("평문을 입력하세요 >> ")))
cipher=atbash(text)
print("암호화된 문장은 >> ", end="")
print(cipher)
print("입니다!")
        


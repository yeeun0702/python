Dic={}

while True:
    Dic={}
    key = int(input("정수 key : "))
    value = (input("문자 value: "))
    if(key == 0) or (value == "문자열 종료"):
        Dic[key] = value
        print("그만")
        print(Dic)
        break

print(list(Dic.keys()))
print(list(Dic.values()))
print(list(Dic.items()))



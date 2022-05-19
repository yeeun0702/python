List=[]
for x in range(0,15):
    x=int(input("정수를 입력하시오 : "))
    List.append(x)
    if x==15:
        print(List)

for x in List[:]:
    if x % 2 == 0:
        List.remove(x)
print(List) # 2의 배수 제거

for x in List[:]:
    if x % 3 == 0:
        List.remove(x)
print(List) # 3의 배수 제거


print(List.pop(0)) # 1을 빼내기

List.insert(4,2)
List.insert(5,3)
print(List) # 2랑 3을 다섯번째, 여섯번째 자리에 넣기

List.sort()
print(List) # 내림차순 정렬
class Student: # 파이썬에서 클래쓰란 객체를 찍어내는 틀
    def __init__(self,name,grade,student_number,sex,address,phone_number,year): #__init__ 함수는 초기화를 자동으로 시켜주는 메소드
            self.name = name #객체에 초깃값 설정을 위해 생성자 구현 . 첫번째 매개변수인 self는 매소드를 호출한 객체가 자동으로 전달되게 함.
            self.grade =grade
            self.student_number = student_number
            self.sex = sex
            self.address = address
            self.phone_number = phone_number
            self.year = year

    def introduce(self): # 클래쓰 안에 메소드 명을 introduce로 지정
        print("이름은 %s 이다" %self.name) # 저장된 데이터와 맞는 포멧코드 사용
        print("학년은 %d 이다" %self.grade)
        print("학번은 %d 학년이다" %self.student_number)
        print("성별은 %s 이다" %self.sex)
        print("주소는 %s 이다" %self.address)
        print("전화번호는 %s 이다" %self.phone_number)
        if self.year == 1: # 조건문 사용
                print("멋사 %d년차"  %self.year)
                print("우와 아기사자다 !")

        else:
                print("멋사 %d년차" %self.year)
                print("우와 운영진이다 !")

 
while True: # while true 반복문 사용
            class_name = input("객체 명을 입력하시오.(단,영문으로) : ")
            if class_name == "종료": # 양변의 값을 비교할 때는 == 연산자 사용 / =는 대입연산자로 비교하는 것이 아님.
                    break # 루프 빠져나오기
            name = input("이름을 입력하시오.(단,한글로):")
            grade = int(input("학년을 입력하시오.(단,숫자로):"))
            student_number = int(input("학번을 입력하시오.(단,숫자로):"))
            sex = input("성별을 입력하시오.(모를 때는 모른다 라고 입력.):")
            if sex == "모른다":
                sex == "None"
            address = input("주소를 입력하시오. (~시까지만) : ")
            phone_number = input("전화번호를 입력하시오.(모를 때는 모른다 라고 입력.):")
            if phone_number == "모른다":
                phone_number == "None"
            year = int(input("멋사 몇년차인가요?.(단,숫자로):"))  

            class_name = Student(name,grade,student_number,sex,address,phone_number,year)
            class_name.introduce()

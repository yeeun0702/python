kimyeeun={'name':"kimyeeun",'age':'21','birthday':'2002년 7월 2일','sex':'여자','phone':'010-3390-4089'}
kimhaeun={'name':"kimhaeun",'age':'21','birthday':'2002년 7월 2일','sex':'여자','phone':'010-3391-4089'}
kimyewon={'name':"kimyewon",'age':'21','birthday':'2002년 7월 1일','sex':'여자','phone':'010-6700-4843'}

name_list=["1","2","3"]
age_list=["1","2","3"]
birthday_list=["1","2","3"]
sex_list=["1","2","3"]
phone_list=["1","2","3"]


name_list[0:3]=[kimyeeun['name'],kimhaeun['name'],kimyewon['name']]
age_list[0:3]=[kimyeeun['age'], kimhaeun['age'], kimyewon['age']]
birthday_list[0:3]=[kimyeeun['birthday'], kimhaeun['birthday'],kimyewon['birthday']]
sex_list[0:3]=[ kimyeeun['sex'], kimhaeun['sex'],kimyewon['sex']]
phone_list[0:3]=[kimyeeun['phone'], kimhaeun['phone'], kimyewon['phone']]

# 5~9줄 아무거나 담은 걸 12~16줄처럼 슬라이싱해서 key랑 value 이용해서 수정하기 

print("이름 리스트는",name_list)
print("나이 리스트는", age_list)
print("생일 리스트는", birthday_list)
print("성별 리스트는", sex_list)
print("전화번호 리스트는", phone_list)

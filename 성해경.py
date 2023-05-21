# 파이썬의 함수 작성법은 아래처럼 def 함수명(매개변수) : 으로 한다.
def examOne(a):
  # if 문의 방식은 js 와 유사하지만 차이는 (){}를 쓰지 않는 점.
  # 이중if 사용 시에는 문단열을 맞춰줘야 정상적으로 작동한다.

  if isinstance(a, int):
    if (a-int(a))!=0:
      print('정수를 입력해주세요')
    else :
      print(a)
  else :
    print('정수를 입력해주세요')

# 함수 실행은 js 와 동일함.
examOne(1.5)
examOne(1)

# print 해서 확인해보니 결과가 class 'int' 로 나온다.
# print(type(1))
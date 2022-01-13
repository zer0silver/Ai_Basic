# 리스트와 반복문을 사용해 데이터를 불러오세요.
# 이를 이용해 각 학생별 평균을 구해보세요

score = [(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
  cnt = 0
  # list(score) = ((100,100),(95,90),(55,60),(75,80),(70,70))
  for x,y in list(score):
    cnt+=1
    print(cnt," 번, 평균 : ", float((x+y)/2))
    
get_avg(score)

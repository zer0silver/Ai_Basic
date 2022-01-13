# num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

num_list = [1,5,7,15,16,22,28,29]


def get_odd_num(num_list):
    res = []
    for i in num_list:
        if (i%2==1):
            res.append(i)
    return res
    
    
print(get_odd_num(num_list))

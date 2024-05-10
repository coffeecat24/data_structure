def sum_range(begin,end,step=1):
    sum=0
    for i in range(begin,end,step): sum=sum+i
    
    return sum

#파이썬은 메인 함수가 따로 없음 파이썬 함수를 불러쓰고싶으면 import할 수 있음
# 외부에서 import해온 테스트 코드? 어떤 코드가 import한 파일에서 실행됨.
#if문 이하의 test 코드의 경우 sum.py를 실행할 경우에만 if문 아래가 실행됨,
#import한 다른 코드에선 if문 이하가 실행 안됨.
if __name__=="__main__":
    print('sum=',sum_range(1,10))
    print('sum=',sum_range(1,10,2))
    print('sum=',sum_range(step=3,begin=1,end=10))
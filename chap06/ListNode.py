#연결 리스트를 만들기 위한 재료
class ListNode:
    #이중 연결 리스트의 경우엔 privious도 추가 가능
    def __init__(self, data, next):
        self.data = data
        self.next = next
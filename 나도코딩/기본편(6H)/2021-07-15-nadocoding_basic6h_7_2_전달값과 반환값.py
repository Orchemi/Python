# ----------------------------------------------------------
# 전달값과 반환값
##  값을 전달하고 반환값을 받는 함수
#   잔액(balance)에 입금액(money)을 전달받아 입금하는 함수

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money  # 반환

balance = 0  # 초기 잔액
balance = deposit(balance, 1000)
"""deposit(balance, money) 함수 실행하여 
balance = 0 에 money(1000) 입금하고 
잔액 알리는 print문 실행 후 
balance에 입금액 추가"""

print(balance)  # 출력값 : 1000


# 출금하는 함수

def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액 >= 출금액
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금액이 잔액보다 많습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)  # 출력값 : 입금이 완료되었습니다. 잔액은 1000원입니다.
balance = withdraw(balance, 2000)  # 출력값 : 출금액이 잔액보다 많습니다. 잔액은 1000원입니다.
balance = withdraw(balance, 500)  # 출력값 : 출금이 완료되었습니다. 잔액은 500원입니다.


## 밤에 출금하는 경우
#   밤에 출금하는 경우 수수료가 붙는다고 가정
#   수수료는 100원

def withdraw_night(balance, money):
    commission = 100  # 수수료 100원
    return commission, balance - money - commission
# 수수료와 잔액-출금액-수수료 값을 'tuple' 형식으로 반환

balance = 0
balance = deposit(balance, 1000)  # 출력값 : 입금이 완료되었습니다. 잔액은 1000원입니다.
commision, balance = withdraw_night(balance, 500)  # 잔액(1000)에서 출금액(500)과 수수료(100)를 빼는 함수 동작
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commision, balance))  # 출력값 : 수수료는 100원이며, 잔액은 400원입니다.

#  ----------------------------------------
#  출처 : 나도코딩 파이썬 무료 강의(기본편)
#  https://www.youtube.com/watch?v=kWiCuklohdY&t=750s

# 가위바위보
# 5판 3선승제
# \n플레이어는 가위 바위 보 중 하나를 선택
# 로봇도 랜덤으로 하나 선택
# 각각의 패가 보여짐
# 승패 여부기록
# 3승 먼저 달성하는 쪽이 이깁니다.
# 시간이 충분하다면 베팅도 한 번 구현해보세요.

from random import *
balance = 10000
betting_amount = 0
prediction = 1
lst_rsp = ["가위", "바위", "보"]
def betting():
    global balance
    global betting_amount
    global prediction
    betting_amount = int(input("얼마를 베팅하시겠습니까? (배당 x2, 잔고 : {})\n".format(balance)))
    if betting_amount > balance:
        print("잔고가 부족합니다. 잔고보다 적은 돈을 입력하십쇼")
        return betting()
    prediction = int(input("플레이어와 로봇 중 승리를 예상하는 곳을 선택하십쇼 (플레이어:1, 로봇:2)"))

    # balance -= betting_amount
    if prediction ==1:
        print(f"{betting_amount}원을 플레이어에 베팅하셨습니다. 게임 시작합니다.\n")
    else:
        print(f"{betting_amount}원을 로봇에 베팅하셨습니다. 게임 시작합니다.\n")

def choice(): # 플레이어, 로봇 선택
    player_rsp = input("가위, 바위, 보 중 하나를 입력하세요.\n")
    if player_rsp != "가위" and player_rsp != "바위" and player_rsp != "보":
        print("잘못입력하셨습니다. 가위, 바위, 보 중 하나를 입력하세요\n")
        return choice()

    if player_rsp == "가위":
        player_rsp = 0
    elif player_rsp == "바위":
        player_rsp = 1
    elif player_rsp == "보":
        player_rsp = 2

    robot_rsp = randint(0, 2) # (0 = 가위) (1 = 바위) (2 = 보)
    # robot_rsp =1

    return winner(player_rsp, robot_rsp, prediction)

def winner(player_rsp, robot_rsp, prediction):
    if player_rsp > robot_rsp and player_rsp + robot_rsp != 2:
        print("\n플레이어 : {} vs {} : 로봇. 플레이어 승".format(lst_rsp[player_rsp], lst_rsp[robot_rsp]))
        return "O"
    elif player_rsp < robot_rsp and player_rsp + robot_rsp !=2:
        print("\n플레이어 : {} vs {} : 로봇. 로봇 승".format(lst_rsp[player_rsp], lst_rsp[robot_rsp]))
        return "X"
    elif player_rsp == robot_rsp:
        print("\n플레이어 : {} vs {} : 로봇. 재대결\n".format(lst_rsp[player_rsp], lst_rsp[robot_rsp]))
        return choice()
    else:
        if player_rsp < robot_rsp:
            print("\n플레이어 : {} vs {} : 로봇. 플레이어 승".format(lst_rsp[player_rsp], lst_rsp[robot_rsp]))
            return "O"

        elif player_rsp > robot_rsp:
            print("\n플레이어 : {} vs {} : 로봇. 로봇 승".format(lst_rsp[player_rsp], lst_rsp[robot_rsp]))
            return "X"


def game():
    global balance
    global betting_amount
    global prediction
    lst_winner = "_ "*5
    lst_winner = list(lst_winner)

    betting()

    for i in range(5):
        lst_winner[i*2] = choice()
        print("승패 현황 : ", end="")
        for i in range(9):
            print(lst_winner[i], end="")
            if i == 8:
                print("\n") # 줄바꿈 2번
                
        if lst_winner.count("O") == 3:
            print("최종 {}:{} 플레이어 승리".format(lst_winner.count("O"), lst_winner.count("X")))
            if prediction == 1:
                balance += betting_amount*2
                print("베팅에 성공하셨습니다. 베팅금액{}, 회수금액{}, 잔고{}입니다.".format(betting_amount, betting_amount*2, balance))
            else:
                balance -= betting_amount
                print("베팅에 실패하셨습니다. 베팅금액{}, 잔고{}입니다.".format(betting_amount, balance))
            break
        elif lst_winner.count("X") == 3:
            print("최종 {}:{} 로봇 승리".format(lst_winner.count("O"), lst_winner.count("X")))
            if prediction == 2:
                balance += betting_amount*2
                print("베팅에 성공하셨습니다. 베팅금액{}, 회수금액{}, 잔고{}입니다.".format(betting_amount, betting_amount*2, balance))
            else:
                balance -= betting_amount
                print("베팅에 실패하셨습니다. 베팅금액{}, 잔고{}입니다.".format(betting_amount, balance))
            break

    if balance == 0:
        print("잔고가 0원입니다. 게임을 종료합니다.")
        return 0

    regame = input("한 번더 베팅하시겠습니까? (예:1/아니오:2)\n")
    if regame == "1":
        return game()
    else:
        print("최종금액 {}원으로 게임이 종료되었습니다.".format(balance))

game()
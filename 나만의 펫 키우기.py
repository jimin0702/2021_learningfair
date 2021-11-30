hp= 30
exp=0
lv=1
day = 1
print('=============================게임설명 =================================')
print()

print('팻키우기 게임은 자신만의 팻에게 애정을 주며 팻을 키우는 게임입니다.')
print()

print('팻에게 밥주기, 운동하기, 놀기, 잠자기 등을 하며 팻을 키울 수 있습니다. ')
print()

print('기본적으로 팻은 HP = 30. EXP = 0 , LV = 1로 설정되어있습니다.')
print()

print('HP가 0이되면 팻은 하늘나라로 가게 되는 동시에 게임오버되며, EXP가 30이 될때마다 LV이 1씩 오릅니다.')
print()

print('LV이 오르면 EXP는 다시 0으로 돌아갑니다.')
print()

print('팻에게 잠을 재우면 다음날로 넘어가게 됩니다.')
print()

print('=========================  팻 키우기 시작!  ===============================')
print()

name= input("팻의 이름을 입력하세요:")   
print()

print(' ***** 미션 : 적은 일수로 팻을 10LV까지 키우기 *****')
print()
print()

print(" <<<< 1 일째 아침입니다! " ,name , '(이)를 잘 돌보아주세요! >>>> ' )
print()

while True:
    print('='*80)
    print(name, '(이)에게 할 일을 선택해주세요 (숫자만 입력해주세요).')
    flag = int(input('1. 밥먹기  / 2. 잠자기  / 3. 놀아주기  / 4.운동하기  / 5. 상태확인  / 6.종료: '))
    print()
    if flag == 1:
        feed = ' 팻에게 먹이를 줍시다'
        menu = ' >>> 팻 먹이 자판기  1. 사료 2. 건강식품 3. 간식 <<< '
        print(feed)
        print(menu)
        print()
        
        # 딕셔너리 사용 - 먹이자판기
        
        food = { '사료': ('-5 HP', '+8 EXP') , '건강식품' : ('-8 HP', '+ 10 EXP'), '간식' : ('-3 HP' , '+5 EXP')}
        print( ' 1. 사료 선택 시 :', food['사료'])
        print( ' 2. 건강식품 선택 시 :', food['건강식품'])
        print( ' 3. 간식 선택 시 :' ,food['간식'])
        print()

        order= int(input("먹이 종류를 선택하세요. 번호입력 : "))
        print()
        if order == 1:
            hp -=5
            exp +=8
            print("당신의 팻이 사료를 먹었습니다.")
            print(name, '사료','HP =', hp, '/ EXP =',exp, '/ LV =', lv)
            print()

        elif order == 2:
            hp -=8
            exp +=10
            print("당신의 팻이 건강식품을 먹었습니다.")
            print(name, '건강식품','HP = ', hp, '/ EXP = ',exp, '/ LV = ', lv)
            print()

        elif order == 3:
            hp -=3
            exp +=5
            print("당신의 팻이 간식을 먹었습니다.")
            print(name, '간식','HP = ', hp, '/ EXP = ',exp, '/ LV = ', lv)



    elif flag == 2:
        hp += 15
        print(name, '잠자기', 'HP = ', hp,  '/ EXP =', exp, '/ LV =', lv)
        day += 1
    
        print()
        print('--------------------하루가 지났습니다---------------------')
        print("<<<<<",day,"일째 아침이 밝았습니다! ", name, "(이)를 잘 돌보아 빠른 시일내에 LV을 올려주세요! >>>>")
        print()
        
    elif flag == 3:
        hp-= 1
        exp+=5
        print(name, '놀아주기','HP = ', hp, '/ EXP = ',exp, '/ LV =', lv)
        print()
        
    elif flag == 4:
        
        sport = ' 팻과 운동을 해봅시다. 무엇을 할까요? '
        menu   = ' >>> 팻과 운동하기 1. 산책   2. 공놀이   <<< '
        print(sport)
        print(menu)
        print()
        # 딕셔너리 사용 - 운동 선택
        
        sports = { '산책': ('-5 HP', '+8 EXP') , '공놀이' : ('-8 HP', '+ 10 EXP')}
        print( ' 1. 산책 선택 시 :', sports['산책'])
        print( ' 2. 공놀이 선택 시 :', sports['공놀이'])
        
        print()


        order= int(input("운동  종류를 선택하세요. 번호입력 : "))
        print()

        if order == 1:
            hp -=10
            exp +=10
            print("당신과 팻이 산책을 했습니다! ")
            print(name, '산책','HP =  ', hp, '/ EXP = ',exp, '/ LV = ', lv)
            print()

        elif order == 2:
            hp -=8
            exp +=10
            print("당신의 팻이 공놀이를 했습니다!")
            print(name, '공놀이','HP = ', hp, '/ EXP = ',exp, '/ LV = ', lv)
            print()

        
    elif  flag == 5:
        print(name,'정보확인', 'HP = ', hp, '/ EXP = ',exp, '/ LV = ', lv)
        print()
        
    elif flag == 6:
        print(name,'종료')
        print()
        break
    
    if exp >= 30:
        lv += 1
        print('축하합니다', name,'(이)가 ', lv, 'LV이 되었습니다.')
        print()
        print('=          =         =        =       =    =====')
        print('=           =       =         =       =    =    =       ')
        print('=            =     =          =       =    =====       ')
        print('=             =   =           =       =    = ')
        print('=              = =             =     =     =')
        print('=====           =                ===       =')
        

        
        
        print()
        print('================================================================')
        print()
        exp -= 30
        
    if hp <= 0:
        print(name,'(이)의 HP가 0이 되었습니다.')
        print('========================== GAME OVER ============================')
        print('돌본 일 수 : ', day, '일', ' 달성 LV ; ', lv)
        input()
        break

    if lv == 10:
        print(name, '(이)가 10LV에 도달하였습니다')
        print()
        print('============================== 미션 성공 ================================')
        print()
        print('돌본 일 수 : ', day,'일', ' 달성 LV ; ', lv)
        print('다음 시행에는 더 빠른 시일 내에 10LV에 도달할 수 있도록 해보세요!')
        print()
        print('============================== 게임 종료 =================================')
        break
        

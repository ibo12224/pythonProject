import func
custlist=func.load_data()
page=len(custlist)-1



while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
    if choice=="I":
        page=func.insert_data(custlist)
        
    elif choice=="C":
        print("현재 고객 정보 조회")
        func.check(custlist,page)
    
    elif choice == 'P':
        page=func.bcheck(custlist,page)
    elif choice == 'N':
        page=func.ncheck(custlist,page)

    elif choice=='D':
        print("고객 정보 삭제")
        em=input("삭제할려는 이메일:")
        delok=0
        for i,item in enumerate(custlist):           
            if item['email']==em:
                print(f'{custlist.pop(i)}고객님 정보 삭제')
                delok=1
                break
            
        if delok==0:
            print("등록되지 않은 email입니다.")
        
    elif choice=="U": 
        print("고객 정보 수정")
        em=input("수정할려는 이메일:")
        idk=0
        for i in range(0,len(custlist)):
            if custlist[i]['email']==em:
                idk = i
            break
        if idk==-1:
            print("등록되지 않은 email입니다.")
            break
        
        
        while True:
            n=input('''
            다음 중 수정할려는 정보를 선택하시오:
            이름, 성별, 출생년도
            없으면 exit>>>
                ''')
            m=input("수정할 정보를 입력하시오.")
            if n=="exit":
                break
            if n in customer:
                customer[n]=m
            else:
                print("존재하지 않는 정보입니다.")
        
    elif choice=="Q":
        print("프로그램 종료")


        break

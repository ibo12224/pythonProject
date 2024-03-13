import json
import re
def load_data():
  f=open('02_customer/data.json','r')
  return json.load(f)
def save_data(custlist):
  f=open("02_customer/data.json","w")
  json.dump(custlist,f,indent=2)
  f.close()
def insert_data(custlist):
  print("고객 정보 입력")
  customer={'name':'','gender':'','email':'','birthyear':''}
  customer['name']=input("이름 입력")
  while True:
      gender = input("성별: ")
      gender=gender.upper()
      if re.match(r'[MF]', gender):
          customer['gender']=gender
          break
  while True:
      regex=re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,10}[.][a-z]{2,10}')
      while True:
          customer['email']=input('이메일을 입력하세요')
          check=regex.search(customer['email'])
          if check:
              break
          else:
              print('@를 포함한 이메일을 입력')
      id_check=0
      for i in custlist:
          if i['email']==customer['email']:
              id_check=1
              break
      if id_check==0:
          break
      print("중복되는 이메일")
    
      while True:
          birthyear=input("출생년도:")
          if 4==len(birthyear):
              customer['birthyear']=birthyear
              break
      print(custlist)
      custlist.append(customer)
      page=len(custlist)
      return page
def check(custlist,page):
  if page>0:
      print(page)
      print(f'고객 정보: {custlist[page]}\n 페이지:{page+1}')
  else:
      print("입력된 페이이지가 없음")
  return page
def bcheck(custlist,page):
  print("이전 고객 정보 조회")
  if page-1!=0:
      page-=1
  print(f'고객 정보: {custlist[page]}\n 페이지:{page+1}')
  return page

def ncheck(custlist,page):
  print("다음 고객 정보 조회")
  n=len(custlist)-1
  if page+1!=n:
      page+=1
  print(f'고객 정보: {custlist[page]}\n 페이지:{page+1}')
  return page


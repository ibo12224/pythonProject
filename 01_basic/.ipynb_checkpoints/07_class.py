# class Cookie:
#   pass
# a= Cookie()
# b=Cookie()

# print(a)
# print(id(a))

# print(type(a))


class FourCal:
  def setdata(self,first,second):
    self.first=first
    self.second=second
  def add(self):
    result=self.first+self.second
    print(result)
    return result
  def print(self):
    print(self.result)
  def __init__(self,first=1,second=1):
    self.first=first
    self.second=second


a=FourCal(3,4)
a.add()
class mFourCal(FourCal):
  pass
b=mFourCal()
b.add()
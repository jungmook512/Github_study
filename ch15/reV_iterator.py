# reV)iterator.py


class ReverseIterator : 
   def __init__(self, data) :
      self.data = data
      self.position = len(self.data)-1

   def __iter__(self) :
      return self
   
   def __next__(self) :
      if self.position < 0 :
         raise StopIteration
      result = self.data[self.position]
      self.position -= 1
      return result


ri = ReverseIterator([1,2,3,4,5,6])
print(type(ri))
print(next(ri))

for item in ri :
   print(item)
   
# print(next(ri))       #StopIteration

# 이터레이터 판단 기준
# __iter__
# __next__
# dir() : 객체의 속성을 보여주는 함수
print(dir(ri))

print('__iter__' in dir(ri))
print('__next__' in dir(ri))
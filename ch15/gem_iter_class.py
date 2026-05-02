# gem_iter_class.py

gen = (i*i for i in range(1,10))

class MyIterator :

    def __init__(self) :
        self.data = 1

    def __iter__(self) :
        return self
    
    def __next__(self) :
        result = self.data * self.data
        if self.data  >=10:
            raise StopIteration
        self.data += 1
        return result
    
my_iter = MyIterator()
print(type(my_iter))

print(next(my_iter))
for i in my_iter :
    print(i)
print(next(my_iter))        #StopIteration
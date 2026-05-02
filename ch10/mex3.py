
# from : 가독성 좋음
from mex1 import plus
from mex1 import Cvalue
# from mex1 import p1

# 객체 생성
p3 = Cvalue()
p3.add(100)
p3.add(200)
p3.fprint()


# from 모듈명 import *
from mex1 import *
# from mex1 import Cvalue, plus, p1

print("---------")
# p1.fprint()

print(__name__)

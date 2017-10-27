# -*-coding:utf-8-*-
# Author:sunhao
import os,sys

Base_Path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(Base_Path)

sys.path.append(Base_Path)



from Shopping_Mall  import change




change.shopping()

change.test()
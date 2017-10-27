# -*-coding:utf-8-*-
# Author:sunhao

import os,sys

Base_Path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.append(Base_Path)

from  modules  import admincenter,authentication,creditcard,shopping

# admincenter.run()
# authentication.test1()
# creditcard.test2()
# shopping.test3()




while True:
    print("\33[35;1m欢迎进入信用卡购物模拟程序\33[0m".center(50,'-'),
          "\n1.购物中心",
          "\n2.信用卡中心",
          "\n3.后台管理",
          "\n4.退出程序")

    choice_id=input("\33[34;0m选择要进入模式\33[0m:")
    if choice_id.isdigit():
        choice_id=int(choice_id)
        if choice_id == 1:
            authentication.user_auth()

        elif choice_id==2:
            authentication.credit_card_auth()

        elif choice_id==3:
            authentication.admin_center()








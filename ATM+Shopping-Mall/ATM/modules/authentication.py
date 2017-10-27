# -*-coding:utf-8-*-
# Author:sunhao

import os,json,getpass


BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


'''数据库文件相对路径'''
__db_users_dict = BASE_DIR + r"\database\users_dict"
__db_credit_card_dict = BASE_DIR + r"\database\credit_card_dict"




'''认证装饰器'''


def auth(auth_type):


    def outer_wrapper(func):


        if auth_type=="user_auth":          #用户登录验证

            def wrapper():

                res=func()
                username = input("\33[34;0m请输入用户名：\33[0m")
                password = input("\33[34;0m请输入密码：\33[0m")
                if len(username.strip())>0:
                    with open(__db_users_dict,'r+') as f_user_dict:

                        users_dict = json.loads(f_user_dict.read())

                        if username in users_dict.keys():
                            if password==users_dict[username]["password"]:
                                #print(users_dict.keys())
                                if users_dict[username]["locked"]==0:
                                    print("\33[31;0m用户 %s 认证成功\33[0m"%username)
                                    return res,username
                                else:
                                    print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % username)
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")


                        else:
                            print("\33[31;0m输入的用户名为空 认证失败\33[0m")

            return wrapper




        elif auth_type=="credit_card_auth":    #信用卡登录验证
            def wrapper():

                res=func()
                credit_card=input("\33[34;0m请输入信用卡卡号(6位数字)：\33[0m")
                credit_passwd=input("\33[34;0m请输入信用卡的密码：\33[0m")

                if len(credit_card.strip()) >0:
                    with open(__db_credit_card_dict,'r+') as f_credit_card_dict:
                        credit_card_dict=json.loads(f_credit_card_dict.read())
                        #print(credit_card_dict)
                        if credit_card in credit_card_dict.keys():
                            if credit_passwd==credit_card_dict[credit_card]["password"]:
                                if credit_card_dict[credit_card]["locked"]==0:
                                    print("\33[31;0m信用卡用户 %s 认证成功\33[0m" % credit_card)
                                else:
                                    print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % credit_card)
                            else:
                                print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
                        else:
                            print("\33[31;0m输入的信用卡用户为空 认证失败\33[0m")

            return wrapper


        elif auth_type=="admin_auth":     # admin中心认证

            def wrapper():

                res=func()

                admin_dict={"admin":"admin"}

                username=input("\33[34;0m请输入管理用户名：\33[0m")
                passwd=input("\33[34;0m请输入管理密码：\33[0m")

                if len(username.strip())>0:
                    if username in admin_dict.keys():
                        if passwd==admin_dict[username]:
                            print("\33[31;0m管理用户 %s 认证成功\33[0m" % username)


                        else:
                            print("\33[31;0m输入的密码不匹配 认证失败\33[0m")

                    else:
                        print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
                else:
                    print("\33[31;0m输入的用户名为空 认证失败\33[0m")

            return wrapper

    return outer_wrapper




"""用户登录认证"""
@auth(auth_type="user_auth")
def user_auth():
    print("\33[32;0m用户登录认证\33[0m".center(40, "-"))
    return True


'''信用卡认证'''
@auth(auth_type="credit_card_auth")
def credit_card_auth():
    print("\33[32;0m信用卡登录认证\33[0m".center(40, "-"))
    return True

@auth(auth_type="admin_auth")
def admin_center():
    print("\33[32;0m后台管理登录认证\33[0m".center(40,"-"))
    return True




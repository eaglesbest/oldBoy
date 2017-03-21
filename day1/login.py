#!/usr/bin/python2.7
#-*- coding:utf-8 -*-

for i in range(3):
    username = raw_input("Username:")
    password = raw_input("Password:")
    if username == '' or password == '':
        print("Username or Password can not be empty.Please input again!")
	continue
    else:
        with open('userInfo','r+') as fobj:
            fobj.seek(36,0)
            for line in fobj.readline():
                userInfo = line.strip().split()
                if userInfo[0] == username and userInfo[1] == password:
                    if userInfo[2] == '1':
                        print("You are locked!")
                    else:
                        print("Welcom %s") % userInfo[0]
                else:
                    retry_counter = userInfo[3]
                    if retry_counter == '3':
                       userInfo[2] = 1
		       ### How to write one line into file
                       fobj.writlines 

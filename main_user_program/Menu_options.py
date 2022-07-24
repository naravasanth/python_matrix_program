from Matrix_learn_simple import additionMatrix as AM
from Matrix_learn_simple import substractionMatrix as SM
from Matrix_learn_simple import multiplicationMatrix as MM
from Matrix_learn_Intermediate import divisionMatrix as DM
from Matrix_learn_Intermediate import equaloperationMatrix as EM
from Matrix_learn_Intermediate import maduloMatrix as MaduleM
from Matrix_learn_Intermediate import suaqurMatrix as SqrM
import numpy as np
import time
import os
class user_menu():
    @staticmethod
    def l1():
        while True:
            try:
                print("enter matrix values with space")
                l = list(map(int, input().split(" ")))
                m1 = np.array(l).reshape(2, 2)
                return m1
                break
            except ValueError:
                print("please enter correct values")
    @staticmethod
    def option():
        lines = []
        with open('C:\\Users\\vakumarn\\PycharmProjects\\matrix project\\main_user_program\\menu_details', 'r') as f:
            lines = f.readlines()
            count = 0
        for line in lines:
            count += 1
            print("option {}:{}".format(count,line),end="")
        while True:
          arg = input("enter matrix option for operation: ")
          try:
            if isinstance(int(arg),int):
                print(int(arg))
                command = int(arg)
                match command:
                        case 1:
                            print(AM.matrix_ba(m1, m2).addition())
                            print("Sum of Matrix")
                        case 2:
                            print(SM.matrix_ba(m1, m2).substraction())
                            print("Substraction of Matrix")
                        case 3:
                            print(MM.matrix_ba(m1, m2).multiplication())
                            print("multiplication of Matrix")
                        case 4:
                            print(DM.matrix_in(m1, m2).division())
                            print("Division of Matrix")
                        case 5:
                            print(EM.matrix_in(m1, m2).equ())
                            print("Matching the Matrix values")
                        case 6:
                            print(MaduleM.matrix_in(m1, m2).madulo())
                            print("Madule of Matrix")
                        case 7:
                            print(SqrM.matrix_in(m1, m2).sqr())
                            print("squer of Matrix")
                break
            else:
                print("please enter correct value")
          except:
              print("enter correct value:")

obj = user_menu
m1 = obj.l1()
m2 = obj.l1()


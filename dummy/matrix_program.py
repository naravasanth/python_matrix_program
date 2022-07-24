from Matrix_learn_simple import additionMatrix as AM
from Matrix_learn_simple import substractionMatrix as SM
from Matrix_learn_simple import multiplicationMatrix as MM
from Matrix_learn_Intermediate import divisionMatrix as DM
from Matrix_learn_Intermediate import equaloperationMatrix as EM
from Matrix_learn_Intermediate import maduloMatrix as MaduleM
from Matrix_learn_Intermediate import suaqurMatrix as SqrM

import numpy as np
class matrix_def():
    ''' user definding matrix 1 and 2 '''
    @staticmethod
    def l1():
        print("enter matrix values with space")
        l = list(map(int, input().split(" ")))
        m1 = np.array(l).reshape(2, 2)
        return m1

class user_choice(matrix_def):
    def set(self,value):
            self.value= value
            try:
                if self.value == 1:
                    print (AM.matrix_ba(m1,m2).addition())
                    print("Sum of Matrix")
                elif self.value ==2:
                    print (SM.matrix_ba(m1,m2).substraction())
                    print("Substraction of Matrix")
                elif self.value ==3:
                    print (MM.matrix_ba(m1,m2).multiplication())
                    print("multiplication of Matrix")
                elif self.value == 4:
                    print (DM.matrix_in(m1,m2).division())
                    print("Division of Matrix")
                elif self.value == 5:
                    print (EM.matrix_in(m1,m2).equ())
                    print("Matching the Matrix values")
                elif self.value == 6:
                    print (MaduleM.matrix_in(m1,m2).madulo())
                    print("Madule of Matrix")
                elif self.value == 7:
                    print (SqrM.matrix_in(m1,m2).sqr())
                    print("squer of Matrix")
                else:
                    print("enter correct value for operation")
            finally:
                while True:
                    try:
                        l1 = int(input("enter value for next operation else enter no for exit:" ))
                        if isinstance(l1,int):
                           value = int(l1)
                           return obj.set(value)
                    except ValueError:
                        print("\nexit from program Thank you .....")
                        break
if __name__=='__main__':
    obj = user_choice()
    m1 = obj.l1()
    m2 = obj.l1()
    value = int(input("enter operation value: "))
    obj.set(value)



















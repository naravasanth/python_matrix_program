from main_user_program.Menu_options import *
class main():
    def out_put(self):
      while True:
        try:
            user_menu.option()
        finally:
            while True:
                choice = input("Please enter 'Yes' for Operation 'No' for exit: ")
                if choice.lower().strip() == 'yes':
                    return obj.out_put()
                elif choice.lower().strip() == 'no':
                    print("'\nThanks you.... exit from program...")
                    break
                else:
                    print("please enter correct value")
            break


obj = main()
obj.out_put()



















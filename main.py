class PythonSwitch:
    def day(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "monday"

    def case_2(self):
        return "tuesday"

    def case_3(self):
        return "wednesday"

    def case_4(self):
        return "thursday"

    def case_5(self):
        return "friday"

    def case_7(self):
        return "saturday"

    def case_6(self):
        return "sunday"


my_switch = PythonSwitch()
print(my_switch.day(1))
print(my_switch.get())

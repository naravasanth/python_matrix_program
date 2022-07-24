
lines = []
with open('C:\\Users\\vakumarn\\PycharmProjects\\matrix project\\main_user_program\\menu_details','r') as f:
    lines = f.readlines()
    count = 0
for line in lines:
    count += 1
    print(f'option {count}: {line}')
import os

result = ''
while True:
    user_in = input()
    if user_in == 'end':
        break
    result += user_in
rename_map = eval(result)

for old, new in rename_map.items():
    if os.path.exists(old):
        os.rename(old, new)
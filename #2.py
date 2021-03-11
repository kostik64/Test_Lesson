zoop_list = ['a', 'b', 'c', 'd', 'e']
if len(zoop_list) % 2 == 0:
    i = 0
    while i < len(zoop_list):
        el = zoop_list[i]
        zoop_list[i] = zoop_list[i+1]
        zoop_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(zoop_list) - 1:
        el = zoop_list[i]
        zoop_list[i] = zoop_list[i + 1]
        zoop_list[i + 1] = el
        i += 2
print(zoop_list)
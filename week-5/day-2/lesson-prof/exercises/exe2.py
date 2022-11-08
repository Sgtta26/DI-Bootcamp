my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

summup = 0
for num in my_list:
    try:
        summup += num
    except:
        continue

print(summup)
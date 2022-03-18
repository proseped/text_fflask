def select_sort(ls:list):
    for i in range(0,len(ls)-1):
        for j in range(i+1,len(ls)):
            if ls[i] > ls[j]:
                ls[i],ls[j] = ls[j],ls[i]
ls = [3,4,5,1,2]
select_sort(ls)
print(ls)
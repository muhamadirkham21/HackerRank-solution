def merge_the_tools(string, k):
    # your code goes here
    for x in range(0,len(string),k):
        u_list=string[x:x+k]
        check =[]
        for y in u_list:
            if y not in check:
                check.append(y)
        print(''.join(check))

merge_the_tools('AABCAAADA', 3)



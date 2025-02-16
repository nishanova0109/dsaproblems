def max_min(x):
    min=x[0]
    max=x[0]
    for i in x:
        if i<min:
            min=i
        if i>max:
            max=i
    return (min,max)
x=[3, 2, 1, 56, 10000, 167]
print(max_min(x))
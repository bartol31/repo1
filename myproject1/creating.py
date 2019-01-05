def generate_range(start,end):
    i = start
    while i <= end:
        yield i
        i += 1

for i in generate_range(0,6):
    print(i)

















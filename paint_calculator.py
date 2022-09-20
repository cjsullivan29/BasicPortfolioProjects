import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc (height=test_h, width=test_w, coverage = 5):
    area = (height * width)
    num_cans = area / coverage
    cans_needed = math.ceil(num_cans)
    return cans_needed
   
print(paint_calc(test_h, test_w, coverage))



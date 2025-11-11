def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      score = num1
    elif num2 > num1 and num2 > num3:
      score = num2
    else:
      score = num3
    return score  
num1 = 8
num2 = 3
num3 = 5
score = find_max_number(num1, num2, num3)
print("The maximum number is:", score)

def find_mean(num1, num2, num3):
    pass  # Replace 'pass' with code

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    pass  # Replace 'pass' with code


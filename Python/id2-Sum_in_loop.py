def find_Sum(amount, digits):                                                                                                                                   
        numbers = digits.split(' ')
        sum = 0
        for x in range(0, amount):
                sum += int(numbers[x])
        print(sum)
find_Sum(input(), raw_input())

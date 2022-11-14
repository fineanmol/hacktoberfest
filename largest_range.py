def largest_range(array):
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            
            left_count += 1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            
            right_count -= 1

            if (right-left) <= (right_count-left_count):
                right = right_count
                left = left_count

    return [left,right]

a = [3,11,0,7,2,4,1]
print(largest_range(a))
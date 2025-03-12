# checks element one by one sorts them in a gradually built-up sorted array. so it builds up sorted array one element by time.

def insertionsort(array):
    for i in range(1, len(array)):
        current_number = array[i]
        compare_number_position = i-1

        while compare_number_position >= 0 and array[compare_number_position] > current_number:
            array[compare_number_position+1]=array[compare_number_position]
            compare_number_position -= 1
        
        array[compare_number_position+1] = current_number

# Decreasing order
def decreasing_insertionsort(array):
    for i in range(1, len(array)):
        current_number = array[i]
        compare_number_position = i-1

        while compare_number_position >= 0 and array[compare_number_position] < current_number:
            array[compare_number_position+1]=array[compare_number_position]
            compare_number_position -= 1
        
        array[compare_number_position+1] = current_number


# Testing
numbers = [2, 1, 7, 4, 8]
insertionsort(numbers)
print("Järjestetty lista:", numbers)
decreasing_insertionsort(numbers)
print("Järjestetty lista toisessa järjestyksessä:", numbers)

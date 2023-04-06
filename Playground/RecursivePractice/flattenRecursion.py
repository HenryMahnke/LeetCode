# given some array [1, [2, [3, 4], 5], 6]
# flatten it such that it returns [1, 2, 3, 4, 5, 6]
def flatten(arr):
    if not isinstance(arr, list):
        # base case: if it's not a list, return a list with a single element
        print(f'Base case: {arr}')
        return [arr]
    else:
        # recursive case: flatten each element and concatenate them together
        result = []
        for element in arr:
            print(f'Processing element: {element}')
            result.extend(flatten(element))
        print(f'Result: {result}')
        return result


print(flatten([1, [2, [3, 4], 5], 6]))
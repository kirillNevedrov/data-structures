from src.stack import Stack


def sort(stack: Stack[int]) -> None:
    temp_stack = Stack[int]()

    stack_length = 0

    while not stack.is_empty():
        value = stack.pop()
        stack_length += 1
        temp_stack.push(value)

    while not temp_stack.is_empty():
        value = temp_stack.pop()
        stack.push(value)

    for i in range(stack_length, 0, -1):
        max_value = None
        is_max_value_detected = False

        while i > 0:
            value = stack.pop()

            if max_value is None or value > max_value:
                max_value = value

            temp_stack.push(value)

            i -= 1

        stack.push(max_value)

        while not temp_stack.is_empty():
            value = temp_stack.pop()
            if value == max_value and not is_max_value_detected:
                is_max_value_detected = True
            else:
                stack.push(value)

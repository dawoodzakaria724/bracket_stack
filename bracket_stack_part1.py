######################################################

# python3

index = 0


def are_matching(left, right):
    # this function checks if both left and right brackets are matching
    # returns true if they are matching and false if they are not

    if left == '(':
        if right != ")":
            return False
    else:
        return True
    if left == '{':
        if right != "}":
            return False
    else:
        return True
    if left == '[':
        if right != "]":
            return False
    else:
        return True


def find_match(text):

    global index
    bracket_stack = []

    for i, next in enumerate(text):
        index = i
        if next in "([{":
            # when you encounter an open bracket, push it to your stack
            bracket_stack.append(next)

        if next in ")]}":
            # in case of right bracket with no left bracket
            if len(bracket_stack) == 0:
                return False
            # otherwise continue with code
            if (len(bracket_stack) > 0) and (are_matching(bracket_stack[-1], next)):
                bracket_stack.pop()

    # check empty stack
    if len(bracket_stack) == 0:
        return True
    else:
        return False

        # When you encounter a right bracket,
        # you need to compare and see if it has a matching left bracket
        # return the index when you encounter the error
        # take into consideration the special cases: right bracket with no
        # left brackets encountered before, or the input was processed and
        # the stack is not empty


def main():
    text = input()

    # Forces user to input something
    while not text:
        print("please enter any character to continue:")
        text = input()

    match = find_match(text)

    # If there is no error, print success
    # if there is an error, print the index return from the above function
    if not match:
        print(index)
    else:
        print("Success!")



if __name__ == "__main__":
    main()
########################################################

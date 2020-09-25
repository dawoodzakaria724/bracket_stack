index = 0


class CheckBrackets:

    def find_match(self, text):
        global index
        __bracket_stack = []

        for i, next in enumerate(text):
            index = i
            if next in "([{":
                # when you encounter an open bracket, push it to your stack
                __bracket_stack.append(next)

            if next in ")]}":
                # in case of right bracket with no left bracket
                if len(__bracket_stack) == 0:
                    return False
                # otherwise continue with code
                if (len(__bracket_stack) > 0) and (self.are_matching(__bracket_stack[-1], next)):
                    __bracket_stack.pop()

        # check empty stack
        if len(__bracket_stack) == 0:
            return True
        else:
            return False

            # When you encounter a right bracket,
            # you need to compare and see if it has a matching left bracket
            # return the index when you encounter the error
            # take into consideration the special cases: right bracket with no
            # left brackets encountered before, or the input was processed and
            # the stack is not empty

    def are_matching(self, left, right):
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


trial = CheckBrackets()
if not trial.find_match(input()):
    print(index)
else:
    print("Success!")

class Pattern():
    """Represents a number pattern, a list of operations
    A pattern is represented by a series of strings in the form
    [operation][integer].  For example, the string "*3" represents
    multiplication by 3.  A pattern list ['*2', '+1', '-3'] means that for
    each number in the pattern, the next number is calculated by multiplying
    the current number by 2, adding 1, and subtracting 3.  For example, this
    would yield the pattern:

            5->8->14->26->50
    """
    def __init__(self):
        """Constructor.  Initializes empty list. """
        self.ops = []

    def add_operation(self, op):
        """Adds an operation to the pattern list. """
        if op[0] in ["*", "+", "-"]:
            self.ops.append(op)
        else:
            print("Improperly formatted operation '{}' not added.".format(op))

    def apply_pattern(self, num):
        for op in self.ops:
            if op[0] == "+":
                num = num + int(op[1:])
            elif op[0] == "-":
                num = num - int(op[1:])
            else:
                num = None
        return num

    def get_prev(self, num):
        for op in self.ops:
            if op[0] == "+":
                num = num - int(op[1:])
            elif op[0] == "-":
                num = num + int(op[1:])
            else:
                num = None
        return num


    def humanize(self):
        """Returns the pattern as a human-readable string"""
        out = ""
        for op in self.ops:
            if op[0] == "+":
                out = out + "add " + op[1] + ", "
            elif op[0] == "-":
                out = out + "subtract " + op[1] + ", "
            elif op[0] == "*":
                out = out + "multiply by " + op[1] + ", "

        if out[-2:] == ", ":
            out = out[:-2]

        return out

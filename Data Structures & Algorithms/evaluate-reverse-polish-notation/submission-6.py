class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = int(tokens[0])
        my_set = []
        my_set.append(int(tokens[0]))

        for i in range(1, len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                my_set.append(tokens[i])
            else: 
                k = my_set.pop()
                j = my_set.pop()
                if tokens[i] == "+":
                    val = int(j) + int(k)
                if tokens[i] == "-": 
                    val = int(j) - int(k)
                if tokens[i] == "*":
                    val = int(j) * int(k)
                if tokens[i] == "/":
                    val = int(j) / int(k)
                my_set.append(val)

        return int(val)
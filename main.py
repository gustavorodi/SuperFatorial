
class Fatorial:
    def __init__(self, m):
        self.Memoization = {}
        valorFinal = 1
        for x in range(1, m+1):
            valorFinal *= self.factorial(x)
        print(valorFinal)

    def factorial(self,n):
        tempKey = ''
        if n == 0:
            return 1
        else:
            tempKey = str(n)
            tempKey += str(n -1)

            if tempKey in self.Memoization.keys():
                return self.Memoization[tempKey]
            else:
                self.Memoization[tempKey] = n * self.factorial(n - 1)
                return self.Memoization[tempKey]


obj = Fatorial(4)
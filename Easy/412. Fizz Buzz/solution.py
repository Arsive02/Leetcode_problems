class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        for i in range(1,n+1):
            if not i%3 and not i%5:
                yield "FizzBuzz"
            elif not i%3:
                yield "Fizz"
            elif not i%5:
                yield "Buzz"
            else:
                yield str(i)

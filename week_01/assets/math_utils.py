
def square_sum(n):
  return sum(i * i for i in range(n))

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

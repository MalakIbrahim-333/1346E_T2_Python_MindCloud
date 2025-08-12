# Reading the first line: K = number of lists, M = modulo value
K, M = map(int, input().split())

# read the K lists
lists = []
for _ in range(K):
    data = list(map(int, input().split()))
    n = data[0]  # first number is size of list
    lists.append(data[1:])  # rest are the elements

# brute force approach to try all combinations
from itertools import product

max_value = 0

# product gives all possible ways of picking one element from each list
for combination in product(*lists):
    total = 0
    for x in combination:
        total += x**2  # f(X) = X^2
    total %= M  # modulo M
    if total > max_value:
        max_value = total

print(max_value)

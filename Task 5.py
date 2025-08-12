import re

n, m = map(int, input().split())
matrix = [input().ljust(m) for _ in range(n)]  # pad with spaces if short

decoded = ''.join(matrix[row][col] for col in range(m) for row in range(n))
decoded = re.sub(r'(?<=\w)[^A-Za-z0-9]+(?=\w)', ' ', decoded)

print(decoded)


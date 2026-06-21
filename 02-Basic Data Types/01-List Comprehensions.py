# Let's learn about list comprehensions! You are given three integers  and representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by i,j,k on a 3D grid where the sum of i+j+k is not equal to n .

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i,j,k]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if i+j+k != n]

print(result)

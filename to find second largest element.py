data1 = [int(i) for i in input("ENTER NUMBERS SEPARATED BY SPACES = ").split()]

# Step 2: Bubble Sort in Ascending Order
n = len(data1)

for i in range(n):
 for j in range(0, n - i - 1):
        print(j)
#         if data1[j] > data1[j + 1]:
#             # Swap
#             temp = data1[j]
#             data1[j] = data1[j + 1]
#             data1[j + 1] = temp
# print(data1)                  

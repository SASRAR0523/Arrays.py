# print all pairs in the array

n = int(input("Enter array size : "))
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        print(arr[i],arr[j])

#print the pairs with sum k

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j] == k:
            print(arr[i],arr[j])      

#Find pairs of even numbers from the given array. 
#Both the number in a pair should be even numbers.

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i]%2 == 0 and arr[j] == 0:
            print(arr[i],arr[j])

#Find pairs of odd numbers from the given array. 
#Both the number in a pair should be odd numbers.

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i] % 2 != 0 and arr[j] % 2 != 0:
            print(arr[i],arr[j])
            
#Find pairs of numbers from the array whose product is equal to a given target value.

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if arr[i] * arr[j] == k:
            print(arr[i],arr[j])

#Print all pairs of numbers from the input array whose sum is greater than the sum value k.

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] > k:
            print(arr[i],arr[j])

#Print all pairs of numbers from the input array whose sum is less than the target value k.

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] < k:
            print(arr[i],arr[j])

#Count the number of all possible pairs that can be formed from the given array.

n = int(input())
arr = list(map(int,input().split()))

count = 0

for i in range(n):
    for j in range(i+1,n):
        count += 1

print(count)

#Print all pairs of numbers from a given array where the sum of the pair is a prime number

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        total = arr[i] + arr[j]
        prime = True

        if total < 2:
            prime = False
        else:
            for k in range(2,total):
                if total % k == 0:
                    prime = False
                    break

        if prime:
            print(arr[i],arr[j])
            
#Given an array of integers of size N, print all the elements which are odd.

n = int(input())
arr = list(map(int,input().split()))

odd = []
for x in arr:
    if x%2 != 0 :
        odd.append(x)

if len(odd) == 0:
    print("None")
else:
    print(*odd) 

#Given an array, rotate the array to the right by k steps, where k is non-negative.

n,k = map(int,input().split())
arr = list(map(int,input().split()))

k = k % n

if k == 0:
    print(*arr)
else:
    print(*(arr[-k:] + arr[:-k]))


#Given an array of integers of size N, find and display the 
# second largest element present in the array

n = int(input())
arr = list(map(int,input().split()))

arr.sort()

print(arr[-2])

Pairs with First Value Smaller
Description
Print all pairs of numbers from a given array where the first value is strictly smaller than the second value.

Input Format
The input consists of a single line containing the length of the array, followed by a second line containing space-separated integers.

Output Format
Print each pair of numbers on a new line, separated by a space.

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            print(arr[i],arr[j])

#Given an array of integers and a value k, write a program to reverse the array starting from index k to the end of the array.

n ,k = map(int,input().split())
arr = list(map(int,input().split()))

arr[k:] = arr[k:][::-1]

print(*arr)


#Given an array of integers, your task is to find and print the sum of the largest and smallest elements in the array.

n = int(input())
arr = list(map(int,input().split()))

print(min(arr) + max(arr))

#Given an array of size N, print all the pairs present in the array.

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        print(arr[i],arr[j])

#Given an array of size N, print the sum of each pair present in the array.

n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        print(arr[i]+arr[j])

#Given an array of size N, print the difference of each pair present in the array.

n = int(input())
arr = list(map(int,input().split()))

if n < 2:
    print("None")
else:
    for i in range(n):
        for j in range(i+1,n):
            print(abs(arr[i]-arr[j]))

#Given an array of integers with a size of N, print all the pairs whose sum is less than K.

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] < k:
            print(arr[i],arr[j])

#Given an array of size N, print all the pairs whose first value is greater than K.

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

found = 

for i in range(n):
    for j in range(i+1,n):
        if arr[i] > k:
            print(arr[i],arr[j])

Input Format
The first line contains two integers N and S, where N is the size of the array 'ARR' and S is the required sum.

The second line contains N space-separated integers representing the array 'ARR'.

Output Format
Print each pair on a new line, where each pair consists of two integers separated by a space.

n,m = map(int,input().split()
arr = list(map(int,input().split()))

pairs = []

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == m:
            a = min(arr[i],arr[j])
            b = max(arr[i],arr[j])
            pairs.append((a,b))

pairs.sort()

for a,b in pairs:
    print(a,b)

#Input Format
#The first line contains integers representing the nodes of the first linked list, ending with -1 to signify the end. The second line contains integers representing the nodes of the second linked list, ending with -1.

#Output Format
#Print the merged sorted linked list as space-separated integers, ending with -1.

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.remove(-1)
b.remove(-1)

c = a + b
c.sort()

print(*c, -1)

#Count the number of unique elements in an ascending sorted array.

n = int(input())
arr = list(map(int, input().split()))

count = 1
unique = 0

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        if count == 1:
            unique += 1
        count = 1

if count == 1:
    unique += 1
                                                
print(unique)   
















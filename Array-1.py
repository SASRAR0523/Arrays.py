# print all pairs in the array
'''
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

#Write a program to count the number of occurrences of each vowel and consonant in a given string. 
# Print the vowels first and then consonants in lexicological order along with their counts
 
s = input()

vowels = "aeiou"

for ch in vowels:
    if ch in s:
        print(ch, "-",s.count(ch))

for ch in sorted(set(s)):
    if ch not in vowels:
        print(ch, "-", s.count(ch))

#Find and print the second largest word present in the given string. 
# Words are separated by spaces, and the length of the word determines its size.

s = input()

words = s.split()

words.sort(key=len)

print(words[-2])

#Given a string s, find the first non-repeating character in it and
#return its index. If it does not exist, return -1.

s = input()

for i in range(len(s)):
    if s.count(s[i]) == 1:
        print(i)
        break

else:
    print(-1)

#Given a string, check if it is a valid palindrome ignoring consonant characters.
# A single string containing lowercase alphabets, numbers, and special characters.
# True if the string is a valid palindrome after ignoring consonant characters, 
# Special Characters and Spaces otherwise False.

s = input().lower()

vowels = "aeiou"
new = ""

for ch in s:
    if ch in vowels:
        new += ch

if new == new[::-1]:
    print("True")
else:
    print("False")

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

# Write a program to find factors of a given number.

# Input Format
# First line consists of a positive integer n

# Output Format
# Print the space separated integer factors of given number.

n = int(input())

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")

# Write a program to count factors of a given number.

# Input Format
# First line consists of a positive integer n

# Output Format
# Print the integer count.

n = int(input())

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count += 1

print(count)

#Counts the number of words in a given string[words might be separated by multiple space].

s = input()

words = s.split()

print(len(words))

#Given an array of integers and a value k, write a program to reverse the array starting from index k to the end of the array.

n ,k = map(int,input().split())
arr = list(map(int,input().split()))

arr[k:] = arr[k:][::-1]

print(*arr)
'''
#Given an array of integers, your task is to find and print the sum of the largest and smallest elements in the array.

n = int(input())
arr = list(map(int,input().split()))

print(min(arr) + max(arr))

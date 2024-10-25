def longestBitonicSubarray(arr):
    n = len(arr)
    
    # Initialize the increasing and decreasing arrays
    inc = [1] * n
    dec = [1] * n
    
    # Fill the increasing subarray lengths
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = inc[i-1] + 1
    
    # Fill the decreasing subarray lengths
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            dec[i] = dec[i+1] + 1
    
    # Find the maximum length of bitonic subarray
    max_len = 0
    for i in range(n):
        max_len = max(max_len, inc[i] + dec[i] - 1)
    
    return max_len



# Example usage
arr = [10, 8, 9, 15, 12, 6, 7]
print(longestBitonicSubarray(arr))  # Output: 5


a1 = [5,1,2,1,4,5]  #3
print(longestBitonicSubarray(a1))

a2 = [9,7,6,2,1]    #5
print(longestBitonicSubarray(a2))


a3 = [10, 9, 8, 9, 10]    #3
print(longestBitonicSubarray(a3))

print("---------")

def digit_sum(x):
    return sum(int(d) for d in str(x))

def lotteryCoupons(n):
    sum_count = {}
    
    # Calculate sum of digits for each coupon and count occurrences
    for i in range(1, n + 1):
        s = digit_sum(i)
        if s in sum_count:
            sum_count[s] += 1
        else:
            sum_count[s] = 1
    
    # Find the maximum frequency of any sum
    max_frequency = max(sum_count.values())
    
    # Count how many sums have this maximum frequency
    max_count = sum(1 for count in sum_count.values() if count == max_frequency)
    
    return max_count

# Example usage
n = 12
print(lotteryCoupons(n))  # Output: 3

print(lotteryCoupons(11))  # Output: 2

print(lotteryCoupons(22))  # Output: 3

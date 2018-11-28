#https://www.interviewbit.com/problems/find-duplicate-in-array/

import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A) - 1
        num_buckets= int(math.ceil(math.sqrt(n)))
        
        #Some HouseKeeping for num of buckets required
        largest = max(A)
        num_buckets_required = num_buckets
        if largest % num_buckets == 0:
            num_buckets_required = largest // num_buckets
        else:
            num_buckets_required = (largest // num_buckets) + 1
            
        bucket_count = [0]*num_buckets_required
        
        #Numbers fall in which bucket and their count
        for num in A:
            if num % num_buckets == 0:
                bucket_count[(num // num_buckets) -1 ] += 1
            else:
                bucket_count[num // num_buckets] += 1
                
        #Find the bucket which has elements greater than sqrt(n)
        bucket_with_repeated_element = -1
        threshold = num_buckets
        for idx, count in enumerate(bucket_count):
            
            #Threshold for last bucket should change as there wont be enough elements
            if idx == len(bucket_count) - 1:
                threshold = largest % num_buckets
                
            if count > threshold:
                bucket_with_repeated_element = idx
                break
        
        #If we have such bucket then hash the elements count 
        #which are present in that bucket
        if bucket_with_repeated_element >= 0:
            num_hash = {}
            for num in A:
                num_falls_in_bucket = -1
                if num % num_buckets == 0:
                    num_falls_in_bucket = (num // num_buckets) - 1
                else:
                    num_falls_in_bucket = (num // num_buckets)
                
                if num_falls_in_bucket == bucket_with_repeated_element:
                    if num in num_hash:
                        num_hash[num] += 1
                    else:
                        num_hash[num] = 1
             
            #iterating over hash and checking if count greater than 1
            for num, count in num_hash.iteritems():
                if count > 1:
                    return num
        else:
            return -1

#https://www.interviewbit.com/problems/merge-intervals/

import bisect

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        merged_intervals = []
        
        all_start = [i.start for i in intervals]
        all_end   = [i.end for i in intervals]
        
        #Finding where the starting/ending value of given interval lie
        start_interval_index = bisect.bisect_right(all_start, new_interval.start)
        end_interval_index   = bisect.bisect_left(all_end, new_interval.end)
        
        #determine four cases where they are and they we will proceed
        is_start_outside = False
        is_end_outside   = False
        
        if start_interval_index == 0:
            is_start_outside = True
        else:
            to_check_index = start_interval_index - 1
            if new_interval.start > intervals[to_check_index].end:
                is_start_outside = True
        
        if end_interval_index == len(all_end):
           is_end_outside = True
        else:
            to_check_index = end_interval_index
            if new_interval.end < intervals[to_check_index].start:
                is_end_outside = True
        
        #All four conditions
        if is_start_outside == False and is_end_outside == False:
            #print "in condition 1"
            merge_interval_start_index  = start_interval_index - 1
            merge_interval_end_index    = end_interval_index
            interval_obj = Interval(intervals[merge_interval_start_index].start, intervals[merge_interval_end_index].end)
            
            #merging the intervals
            for i in range(merge_interval_start_index):
                merged_intervals.append(intervals[i])
            merged_intervals.append(interval_obj)
            for i in range((merge_interval_end_index + 1), len(intervals)):
                merged_intervals.append(intervals[i])
            
            #print merged_intervals
        elif is_start_outside == False and is_end_outside == True:
            #print "In condition 2"
            merge_interval_start_index = start_interval_index - 1
            merge_interval_end_index   = end_interval_index
            interval_obj  = Interval(intervals[merge_interval_start_index].start, new_interval.end)
            
            #merging intervals
            for i in range(merge_interval_start_index):
                merged_intervals.append(intervals[i])
            merged_intervals.append(interval_obj)
            for i in range(merge_interval_end_index, len(intervals)):
                merged_intervals.append(intervals[i])
            
            #print merged_intervals
        elif is_start_outside == True and is_end_outside == False:
            #print "in condition 3"
            merge_interval_start_index = start_interval_index
            merge_interval_end_index   = end_interval_index
            interval_obj = Interval(new_interval.start, intervals[merge_interval_end_index].end)

            for i in range(merge_interval_start_index):
                merged_intervals.append(intervals[i])
            merged_intervals.append(interval_obj)
            for i in range(merge_interval_end_index + 1, len(intervals)):
                merged_intervals.append(intervals[i])
            
        elif is_start_outside == True and is_end_outside == True:
            merge_interval_start_index = start_interval_index
            merge_interval_end_index   = end_interval_index
            interval_obj = new_interval
            
            for i in range(merge_interval_start_index):
                merged_intervals.append(intervals[i])
            merged_intervals.append(interval_obj)
            for i in range(merge_interval_end_index , len(intervals)):
                merged_intervals.append(intervals[i])
            
            #print merged_intervals
        
        return merged_intervals

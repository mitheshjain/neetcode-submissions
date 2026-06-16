"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times=[item.start for item in intervals]
        end_times=[item.end for item in intervals]
        start_times.sort()
        end_times.sort()
        if not intervals:
            return 0
        if len(intervals)==1:
            return 1
        count=0
        s=e=0
        maxRooms=0
        while s < len(intervals):
            
            if start_times[s]<end_times[e]:
                count+=1
                s+=1

            else:
                e+=1
                count=count-1
            maxRooms=max(maxRooms,count)
        
        return maxRooms

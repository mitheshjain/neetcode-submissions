"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        if not intervals or len(intervals)==1:
            return True
        previous = intervals[0]

        for i in range(1,len(intervals)):
            current=intervals[i]
            if current.start<previous.end:
                return False
            previous=current
        return True
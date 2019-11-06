#Given a collection of intervals, merge all overlapping intervals.

#For example:
#Given [1,3],[2,6],[8,10],[15,18],

#return [1,6],[8,10],[15,18].

#Make sure the returned intervals are sorted.

def merge_overlapping_intervals(intervals):
  i = 0 
  while i < len(intervals) - 1:
    if intervals[i][1] > intervals[i+1][0] and intervals[i][1] < intervals[i+1][1]:
      start = intervals[i][0]
      end = intervals[i+1][1]
      intervals.pop(i+1)
      intervals.pop(i)
      intervals.insert(i, [start, end])
    else:
      i += 1
  return intervals


#Test

testing_intervals = [[1,3], [2,6], [8,10], [15,18]]

print(merge_overlapping_intervals(testing_intervals))
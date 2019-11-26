#Given two sorted integer arrays nums1 and nums2,
#merge nums2 into nums1 as one sorted array.

def merge_sorted_list(nums1, nums2):
  index_nums1 = 0
  index_nums2 = 0
  
  while (index_nums2 < len(nums2)):
    if nums2[index_nums2] <= nums1[index_nums1] or nums1[index_nums1] == 0:
      nums1.insert(index_nums1, nums2[index_nums2])
      nums1.pop()
      index_nums2 += 1
    else:
      index_nums1 += 1
      
  return nums1

merge_sorted_list([1,2,3,0,0,0],[2,5,6])
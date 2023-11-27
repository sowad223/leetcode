# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         k=set(nums1)
#         k1=set(nums2)
#         result = []
#         for i in nums1:
#             if i not in result:
#                  if i in nums2:
#                     result.append(i)
#         return result
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def find_intersection_recursive(nums1, nums2, index, result):
            if index < len(nums1):
                if nums1[index] in nums2 and nums1[index] not in result:
                    result.append(nums1[index])
                find_intersection_recursive(nums1, nums2, index + 1, result)

        result = []
        find_intersection_recursive(nums1, nums2, 0, result)
        return result  
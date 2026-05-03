class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1.reverse()

        l, r = n, m + n - 1
        while l < r:
            nums1[l], nums1[r] = nums1[r], nums1[l]
            l += 1
            r -= 1
        
        idx = 0
        l1, l2 = n, 0

        while idx < m + n:
            if l1 < m + n and l2 < n:
                if nums1[l1] < nums2[l2]:
                    nums1[idx] = nums1[l1]
                    l1 += 1
                else:
                    nums1[idx] = nums2[l2]
                    l2 += 1
            elif l2 < n:
                nums1[idx] = nums2[l2]
                l2 += 1
            else:
                nums1[idx] = nums1[l1]
                l1 += 1
            idx += 1
        

        


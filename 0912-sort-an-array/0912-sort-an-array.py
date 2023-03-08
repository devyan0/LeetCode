class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def _sift_up(arr):
            i = len(arr)-1
            p = (i-1) // 2
            while 0 <= p:
                if arr[i] < arr[p]:
                    arr[i], arr[p] = arr[p], arr[i]
                i = p
                p = (p-1) // 2
        
        def _sift_down(arr):
            i = 0
            while 2*i+1 < len(arr):
                l, r = 2*i+1, 2*i+2
                child = l
                if r < len(arr) and arr[r] < arr[l]:
                    child = r
                
                if arr[i] > arr[child]:
                    arr[i], arr[child] = arr[child], arr[i]
                
                i = child
        
        def push(arr, k):
            arr.append(k)
            _sift_up(arr)
        
        def pop(arr):
            if not arr:
                return
            if len(arr) == 1:
                return arr.pop()
            root = arr[0]
            arr[0] = arr.pop()
            _sift_down(arr)
            return root
        
        heap, res = [], []
        for n in nums:
            push(heap, n)
        
        while heap:
            res.append(pop(heap))

        return res

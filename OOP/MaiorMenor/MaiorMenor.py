class MaiorMenor (object):
    nums = []

    def __init__(self, nums):
        self.nums = nums

    
    def maior(self):
        return max(self.nums)
    
    def menor(self):
        return min(self.nums)
class Media(object):

    nums = []


    def __init__(self, nums):
        self.nums = nums
        

    def mediaPonderada(self):
        
        numerador = 0
        denominador = 0
    
        for i in range(len(self.nums)):
            if i >= 1 and i < len(self.nums)-1:
                numerador += self.nums[i] * 0.1
                denominador += 0.1
            else:
                numerador += self.nums[i] * 0.3
                denominador += 0.3

        return numerador/denominador          
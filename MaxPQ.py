import math
import random

class MaxPQ:

    def __init__(self, size):
        self.array = (size + 1) * [None]
        self.N = 0
    
    def insert(self, swimming_key):
        self.N += 1
        if self.N == len(self.array):
            self.array = self.array + (self.N * [None])
        self.array[self.N] = swimming_key
        swimming_index = self.N 
        if swimming_index > 1:
            continue_swimming = True
            while continue_swimming:
                parent_index = swimming_index // 2
                if parent_index >= 1:
                    if self.array[swimming_index] > self.array[parent_index]:
                        tmp = self.array[parent_index]
                        self.array[parent_index] = swimming_key
                        self.array[swimming_index] = tmp
                        swimming_index = parent_index
                    else:
                        continue_swimming = False
                else:
                    continue_swimming = False

    def del_max(self):
        output_int = self.array[1]
        if self.N == 1:
            self.array[1] = None
            self.N -= 1
        else:
            sinking_key = self.array[self.N]
            self.array[1] = sinking_key
            self.array[self.N] = None
            self.N -= 1
            if self.N < len(self.array) / 4:
                self.array = self.array[ : math.ceil(len(self.array) / 2)  ]
            sinking_key_index = 1
            left_child_index = 2 * sinking_key_index
            right_child_index = left_child_index + 1
            continue_sinking = True
            while continue_sinking:
                
                if not left_child_index > self.N and not right_child_index > self.N:
            #        print('self.N ' + str(self.N))
            #        print('sinking key ' + str(sinking_key_index))
            #        print('left ' + str(left_child_index))
            #        print('right ' + str(right_child_index))
            #        print('value of sinking key ' + str(self.array[sinking_key_index]) )
            #        print('value of left child ' + str(self.array[left_child_index]))
            #        print('value of right child ' + str(self.array[right_child_index]))

                    if self.array[sinking_key_index] < max(self.array[left_child_index], self.array[right_child_index]):

                        if self.array[left_child_index] > self.array[right_child_index]:
                            tmp = self.array[left_child_index]
                            self.array[left_child_index] = sinking_key
                            self.array[sinking_key_index] = tmp
                            sinking_key_index = left_child_index

                        else:
                            tmp = self.array[right_child_index]
                            self.array[right_child_index] = sinking_key
                            self.array[sinking_key_index] = tmp
                            sinking_key_index = right_child_index
                    
                    else:        
                        continue_sinking = False

                elif not left_child_index > self.N:
                    if self.array[sinking_key_index] < self.array[left_child_index]:
                        tmp = self.array[left_child_index]
                        self.array[left_child_index] = sinking_key
                        self.array[sinking_key_index] = tmp
                        sinking_key_index = left_child_index

                    else:
                        continue_sinking = False            
                    
                elif not right_child_index > self.N:
                    if self.array[sinking_key_index] < self.array[right_child_index]:
                        tmp = self.array[right_child_index]
                        self.array[right_child_index] = sinking_key
                        self.array[sinking_key_index] = tmp
                        sinking_key_index = left_child_index

                    else:
                        continue_sinking = False
                else:
                    continue_sinking = False
                
                if sinking_key_index >= self.N:
                    continue_sinking = False
                left_child_index = 2 * sinking_key_index
                right_child_index = left_child_index + 1

        return output_int

    def show_maxpq(self):
        return self.array
    
    def show_self_N(self):
        return self.N
    
    def is_empty(self):
        if self.N > 0:
            return False
        else:
            return True

input_list = list(range(100, 200))

random.shuffle(input_list)

tim_MaxPQ = MaxPQ(10)

for x in input_list:
    tim_MaxPQ.insert(x)

while not tim_MaxPQ.is_empty():

    print(str(tim_MaxPQ.show_self_N()) + ' ' + str(tim_MaxPQ.del_max()) ) 

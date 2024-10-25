from decimal import Decimal
import random


class Qualean (object):

    def __init__(self, real_num):
        '''
        Inspired by Boolean + Quantum concepts. 
        We can assign it only 3 possible real states.

        True, False, and Maybe (1, 0, -1). 
        But it internally picks an imaginary state, an imaginary number random.uniform(-1, 1).

        It multiplies real number with imaginary number 
        and stores that 'magic' number internally 
        after using Bankers rounding to 10th decimal place.
        '''



        # reject if input not in [-1,0,1]

        if real_num not in [-1, 0, 1]:
            raise ValueError ("Number not in [-1,0,1]") 
        self._real_num = real_num

        try:
            self._img_num = Decimal (random.uniform (-1, 1))
        except:
            raise ImportError ("Can't find module random")

        #_num is the actual qualean number

        self._num = 0

        # generate the actual number using below function

        self.magic_number()

    def magic_number (self):
        '''
        It multiplies the real with imaginary number. 
        It uses python math.round function 
        which internally uses banker's algorithm for rounding.
        '''

        self._num = round (self._real_num * self._img_num, 10)
        
    @property
    def imag (self):
        '''
        The randomly generated imaginary number
        '''
        return self._img_num

    @property
    def real (self):
        '''
        The real number as per input
        '''
        return self._real_num

    @property
    def qual(self):
        '''
        The qualean number
        '''
        return self._num
        
        
    def __repr__(self):
        return '{0}'.format(self._num)
        
        
    def __str__(self):
        return '{0}'.format(self._num)
        
        
    def __mul__(self, value):
        '''
        Return self * value
        '''
        # check if the object is qualean

        if isinstance (value, Qualean):
            return self._num * value._num

        return self._num * Decimal (value)


    def __add__(self, value):
        '''
        Return self + value
        '''
        # check if the object is qualean

        if isinstance (value, Qualean): 
            return self._num + value._num
        
        return self._num + Decimal (value)


    def __sqrt__(self):
        '''
        Return sqrt (self)
        '''
        # self._num is a Decimal type which has sqrt () as a func.
        return self._num.sqrt()



########


q = Qualean(1)
print(q)

print(q, ", ", q.imag, ", ", q.real, ", ", q.qual)

q_sum = q + 10

q_prod = q * 3

q_sqrt = q.__sqrt__()

print(f"{q_sum}, {q_prod}, {q_sqrt}")

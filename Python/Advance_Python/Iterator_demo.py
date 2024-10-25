# Iterator
# Iterators are objects where we can loop through a collection

# __iter__ : returns the object itself and inform that it is iterable
# __next__ : fetch next value, once all fetched, stop


class MyIterator:

    def __init__(self, limit) -> None:
        self.limit = limit
        self.current = 0

    
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.current < self.limit:
            self.current = self.current + 1
            return self.current
        else:
            raise StopIteration
        


my_iter_obj = MyIterator(3)


print(next(my_iter_obj))


for item in my_iter_obj:
    print(item)
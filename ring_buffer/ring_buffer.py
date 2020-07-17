# impliment this class as if it were a queue?
# overrides oldest value after set amount (capacity?)
# compare length of storage to capacity in conditions?

# Ring Buffer AKA Circular Buffer


class RingBuffer:
    def __init__(self, capacity):
        # data storage
        self.storage = []
        self.capacity = capacity
        # current data item
        self.current = 0

    #  adds a single element to the buffer
    def append(self, item):
        # if storage length is less than capacity
        if len(self.storage) < self.capacity:
            # add stuff to storage
            self.storage.append(item)
        # else add stuff to end and removing head?
        else:
            # current item in storage list is assigned as item
            self.storage[self.current] = item
            # increment
            self.current += 1
            # if current is greater than or equal to capacity
            if self.current >= self.capacity:
                # reset current value
                self.current = 0

    # returns ALL elements in the buffer
    # should NOT return any None values if they exist
    def get(self):
        # this passes the test, I guess there are no None test cases?
        return self.storage

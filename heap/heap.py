class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # insert item into the last spot in the array
        self.storage.append(value)

        # run bubble-up to sort the heap
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # grab the last item in the storage and save it to a variable
        last_item = self.storage.pop()
        
        # if there is a self.storage
        if self.storage:
            # store self.storage[0] in a variable to be deleted
            deleted = self.storage[0]
            # reassign self.storage[0] to be the last item, moving it to the front of the list
            self.storage[0] = last_item
            # run sift_down on starting on the new first index
            self._sift_down(0)
            # return the deleted item
            return deleted
        # if there is no self.storage
        else:
            # return the popped item
            return last_item

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # called as helper in insert
    # bubble up the newly inserted element to a valid spot in the heap
    def _bubble_up(self, index):
        # loop while the parent index is a valid heap index
        while (index - 1) // 2 >= 0:

            # child has access to parent at this point with this formula
            # compare the child value against it's parent's value
            # if childs value > parent's value
            if self.storage[(index - 1) // 2] < self.storage[index]:

                # swap these two elements via their indices
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]

            # repeat process until child no longer needs to be swapped w/ parent
            index = (index - 1) // 2

    #helper in delete

    def _sift_down(self, index):
        # loop as long as child index is less than the last index
        while index * 2 + 1 <= len(self.storage) - 1:

            # create variables for child indices
            left_child = index * 2 + 1
            right_child = index * 2 + 2

            # if index of right child is greater than the length of storage, or if
            # the left child value is greater than the right child value
            if right_child > len(self.storage) - 1 or self.storage[left_child] > self.storage[right_child]:
                # the bigger child is now the left child
                big_child = left_child

            # else the right child value is greater than the left child value
            else:
                # the bigger child is now the right child
                big_child = right_child

            # if the index value is less than the big child
            if self.storage[index] < self.storage[big_child]:
                # swap these two elements via their indices
                self.storage[index], self.storage[big_child] = self.storage[big_child], self.storage[index]
                # and then index is now big child
            index = big_child


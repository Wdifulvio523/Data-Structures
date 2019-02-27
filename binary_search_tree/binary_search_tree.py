class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # store variables for self, and a boolean
    current = self
    complete = False
    # Begin loop using the boolean == false
    while not complete:
    # compare values
        # if current val > val
        if current.value > value:
            # check if there is a left
            if current.left:
                # if there is a left, set the left to the new current
                current = current.left
            else:
                # if no left, set the new left to the value (create new BST node)
                current.left = BinarySearchTree(value)
                complete = True
        # if current val < val  
        else:
            # check if there is a right, same logic as above
            if current.right:
                current = current.right
            else:
                current.right = BinarySearchTree(value)
                complete = True


  def contains(self, target):
    
    current = self
    complete = False
    
    while not complete:
      
      # if there is nothing left to check, return false
      if not current:
        return False
      
      # if the value of the current node is == target, 
      if current.value == target:
        return True
      
      # if the current value is greater than the target 
      elif current.value > target:    
        current = current.left
      
      # if current value is less than the target 
      else:
        current = current.right
  
  def contains_class(self, target):
      # search BST for given target value, returning a boolean
      # check if target value matches self.value on the current node
        # if so, return True
      if self == target:
        return True
      # compare the target value against self.value
        # if target < self.value
      if target < self.value:
          # if self.left exists
          if self.left:
            # call the left child's contain method, passing in target val
            self.left.contains(target)
          # else return false
          else:
            return False 
        # if target > self.value
      if target > self.value:
          # if self.right exists
          if self.right:
            # call the right child's contain method, passing in target val
            self.right.contains(target)
          # else return false
          else:
            return False

  def get_max(self):
    current = self
    max = 0 
    
    while current:
            
      # if the current value is greater than the max  
      if current.value > max: 
        max = current.value   
        current = current.right

    return max

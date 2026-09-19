# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.nextIndex = 0
        self.nestedIterator = dict()
    
    def next(self) -> int:
        if not self.hasNext():
            return -1
        
        if self.nestedList[self.nextIndex].isInteger():
            i = self.nextIndex
            self.nextIndex += 1
            return self.nestedList[i].getInteger()
        
        i = self.nextIndex
        while i < len(self.nestedList):
            item = self.nestedList[i]
            if item.isInteger():
                self.nextIndex = i + 1
                return item.getInteger()
                break

            self.nestedIterator[i] = self.nestedIterator.get(i, NestedIterator(item.getList()))
            if self.nestedIterator[i].hasNext():
                return self.nestedIterator[i].next()
            i += 1
        
        return -1

    def hasNext(self) -> bool:
        if self.nextIndex >= len(self.nestedList):
            return False
        if self.nestedList[self.nextIndex].isInteger():
            return True
        
        i = self.nextIndex
        while i < len(self.nestedList):
            item = self.nestedList[i]
            if item.isInteger():
                return True

            self.nestedIterator[i] = self.nestedIterator.get(i, NestedIterator(item.getList()))
            if self.nestedIterator[i].hasNext():
                return True
            i += 1
        
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
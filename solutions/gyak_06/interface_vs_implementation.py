from abc import ABC, abstractmethod

################################################
##### Abstract Data Type (ADT) / Interface #####
################################################

class StackADT(ABC):
    @abstractmethod
    def push(self, item): pass

    @abstractmethod
    def pop(self): pass

    @abstractmethod
    def peek(self): pass

    @abstractmethod
    def is_empty(self): pass

##########################
##### Implementation #####
##########################

class ListStack(StackADT):
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop() if not self.is_empty() else None

    def peek(self):
        return self._data[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._data) == 0

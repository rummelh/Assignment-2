# Name: Hannah Rummel
# OSU Email: rummelh@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 2/6/2023
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        self._da.append(value)


    def remove(self, value: object) -> bool:
        """returns true if element is removed from array and false otherwise"""
        new_arr = DynamicArray()
        count = 0
        for i in range(self.size()):
            if self._da.get_at_index(i)==value and count == 0:
                count+=1
            else:
                new_arr.append(self._da.get_at_index(i))
        self._da = new_arr
        if count > 0:
            return True
        else: return False



    def count(self, value: object) -> int:
        """counts the number of that value in an array"""
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i)==value:
                count+=1
        return count


    def clear(self) -> None:
        """removes every element from an array"""
        empty_da = DynamicArray()
        self._da = empty_da

    def equal(self, second_bag: "Bag") -> bool:
        """tests to see if two bags are equal"""
        if self._da.length() != second_bag.size():
            return False
        if self._da.length() == 0 and second_bag.size()==0:
            return True
        for i in range(self._da.length()):
            count_1 = self.count(self._da.get_at_index(i))
            count_2 = second_bag.count(self._da.get_at_index(i))
            if count_1!= count_2:
                return False
        else: return True


    def __iter__(self):
        self._index = 0

        return self

    def __next__(self):
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration
        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# equal example 2")
    bag_6 = Bag([-73217, -52647, 65851, -94601, -98110, -88797, -13591, -14129, 50035, -50480, -76840])
    bag_7 = Bag([-94601, 50035, -50480, -13591, -88797, -98110, -33277, -52647, -73217, -14129, 65851])
    print(bag_6.equal(bag_7))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)

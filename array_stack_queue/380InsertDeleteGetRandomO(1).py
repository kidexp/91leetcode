import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_index_dict = {}
        self.value_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_index_dict:
            return False
        self.value_list.append(val)
        self.num_index_dict[val] = len(self.value_list) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_index_dict:
            return False
        val_index = self.num_index_dict[val]
        last_element = self.value_list[-1]
        self.value_list[val_index], self.value_list[-1] = (
            self.value_list[-1],
            self.value_list[val_index],
        )
        self.value_list.pop()
        self.num_index_dict.pop(val)
        if last_element != val:
            self.num_index_dict[last_element] = val_index
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.value_list[random.randint(0, len(self.value_list) - 1)]


if __name__ == "__main__":
    random_set= RandomizedSet()
    print(random_set.insert(1))
    print(random_set.remove(2))
    print(random_set.insert(2))
    print(random_set.num_index_dict, random_set.value_list)
    print(random_set.remove(1))
    print(random_set.insert(2))
    print(random_set.num_index_dict, random_set.value_list)
    print(random_set.remove(2))
    print(random_set.num_index_dict, random_set.value_list)

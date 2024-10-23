class SmallestInfiniteSet(object):

    def __init__(self):
        self.Num = set()
        for i in range(1, 1001):
            self.Num.add(i)

    def popSmallest(self):
        min_number = min(self.Num)
        self.Num.remove(min_number)
        return (min_number)
        

    def addBack(self, num):
        if not num in self.Num:
            self.Num.add(num)

def main():
    # Initialize the SmallestInfiniteSet
    smallest_set = SmallestInfiniteSet()

    # Pop the smallest numbers several times
    print("Popping smallest numbers:")
    for _ in range(5):
        print(smallest_set.popSmallest())  # Popping the smallest number

    # Add a number back to the set
    print("\nAdding number 3 back to the set.")
    smallest_set.addBack(3)

    # Pop the smallest number again to see if 3 is available
    print("Popping smallest numbers after adding back 3:")
    for _ in range(5):
        print(smallest_set.popSmallest())

if __name__ == "__main__":
    main()
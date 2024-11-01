class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        item_dict = {}
        
        for item, value in items1:
            if item in item_dict:
                item_dict[item] += value
            else:
                item_dict[item] = value

        for item, value in items2:
            if item in item_dict:
                item_dict[item] += value
            else:
                item_dict[item] = value

        # Convert the dictionary back to a sorted list of lists
        merged_items = [[item, value] for item, value in sorted(item_dict.items())]

        return merged_items


def main():
    # Create an instance of Solution
    sol = Solution()

    # Define the two lists of items
    items1 = [[1, 3], [2, 2], [4, 5]]
    items2 = [[3, 2], [2, 1], [1, 2]]

    # Call mergeSimilarItems
    result = sol.mergeSimilarItems(items1, items2)

    # Print the result
    print("Merged List of Items:")
    for item in result:
        print(item)

# Execute the main function
if __name__ == "__main__":
    main()
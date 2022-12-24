# Keep only the highest version in a text box from a list

This code defines a function called just_highest_version that takes in four arguments:

- **splitter:** a string that represents the separator used to split each element in the list.
- **n_splitter:** an integer that represents the position of the version name in the split element.
- **version:** an integer that represents the position of the version number in the split element.
- **list_to_split:** a list of strings that represent the elements that need to be processed.

## Code explanation

The function sorts the list_to_split in ascending order, and then creates an empty list called list_highest_version. It then initializes a variable called val to 0 and enters a loop that will run until val is equal to the length of list_to_split minus 1.

Inside the loop, the function initializes variables called max and maxInd to 0. It also splits the val-th element in list_to_split using the splitter separator and assigns the resulting list to a variable called group. It then splits the val-th element again and assigns the resulting list to a variable called element.

The function then enters another loop that will run as long as element[n_splitter] (the version name) is equal to group[n_splitter] (the version name of the first element in the group). Inside this loop, the function compares the version number stored in element[version] to the current maximum value stored in max. If element[version] is greater, the function updates max to the new maximum value and maxInd to the current index val.

After the inner loop completes, the function appends the element at index maxInd in list_to_split to list_highest_version. The outer loop then increments val by 1 and continues until val is no longer less than the length of list_to_split minus 1.

Finally, the function returns the list_highest_version list.

The purpose of this function is to keep only the highest version of each group of elements in list_to_split where the version name and number are located in a text box with separators. It does this by sorting the list, grouping the elements by version name, and then selecting the element with the highest version number within each group.

---

**Developed for Moko** - Thales Alenia Space

**Written by : Jean Guiraud**

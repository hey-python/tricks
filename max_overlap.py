"""
Consider a big party where a log register for guest’s entry and exit times is maintained.
Find the time at which there are maximum guests in the party.

Input:
arrs = [1, 2, 9, 5, 5]
exits = [4, 5, 12, 9, 12]
"""


def get_max_guest(arr1, arr2):
    arr1.sort()
    arr2.sort()

    present_guest = 0
    max_guest = 0
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr[i] <= arr2[j]:
            present_guest += 1

            if present_guest > max_guest:
                max_guest = present_guest

            i += 1
        else:
            present_guest -= 1
            j += 1

    return max_guest


if __name__ == '__main__':
    arr = [1, 2, 9, 5, 5]
    exits = [4, 5, 12, 9, 12]
    print(get_max_guest(arr, exits))

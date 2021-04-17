#!/usr/bin/env python
"""
This module was created to get to know the inner workings of the Merge Sort Algorithm.

Following along with a Course on Algorithms and Datastructures, this module shares similarity
with the coding examples shown in said course. The code was still written by me and there are
differences to the examples throughout. This particular file aims to rebuild the core functionality
of the Merge Sort Algorithm.
"""

__author__ = "Robin Wettstaedt"
__contact__ = "robinwettstadt@gmail.com"
__credits__ = "Course: Algorithms and Data Structures - Full Course for Beginners by teamtreehouse.com"
__date__ = "2021/04/17"
__deprecated__ = False
__email__ = "robinwettstadt@gmail.com"
__maintainer__ = "Robin Wettstaedt"
__status__ = "Pre-Alpha"
__version__ = "0.0.1"


def merge_sort(unsorted_list):
    """
    Sorts a List in ascending order
    returns a new sorted list, containing the values from undsorted list input
    Divide: Find midpoint if the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    :param unsorted_list:
    :return: new sorted list
    """

    # nothing to sort if number of elements in list is 0 or 1
    if len(unsorted_list) <= 1:
        return unsorted_list

    # dividing the input array
    left_half, right_half = split(unsorted_list)

    # recursive calls to further divide the (already divided) arrays
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # sorting a merging of both halfs
    return merge(left, right)


def split(unsorted_list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    :param unsorted_list
    :return: left, right (input list split in two halfs)
    """

    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    return left, right


def merge(left, right):
    """
    This functions merges two lists (arrays), sorting them in the process
    Returns a new merged list
    :param left (one half of the two lists that shall be sorted and merged together)
    :param right (other half of the two lists that shall be sorted and merged together)
    :return new merged, sorted list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(sorted_list):
    """
    Verifies if a given list is sorted
    by recursively checking the first and second element of it
    :param sorted_list (a list that is (supposedly) sorted)
    :return Boolean (True if sorted, False if not)
    """
    if len(sorted_list) <= 1:
        return True

    return sorted_list[0] <= sorted_list[1] and verify_sorted(sorted_list[1:])


def testing():
    """
    Includes calling of the necessary functions to check if the merge sort works as intended.
    An exemplary list is created and its sorted status is checked before and after applying the Algorithm.
    """
    example_list = [59, 48, 50, 17, 14, 14, 44, 33, 22]
    print(example_list)
    print(f"The sorted status of the given list is: {verify_sorted(example_list)}")
    print(merge_sort(example_list))
    print(f"The sorted status of the given list is: {verify_sorted(merge_sort(example_list))}")

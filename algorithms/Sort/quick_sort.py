class Solution:
    def quicksort(self, arr):
        '''
        :type arr: list of int
        :rtype: list of int
        '''
        self.quicksort_helper(arr, 0, len(arr) - 1)

        return arr

    # Helper function for recursively doing the quicksort
    # quicksort will be called recursively for the elemnts to the left of pivot
    # And the elements to the right of pivot
    def quicksort_helper(self, arr, left, right):
        if left < right:
            # Find the position of pivot
            pivot_final_resting_position = self.partition(arr, left, right)

            # Recursively call left and right subarray to the pivot
            self.quicksort_helper(arr, left, pivot_final_resting_position - 1)
            self.quicksort_helper(arr, pivot_final_resting_position + 1, right)

    # Helper function to perform the partition
    def partition(self, arr, left, right):

        # Here we make the right most element as pivot
        pivot = arr[right]

        # We re-arrange the array such that
        # The elements smaller than the pivot are at left to the pivot
        # And The elements greater than the pivot are at right to the pivot
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1

                self.swap(arr, i, j)

        # The pivot comes to its correct position
        self.swap(arr, i + 1, right)

        # Return the pivot's final resting position
        return i + 1

    # Helper function to swap elements at 2 different array indices
    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp


class OtherSolution:
    # This Function handles sorting part of quick sort
    # start and end points to first and last element of
    # an array respectively
    def partition(self, start, end, array):
        # Initializing pivot's index to start
        pivot_index = start
        pivot = array[pivot_index]

        # This loop runs till start pointer crosses
        # end pointer, and when it does we swap the
        # pivot with element on end pointer
        while start < end:

            # Increment the start pointer till it finds an
            # element greater than pivot
            while start < len(array) and array[start] <= pivot:
                start += 1

            # Decrement the end pointer till it finds an
            # element less than pivot
            while array[end] > pivot:
                end -= 1

            # If start and end have not crossed each other,
            # swap the numbers on start and end
            if start < end:
                array[start], array[end] = array[end], array[start]

        # Swap pivot element with element on end pointer.
        # This puts pivot on its correct sorted place.
        array[end], array[pivot_index] = array[pivot_index], array[end]

        # Returning end pointer to divide the array into 2
        return end

    def quick_sort(self, start, end, array):
        if start < end:
            # p is partitioning index, array[p]
            # is at right place
            p = self.partition(start, end, array)

            # Sort elements before partition
            # and after partition
            self.quick_sort(start, p - 1, array)
            self.quick_sort(p + 1, end, array)
        return array


class MySolution:
    def run(self, nums):
        return self.quick_sort(0, len(nums) - 1, nums)

    def quick_sort(self, start, end, array):
        if start < end:
            # Find position of the pivot
            pivot_final_resting_position = self.partition(start, end, array)
            self.quick_sort(start, pivot_final_resting_position - 1, array)
            self.quick_sort(pivot_final_resting_position + 1, end, array)

        return array

    def partition(self, start, end, array):
        partitioning_index = 0
        return partitioning_index


# def _quicksort(arr):
#     return quick_sort(arr, 0, len(arr) - 1)
# def quick_sort(arr, left, right):
#     if left < right:
#         Find the position of pivot
        # pivot_final_resting_position = partition(arr, left, right)
        # Recursively call left and right subarray to the pivot
        # quick_sort(arr, left, pivot_final_resting_position - 1)
        # quick_sort(arr, pivot_final_resting_position + 1, right)
    # return arr
# Helper function to perform the partition
# def partition(arr, left, right):
    # Here we make the right most element as pivot
    # middle = (left + right) // 2
    # pivot = arr[middle]
    # We re-arrange the array such that
    # The elements smaller than the pivot are at left to the pivot
    # And The elements greater than the pivot are at right to the pivot
    # i = left - 1
    # for j in range(left, right):
    #     if arr[j] <= pivot:
    #         i += 1
            # swap(arr, i, j)
    # The pivot comes to its correct position
    # swap(arr, i + 1, right)
    # Return the pivot's final resting position
    # return i + 1
    # Helper function to swap elements at 2 different array indices
# def swap(arr, first, second):
#     arr[first], arr[second] = arr[second], arr[first]
#
# def quicksort(nums):
#     return quicksort(nums)

def quick_sort(arr, begin, end):
    if begin < end:
        partition_index = partition(arr, begin, end)
        quick_sort(arr, begin, partition_index - 1)
        quick_sort(arr, partition_index + 1, end)

def partition(arr, begin, end):
    pivot = arr[begin]
    pivot_index = begin


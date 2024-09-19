Quicksort algorithm Implementation, Analysis and Randomization

This Assignment focuses on the Quicksort algorithm, its implemenetation, performance analysis, and a randomized version.

'quicksort.py': contains Quicksort implementationfor selecting a pivot, partitioning the array, and recursively sorting the subarrays.

'randomized_quicksort.py': contains a randomized version of Quicksort where the pivot is chosen randomly from the subarray.

'quicksort_comparison.py': contains the logic to empirically compare the running time of the deterministic and randomized versions of Quicksort on different inout sizes and distributions.

prerequisites:

python3.x

Run the code:

To run above files below are the commands:

python quicksort.py

python randomized_quicksort.py

python quicksort_comparison.py

sample output for quicksort.py:

python -u "/home/manasa/vscode_projects/Quicksort_algorithm/quicksort.py"

Sorted array: [1, 5, 7, 8, 9, 10]

sample output for randomized_quicksort.py:

python -u "/home/manasa/vscode_projects/Quicksort_algorithm/randomized_quicksort.py"

Sorted array: [4, 6, 25, 30, 41, 54]

sample output for quicksort_comparison.py:

python -u "/home/manasa/vscode_projects/Quicksort_algorithm/quicksort_comparison.py"

Array Size: 100

Random Array:

Deterministic Quicksort Time: 0.000071 seconds

Randomized Quicksort Time: 0.000097 seconds

Sorted Array:

Deterministic Quicksort Time: 0.000259 seconds

Randomized Quicksort Time: 0.000114 seconds

Reverse Sorted Array:

Deterministic Quicksort Time: 0.000258 seconds

Randomized Quicksort Time: 0.000104 seconds

Array Size: 1000

Random Array:

Deterministic Quicksort Time: 0.000806 seconds

Randomized Quicksort Time: 0.001253 seconds

This project is licensed under the MIT License. See the LICENSE file for details.

from time import *
import reverse_join_reversed
import reverse_loop_appending_for
import reverse_loop
import reverse_recursion
import reverse_slicing

def measure_time(func, str):
    start_time = time()
    func(str)
    end_time = time()
    execution_time = end_time - start_time
    return execution_time * 1000

str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print("reverse_join_reversed: ", measure_time(reverse_join_reversed.solution, str))
print("reverse_loop_appending_for: ", measure_time(reverse_loop_appending_for.solution, str))
print("reverse_loop: ", measure_time(reverse_loop.solution, str))
print("reverse_recursion 1: ", measure_time(reverse_recursion.solution1, str))
print("reverse_recursion 2: ", measure_time(reverse_recursion.solution2, str))
print("reverse_slicing: ", measure_time(reverse_slicing.solution, str))

# homework
# --------------------------------------
# run the test on multiple different strings saved in strings.txt
# measure the average result for each solution
# save results to the dictionary
# save the dictionary to txt file
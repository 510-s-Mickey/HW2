"""
This is a script to random array
"""
import subprocess

def random_array(arr):
    """
    Function to generate random array
    """
    for index, _ in enumerate(arr):
        # Adding check=True to ensure errors are caught
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[index] = int(shuffled_num.stdout)
    return arr

"""
This file is used to test rand
"""

from unittest.mock import patch
from rand import random_array

@patch('subprocess.run')
def test_random_array(mock_subprocess_run):
    """
    Test the random_array function
    """
    # Mocking the output of subprocess.run
    mock_subprocess_run.return_value.stdout = b'10'

    # Define an input array of length 5 with None values
    input_array = [None] * 5

    # Call the function to be tested
    result_array = random_array(input_array)

    # Ensure that the result array is filled with integer 10 (from the mocked subprocess output)
    assert result_array == [10, 10, 10, 10, 10]

    # Verify that subprocess.run was called 5 times (once for each element in the array)
    assert mock_subprocess_run.call_count == 5

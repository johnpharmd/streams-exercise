from io import StringIO
from random import choice


def make_random_digit_string():
    rand_string_list = []
    zero_to_nine = [i for i in range(10)]
    for i in range(40):
        rand_string_list.append(str(random.choice(zero_to_nine)))
    return ''.join(rand_string_list)


class StreamProcessor():
    
    
    def __init__(self, stream):
        self._stream = stream
    

    def process(self):
        """
        TODO: Implement the `process` method, as described above.
        
        :return: int
        """

        count = 0  # How many two-digit numbers the `process` method has added
                   # together.
        total = 0  # The running total of sums.

        # TODO: WRITE CODE HERE:

        # Just some example syntax, you can read two digits from the head of the
        # stream using the following code:
        #
        # digits = self._stream.read(2)
        while total < 200 and count < 10:
            two_digits = self._stream.read(2)
            if len(two_digits) < 2:
                break
            
            count += 1
            two_digits = int(two_digits)
            total += two_digits
                
        return count


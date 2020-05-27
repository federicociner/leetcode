"""Design a hit counter which counts the number of hits received in the past 5
minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you
may assume that calls are being made to the system in chronological order (ie,
the timestamp is monotonically increasing). You may assume that the earliest
timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Follow up:

    What if the number of hits per second could be very large? Does your design
    scale?

"""
from collections import defaultdict


# Dictionary
class HitCounterDictionary:
    def __init__(self):
        """Initialize your data structure here. """
        self.counter = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """ Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).

        """
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).

        """
        count = 0

        for k, v in self.counter.items():
            if timestamp - k >= 300:
                self.counter[k] = 0
            else:
                count += self.counter[k]

        return count


# Scalable with array
class HitCounter:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def __init__(self):
        """Initialize your data structure here. """
        self.timestamps = [0 for i in range(300)]
        self.hits = [0 for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """ Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).

        """
        index = timestamp % 300

        if self.timestamps[index] != timestamp:
            self.timestamps[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        """Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).

        """
        count = 0

        for i in range(len(self.timestamps)):
            if timestamp - self.timestamps[i] < 300:
                count += self.hits[i]
        return count


if __name__ == "__main__":
    counter = HitCounter()

    # Example 1
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)

    assert counter.getHits(4) == 3

    counter.hit(300)

    assert counter.getHits(300) == 4
    assert counter.getHits(301) == 3

    print("All tests passed.")

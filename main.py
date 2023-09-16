from collections import Counter
from heapq import heapify, heappop, heappush
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    ch: Optional[str]
    freq: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __lt__(self, other):
        return self.freq < other.freq

def get_huffman_tree(text):
    if not text:
        return
    freq = Counter(text)
    pq = [Node(k, v) for k, v in freq.items()]
    heapify(pq)
    while len(pq) > 1:
        left, right = heappop(pq), heappop(pq)
        new_freq = left.freq + right.freq
        heappush(pq, Node(None, new_freq, left, right))
    return pq[0]

print(get_huffman_tree('AADDDDDBBBE'))

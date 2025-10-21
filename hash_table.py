from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Tuple, Optional, Iterable

@dataclass
class Record:
    mode: str  # "Product" or "Item"
    id: int
    name: str
    price: Optional[float] = None   # para sa Product
    description: Optional[str] = None  # para sa Item
    key: Optional[int] = None
    hash_index: Optional[int] = None

class HashTable:
    """
    Separate yung hash table sa dynamic resizing
    h(k) = k mod m
    """
    def __init__(self, initial_capacity: int = 11, max_load_factor: float = 0.75) -> None:
        self._capacity = self._next_prime(max(11, initial_capacity))
        self._buckets: List[List[Tuple[int, Record]]] = [[] for _ in range(self._capacity)]
        self._size = 0
        self._max_load = max_load_factor

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size

    @property
    def load_factor(self) -> float:
        return self._size / self._capacity if self._capacity else 0.0

    def _hash(self, k: int) -> int:
        return k % self._capacity

    def insert(self, key: int, record: Record) -> None:
        if key is None:
            raise ValueError("Key must not be None")
        idx = self._hash(key)
        bucket = self._buckets[idx]
        # Upsert behavior
        for i, (k, rec) in enumerate(bucket):
            if k == key:
                record.key = key
                record.hash_index = idx
                bucket[i] = (key, record)
                return
        record.key = key
        record.hash_index = idx
        bucket.append((key, record))
        self._size += 1
        if self.load_factor > self._max_load:
            self._resize(self._next_prime(self._capacity * 2))

    def get(self, key: int) -> Optional[Record]:
        idx = self._hash(key)
        for k, rec in self._buckets[idx]:
            if k == key:
                return rec
        return None

    def remove(self, key: int) -> bool:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def items(self) -> Iterable[Record]:
        for bucket in self._buckets:
            for _, rec in bucket:
                yield rec

    def clear(self) -> None:
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def _resize(self, new_capacity: int) -> None:
        old_items = list(self.items())
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for rec in old_items:
            self.insert(rec.id, rec)

    @staticmethod
    def _next_prime(n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        candidate = n if n % 2 else n + 1
        while not is_prime(candidate):
            candidate += 2
        return candidate

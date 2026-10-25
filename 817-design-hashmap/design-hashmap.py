class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
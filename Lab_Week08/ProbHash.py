from Student import *


class ProbHash:
    def __init__(self, cap):
        self.hashTable = cap * [None]
        self.n = cap

    def hashFunction(self, myKey):
        return myKey % self.n

    def rehashFunction(self, hashKey):
        return (hashKey + 1) % self.n

    def searchData(self, key):
        idx_counter = 0
        student_obj: Student = None
        for student in self.hashTable:
            idx_counter += 1
            if (student is None):
                continue
            if (student.id == key):
                student_obj = student
                break
        if (student_obj is not None):
            print("Found", key, "at index: ", idx_counter - 1)
            return student_obj
        else:
            print(key, "does not exist")

    def insertData(self, student_obj: Student):
        student_id = student_obj.id
        hash_idx = self.hashFunction(student_id)
        while (self.hashTable[hash_idx] is not None):
            hash_idx = self.rehashFunction(student_id)
        self.hashTable[hash_idx] = student_obj
        print("Inserted", student_obj.getId(), "at index: ", hash_idx)

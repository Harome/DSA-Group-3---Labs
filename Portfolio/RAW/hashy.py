from prettytable import PrettyTable

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size

    def insert(self, key, data):
        hash_value = hash(data) % self.size
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, data)
        else:
            # Handle collisions using linear probing
            while self.table[hash_value] is not None:
                hash_value = (hash_value + 1) % self.size
            self.table[hash_value] = (key, data)

    def delete(self, key):
        hash_value = key % self.size
        if self.table[hash_value] is not None and self.table[hash_value][0] == key:
            self.table[hash_value] = None
            print(f"Deleted key {key}")
        else:
            print(f"Key {key} not found")

    def display_table(self):
        table = PrettyTable()
        table.field_names = ["Index", "Key", "Data", "Hash Code"]
        for i, item in enumerate(self.table):
            if item is not None:
                key, data = item
                table.add_row([i, key, data, hash(data) % self.size])
        print(table)

# Example usage:
hash_table = HashTable(32)

# Insertion
hash_table.insert(hash("example1") % 32, "example1")
hash_table.insert(hash("example2") % 32, "example2")
hash_table.insert(hash("example3") % 32, "example3")

# Display
print("After Insertion:")
hash_table.display_table()

# Deletion
hash_table.delete(hash("example2") % 32)

# Display after deletion
print("\nAfter Deletion:")
hash_table.display_table()

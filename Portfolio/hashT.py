from prettytable import PrettyTable

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size

    def hash_function_3(self, key):
        return hash(key) % self.size

    def insert(self, key, data, hash_function):
        if hash_function == 1:
            hash_value = self.hash_function_1(key)
        elif hash_function == 2:
            hash_value = self.hash_function_2(key)
        else:
            hash_value = self.hash_function_3(data)

        if self.table[hash_value] is None:
            self.table[hash_value] = [(key, data)]
        else:
            self.table[hash_value].insert(0, (key, data))

    def delete(self, key, hash_function):
        if hash_function == 1:
            hash_value = self.hash_function_1(key)
        elif hash_function == 2:
            hash_value = self.hash_function_2(key)
        else:
            hash_value = self.hash_function_3(key)

        if self.table[hash_value] is not None:
            for i, (stored_key, stored_data) in enumerate(self.table[hash_value]):
                if stored_key == key:
                    del self.table[hash_value][i]
                    print(f"Deleted key {key}")
                    return
        print(f"Key {key} not found")

    def display_table(self):
        table = PrettyTable()
        table.field_names = ["Index", "Key", "Data", "Hash Code"]
        for i, stack in enumerate(self.table):
            if stack is not None:
                for item in stack:
                    table.add_row([i, item[0], item[1], self.hash_function_3(item[1]) % self.size])
        return table.get_html_string()

    def reset_table(self):
        self.table = [None] * self.size

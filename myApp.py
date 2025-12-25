import json
import os

class KeyValueStore:
    def __init__(self, db_path="database.json"):
        self.db_path = db_path
        self.store = {}
        self._load()

    def _load(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                try:
                    self.store = json.load(f)
                except:
                    self.store = {}

    def _save(self):
        with open(self.db_path, "w") as f:
            json.dump(self.store, f, indent=4)

    def set(self, key, value):
        self.store[key] = value
        self._save()
        print(f"'{key}' saved with value: {value}")

    def get(self, key):
        if key in self.store:
            return self.store[key]
        return f"key '{key}' not found."

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            self._save()
            print(f"key '{key}' deleted.")
        else:
            print(f"key '{key}' does not exist.")

    def show(self):
        if self.store:
            print("Available data:")
            for k, v in self.store.items():
                print(f"{k} : {v}")
        else:
            print("there is no data")


if __name__ == "__main__":
    db = KeyValueStore()

    while True:
        print("select one of the operations: set, get, delete, show, exit")
        action = input("insert operation: ").strip().lower()

        if action == "set":
            key = input("insert key: ")
            value = input("insert value: ")
            db.set(key, value)

        elif action == "get":
            key = input("insert key: ")
            print("value: ", db.get(key))

        elif action == "delete":
            key = input(" insert key: ")
            db.delete(key)

        elif action == "show":
            db.show()

        elif action == "exit":
            print("Exit the program...")
            break

        else:
            print("The operation is invalid! Please try again")

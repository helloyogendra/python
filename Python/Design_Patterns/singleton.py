class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 == s2)  # Output: True, both are the same instance

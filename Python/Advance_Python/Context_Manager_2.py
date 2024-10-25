# Context Manager
# Releasing Resource automatically

# Custom Context Manager

# to define a custom context manager so it can be used with 'with' clause
# we need to implement two magic methods
# __enter__
# __exit__

# Example - 1
# Custom File Manager - Context manager

class FileManager:

    def __init__(self, file_name) -> None:
        self.file_name = file_name


    def __enter__(self):
        print('Create/init Object/Handle')
        self.file = open(self.file_name, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Release the Object/Handle')
        self.file.close()


# using the above Custom Context manager

with FileManager('23_Oct_1.txt') as file_handle:
    file_content = file_handle.read()
    print(file_content)


print('ouside of context scope, file handle released already')



# Example - 2
# Custom File Manager - Context manager - by using an inbuilt decorator

from contextlib import contextmanager


@contextmanager
def File_Manager(file_name):
    try:
        file = open(file_name, 'r')

        yield file

    except Exception as ex:
        print(ex)

    finally:
        if file:
            file.close()    



with File_Manager('23_Oct.txt') as f:
    file_content = f.read()
    print(file_content)


print('ouside of context scope, file handle released already')
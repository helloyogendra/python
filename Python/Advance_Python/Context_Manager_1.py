# Context Manager
# Releasing Resource automatically

# Database Connection 
# mySQL Connector Package

# Python <-mySQL Connector-> MySQL


# Example of file handling without a context manager

def write_file_1(txt: str):
    try:
        file = open('23_Oct.txt', 'w')

        file.write(txt)

    except Exception as ex:
        print(ex)
        print('It will only execute when exceptions')
    else:
        print('It will only execute if no exceptions')
    finally:
        print('It will always execute, exception or no-exception')

        if file:
            file.close()        # must close the file handle


msg = "just some text data"

write_file_1(msg)




# Example of file handling with a context manager
# 'with' will create a context manager
# once the scope of 'with' block is over, resource will be released by context manager

def write_file_2(txt: str):
    try:
        with open('23_Oct_1.txt', 'w') as file:
            file.write(txt)

        print("this line is outside of with block")

    except Exception as ex:
        print(ex)
        print('It will only execute when exceptions')
    else:
        print('No exceptions, all good, check your file')
    


msg = "just some text data for our training"

write_file_2(msg)

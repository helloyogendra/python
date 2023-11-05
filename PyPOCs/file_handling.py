import os

def file_writer(file_name, data):
    try:
        file_handle = open(file_name, "w")     # here "w" means file-writing operation
        file_handle.write(data)
    except Exception as ex:
        print(ex)
    else:
        print("file writing done")
    finally:
        file_handle.close()

        
def file_apppend(file_name, data):
    try:
        file_handle = open(file_name, "a")  # here "a" means append more data to a file, file-apppend operation
        file_handle.write(data)
    except Exception as ex:
        print(ex)
    else:
        print("file writing done")
    finally:
        file_handle.close()


def file_reader(file_name):
    try:
        file_handle = open(file_name, "r")       # here "r" means append read data from a file, file-reading operation
        if file_handle.mode == "r":
            file_content = file_handle.read()
            #print(file_content)
    except Exception as ex:
        print(ex)
    else:
        print("file reading done")
    finally:
        file_handle.close()
    return file_content


def file_delete(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"delete file -> {file_name}")
    else:
        print("file not found")
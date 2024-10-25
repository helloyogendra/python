from enum import Enum

Const_ABC = "abc"
Const_DEF = "def"

# Define an enumeration class
class Json_Keys(Enum):
    DXAT_ALERT = "dxATAlert"
    PAYLOAD = "payLoad"
    PAYLOAD_SCHEMA = "payLoadSchema"
    
    SYM = "sym"
    TIME = "time"
    ALERTKEY = "alertkey"
    SOURCE_TABLE = "sourceTable"
    SOURCE = "source"
    SCHEMA = "Schema"

# Access the constants
# print(Constants.SYM1.value)  # Access the value of the SYM1 constant
# print(Constants.TIME1.value)
# print(Constants.ALERTKEY1.value)

# # You can also iterate over the constants
# for constant in Constants:
#     print(f"{constant.name}: {constant.value}")


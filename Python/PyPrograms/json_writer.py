import json
from json_constants import Json_Keys as Key, Const_ABC, Const_DEF


# Load the JSON Template from a file
with open("temp.json", "r") as jsonTemplateFile:
    jsonTemplateObject = json.load(jsonTemplateFile)
    print(jsonTemplateObject)
    print("============================================")
    print(str(jsonTemplateObject))

# Getting values to populate the JSON later :
sym         = "ABC"
time        = "2023-10-11"
alertkey    = "123"
sourceTable = "Table1"
source      = "Source1"
schema      = "Schema1"

print(Const_ABC, Const_DEF)

# START : Block-A : Populate the JSON with values :
jsonTemplateObject[Key.DXAT_ALERT.value][0][Key.TIME.value]         = time
jsonTemplateObject[Key.DXAT_ALERT.value][0][Key.SYM.value]          = sym
jsonTemplateObject[Key.DXAT_ALERT.value][0][Key.ALERTKEY.value]     = alertkey

jsonTemplateObject[Key.PAYLOAD.value][0][Key.SOURCE_TABLE.value]    = sourceTable
jsonTemplateObject[Key.PAYLOAD.value][0][Key.SYM.value]             = sym
jsonTemplateObject[Key.PAYLOAD.value][0][Key.SOURCE.value]          = source

jsonTemplateObject[Key.PAYLOAD_SCHEMA.value][0][Key.ALERTKEY.value] = schema
# END : Block-A : 


with open("jsonTemplateObject1.json", "w") as jsonFile:
    json.dump(jsonTemplateObject, jsonFile, indent=4)
    print(jsonTemplateObject)


print("JSON Writing done!!")   
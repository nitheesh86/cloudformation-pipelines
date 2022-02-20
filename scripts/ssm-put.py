import json
data = {
"Parameters": [
        {
            "Name": "/dummy-param/hello",
            "Type": "String",
            "Value": "hello ",
        },
        {
            "Name": "/dummy-param/world",
            "Type": "String",
            "Value": "world!",
        }
}
listOfParams = data["Parameters"]
f = open("commands.sh", "a")
f.write("#!/bin/sh\n")
f.close()
for item in listOfParams:
    Name = item["Name"]
    Value = item["Value"]
    Type = item["Type"]
f = open("commands.sh", "a")
    command = f'aws ssm --region=us-east-1 put-parameter --name "{Name}" --value "{Value}" --type "{Type}"';
    f.write(command)
    f.write("\n")
    f.close()

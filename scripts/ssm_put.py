import boto3
import json

AWS_REGION = "ap-south-1"

ssm_client = boto3.client("ssm", region_name=AWS_REGION)

with open('credential.json', 'r') as f:
  params = json.load(f)
  print(params)

mydict = params
for key in mydict.keys():
    val = mydict[key]
    new_string_parameter = ssm_client.put_parameter(
        Name= key,
        Value= val,
        Type='String',
        Overwrite=True,
        Tier='Standard',
        DataType='text')
    print(
    f"String Parameter created with version {new_string_parameter['Version']} and Tier {new_string_parameter['Tier']}"
)

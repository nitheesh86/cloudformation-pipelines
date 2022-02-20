import boto3


AWS_REGION = "ap-south-1"

ssm_client = boto3.client("ssm", region_name=AWS_REGION)

#with open('ssm.txt') as f:
#    for line in f:
#        print(line)

mydict = {'a': 'hello', 'b': 'world'}
for key in mydict.keys():
    val = mydict[key]
    new_string_parameter = ssm_client.put_parameter(
        Name= key,
        Description='EC2 Instance type for Dev environment',
        Value= val,
        Type='String',
        Overwrite=True,
        Tier='Standard',
        DataType='text')
    print(
    f"String Parameter created with version {new_string_parameter['Version']} and Tier {new_string_parameter['Tier']}"
)

import boto3
import csv

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name="us-east-1", aws_access_key_id="AKIAZRDUO2GDIMHYBTZG", aws_secret_access_key="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" )

# Retrieve the instances and their tags
instances = ec2.describe_instances()

# Create a list of unique tag keys across all instances
tag_keys = set()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        if 'Tags' in instance:
            for tag in instance['Tags']:
                tag_keys.add(tag['Key'])

# Create a CSV file and write the header row
with open('instances_with_tags.csv', 'w', newline='') as csvfile:
    fieldnames = ['InstanceName', 'InstanceId', 'InstanceType', 'State', 'Zone', 'PrivateIpAddress', 'PrivateDnsName', 'PublicDnsName', 'PlatformDetails']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Write data rows
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            row = {
                
                'InstanceName' : instance['Tags'][0]['Value'],
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'Zone': instance['Placement']['AvailabilityZone'],
                'PrivateIpAddress': instance['PrivateIpAddress'],
                'PrivateDnsName': instance['PrivateDnsName'],
                'PublicDnsName': instance['PublicDnsName'],
            }

            try:
                row['PlatformDetails'] = instance['PlatformDetails']
            except ValueError:
                pass
            
                #for tag in instance['Tags']:
                #    row[tag['Key']] = tag['Value']
            
            writer.writerow(row)
import boto3
import os 

bucketName = 'dst-app-bucket'
remoteDirectoryName = 'dmb_uat/0/'
aws_access_key_id='AKIAZRDUO2GDIMHYBTZG'
aws_secret_access_key='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'

def downloadDirectoryFroms3(bucketName, remoteDirectoryName, entireBucket=False):
    s3_resource = boto3.resource(
        's3', 
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key
    )
    bucket = s3_resource.Bucket(bucketName) 
    print("Hello WOrld")
    if entireBucket:
        for obj in bucket.objects.all():
            # Extract path and filename from object key
            path, file_name = os.path.split(obj.key)
            
            # Ensure path exists locally
            os.makedirs(path, exist_ok=True)
            
            # Download the object
            if not obj.key.endswith("/"):
                bucket.download_file(obj.key, os.path.join(path, file_name))
    else:
        for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
            print(f"type : {type(obj.key.split('/')[-1])} \n Value : {obj.key.split('/')[-1]}")
            path, file_name = os.path.split(obj.key)
            if not obj.key.endswith("/"):
                bucket.download_file(obj.key, file_name) # save to same path

downloadDirectoryFroms3(bucketName,remoteDirectoryName, True)
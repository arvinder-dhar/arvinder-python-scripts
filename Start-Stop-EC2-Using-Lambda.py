'''
Author : Arvinder
Description : This Code has not been wholly and Solly Developed by Arvinder

This Code avoids the interactive way of entering the creds and uses the LAMBDA Execution Role
This code will be used in Lambda Function and will start/stop EC2 based on Movies.csv file present in ruchi0312 bucket
Movies.csv contents are:
Action  Scope
------  -----
Machine on

EC2 will be turned on if scope=on and vice-versa
There are several dependencies to invoke a S3 trigger to Lambda.
The details are explained in the Serverless Section of SAA-C02 Exam like Layers to Import Module..

'''

import boto3
import pandas

# Connect to S3 using boto3.client
client = boto3.client('s3',region_name = 'ap-south-1')

'''
If you want to pass the creds (not a recommended way) modify the code as

client = boto3.client('s3', 
                      aws_access_key_id=<Access-Key-ID>, 
                      aws_secret_access_key=<Secret-Access-Key>, 
                      region_name='ap-south-1'
                      )
'''

# Fetch the list of existing buckets
clientResponse = client.list_buckets()

# Get the S3 object
obj = client.get_object(
    Bucket = 'Bucket', #Bucket Name
    Key = 'Movies.csv'
)
    
# Read data from the S3 object
data = pandas.read_csv(obj['Body'])

region = 'ap-south-1'
instances = ['Instance-ID'] #EC2 Instance ID
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    if (data.iloc[0,1] == 'on'):
        ec2.start_instances(InstanceIds=instances)
        print('Started(ON) Instance: ' + str(instances))
    elif (data.iloc[0,1] == 'off'):
        ec2.stop_instances(InstanceIds=instances)
        print('Stopped(OFF) Instance: ' + str(instances))
import boto3
# import ConfigParser
import argparse

# Let's use Amazon S3
#s3 = boto3.resource('s3')

#access_key = 'hg'
access_key1 = 'Avvv'
#secret_key = 'yxk'
secret_key1 = 'xyz'
#create a new bucket!!
url = "https://s3.amazonaws.com/"


#create a new bucket!!

def test():
    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list

    print("Bucket List: %s" % buckets)
    #
    # client = boto3.client(
    #     's3',
    #     aws_access_key_id=access_key,
    #     aws_secret_access_key=secret_key
    # )
    # client.create_bucket(Bucket='rahul_chef_test')
    #
    # # Upload a new file in the in the bucket!!
    #
    # data = open('test1.txt', 'rb')
    # s3.Bucket('rahul_chef_test').put_object(Key='test1.txt', Body=data)

test()


#def test():
 #   print("hello")
    # Create an S3 client
    # s3 = boto3.client('s3', aws_access_key_id=access_key1, aws_secret_access_key=secret_key1, endpoint_url= url)
    # #s3 = boto3.client('s3')
    # s3.create_bucket(Bucket='PlTest1')
#test()
import boto3

s3 = boto3.client('s3')
source_path = '/Users/ryanzotti/Documents/repos/Self_Driving_RC_Car/data/1/h2o_train.csv'
bucket_name = 'self-driving-car'
target_path = 'data/1/hello-remote.txt'
s3.upload_file(source_path, bucket_name, target_path)

print("Finished.")
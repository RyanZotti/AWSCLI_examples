## Instructions

**Prerequisites:**

You need a `~/.aws/credentials` file that should look something like this:

	[default]
	aws_access_key_id = fake
	aws_secret_access_key = fake
	region = us-east-1

Where the above details are associated with an AWS `User`, which you can check in the AWS `IAM` (Identity and Access Management) console. Also, the `User` needs a `Policy` like `AmazonS3FullAccess` that can write to `S3` or do whatever else you're trying to do. 


import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('self-driving-car')

# list all contents, but page through the results, which
# apparently checks the files in batches, so as not to
# overwhelm your computer. I got the source from here:
# http://boto3.readthedocs.io/en/latest/guide/collections.html#controlling-page-size
for i, obj in enumerate(bucket.objects.page_size(100)):
    print(obj.key)
print(i) # note, the page size was 100, but i returned 330

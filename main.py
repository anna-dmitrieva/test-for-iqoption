from minio import Minio
from minio.error import ResponseError

client = Minio('192.168.1.154:9000',
                access_key='Q3AM3UQ867SPQQA43P2F',
                secret_key='tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                secure=False)

try:
    response = client.get_partial_object('mybucketname', 'test.jpg', 1000)
    file = open("image.jpg", "w")
    file.write(response.read())
    file.close()
except ResponseError as err:
    print(err)

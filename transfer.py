from config import *
from error import *
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def transfer(file_list):
    params_or_error = get_config()
    if type(params_or_error) == Error:
        return params_or_error

    secret_id = params_or_error[0]
    secret_key = params_or_error[1]
    client = CosS3Client(CosConfig(Region=REGION, SecretId=secret_id, SecretKey=secret_key, Token=None, Scheme=SCHEME))
    url_list = []

    for file in file_list:
        reponse = client.upload_file(
            Bucket=BUCKET,
            LocalFilePath=file,
            Key=file,
            PartSize=20,
            MAXThread=5,
            EnableMD5=False
        )
        if not client.object_exists(Bucket=BUCKET, Key=file):
            print("Something use cos transform error")
            print(str(reponse))
            return Error(TRANSFORM_ERROR)
        url_list.append(client.get_object_url(Bucket=BUCKET, Key=file))
    print(url_list)
    return url_list


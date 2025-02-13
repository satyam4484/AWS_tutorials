import subprocess

def run_command(command):
    try:
        result = subprocess.run(command,shell=True,check=True,capture_output=True,text=True)
        return result.stdout
    except Exception as e:
        print(f"Error executin command:{e}")


def create_bucket(bucket_name: str):
    print("making s3 bucket with python code and the bucket name is ---",bucket_name)
    command=f"aws s3 mb s3://{bucket_name}"
    print(run_command(command))


def upload_file(bucket_name: str):
    print("uploading file to s3 with dummyy content")

    with open("dummy.txt","w") as file:
        file.write("This is dummy text file")
    command = f"aws s3 cp dummy.txt s3://{bucket_name}"
    print(run_command(command))

def list_s3_bucket():
    print("displaying all the buckets from s3 ")

    command = "aws s3 ls"
    print(run_command(command))

list_s3_bucket()
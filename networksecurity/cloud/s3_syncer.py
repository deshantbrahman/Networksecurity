
import os


import subprocess

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = ["aws", "s3", "sync", folder, aws_bucket_url]

        result = subprocess.run(command, capture_output=True, text=True)

        print("STDOUT:")
        print(result.stdout)

        print("STDERR:")
        print(result.stderr)

        print("Return Code:", result.returncode)
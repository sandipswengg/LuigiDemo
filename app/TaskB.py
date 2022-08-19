import luigi
import boto3

class ReadS3Data(luigi.Task):
    S3_BUCKET_NAME = "glue-demonstration"
    LOCAL_DIR = "../OUTDIR"


    def output(self):
        out_file_path = "%s/S3_Response.txt" %(self.LOCAL_DIR)

        return luigi.LocalTarget(out_file_path)

    def run(self):
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(self.S3_BUCKET_NAME)

        with self.output().open("w") as outfile:
            for obj in bucket.objects.all():
                key = obj.key
                outfile.write("%s\n" %(key))

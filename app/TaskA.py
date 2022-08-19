import luigi
from TaskB import ReadS3Data

class WriteLocalFileTask(luigi.ExternalTask):
    LOCAL_DIR = "../OUTDIR"

    """
        This will write the output
        The data will be generated from the run()
    """
    def output(self):
        out_file_path = "%s/final.txt" % (self.LOCAL_DIR)
        return luigi.LocalTarget(out_file_path)

    def requires(self):
        return ReadS3Data()

    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("hello Luigi")

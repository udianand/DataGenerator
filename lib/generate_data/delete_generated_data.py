from utility import utils

user_name = spark.sql("SELECT current_user()").collect()[0][0]

raw_files = "/dbfs/FileStore/{}/wm_demo/raw/data".format(user_name)
spark_raw_files = raw_files.replace("/dbfs", "")


def clear_dataset(dataset: str) -> None:
    dbutils.fs.rm("{}/{}".format(spark_raw_files, dataset), True)


def clear_all_datasets() -> None:
    for key, value in utils.base_and_derived_datasets().items():
        clear_dataset(key)
        print("{} deleted successfully".format(key))

        clear_dataset(value)
        print("{} deleted successfully".format(value))


clear_all_datasets()

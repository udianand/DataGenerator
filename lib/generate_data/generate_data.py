import json
import uuid
import time
import numpy as np

from crm import account, contact
from utility import utils


utils.pip_install(utils.module_faker)

user_name = spark.sql("SELECT current_user()").collect()[0][0]

raw_files = "/dbfs/FileStore/{}/wm_demo/raw/data".format(user_name)
spark_raw_files = raw_files.replace("/dbfs", "")
dbutils.fs.mkdirs(raw_files)

datasets = set()


def generate_base_data(
    dataset_class_name: str, dataset_name: str, n_records: int
) -> None:
    dbutils.fs.mkdirs("{}/{}".format(spark_raw_files, dataset_name))
    dataset_obj = utils.get_class_instance(dataset_class_name)

    for _ in range(n_records):
        with open(
            "{}/{}/{}_{}.json".format(
                raw_files, dataset_name, dataset_name, str(uuid.uuid4())
            ),
            "w",
        ) as f:
            json.dump(dataset_obj.create(), f)

    print(
        "{}/{} created successfuly with {} records".format(
            spark_raw_files, dataset_name, n_records
        )
    )


def generate_derived_data(
    dataset_class_name: str, dataset_name: str, list_base_ids=[]
) -> None:
    dbutils.fs.mkdirs("{}/{}".format(spark_raw_files, dataset_name))
    dataset_obj = utils.get_class_instance(dataset_class_name)

    for base_id in list_base_ids:
        derived_data = dataset_obj.create(base_id)
        with open(
            "{}/{}/{}_{}.json".format(
                raw_files, dataset_name, dataset_name, str(uuid.uuid4())
            ),
            "w",
        ) as f:
            json.dump(derived_data, f)

    print(
        "{}/{} created successfuly with {} records".format(
            spark_raw_files, dataset_name, len(list_base_ids)
        )
    )


def get_distinct_database_ids(dataset_name: str) -> list:
    dir = "{}/{}".format(spark_raw_files, dataset_name)
    list_distinct_ids = [
        a.id
        for a in spark.read.json(
            "{}/{}/{}_*.json".format(spark_raw_files, dataset_name, dataset_name)
        )
        .select("id")
        .distinct()
        .collect()
    ]

    return list_distinct_ids


def generate_data(num_base_records=10):
    for key, value in utils.base_and_derived_datasets().items():
        generate_base_data(key, key, num_base_records)
        generate_derived_data(value, value, get_distinct_database_ids(key))


num_records = 10_000_000_000
# num_records = 1
start_time = time.time()
generate_data(num_records)
end_time = time.time()
elapsed_time = end_time - start_time
print("Execution time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

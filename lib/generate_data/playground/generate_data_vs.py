import json
import uuid
import pandas as pd

from utility import utils


utils.pip_install("Faker")

user_name = spark.sql("SELECT current_user()").collect()[0][0]

raw_files = "/dbfs/FileStore/{}/wm_demo/raw/data".format(user_name)
spark_raw_files = raw_files.replace("/dbfs", "")
dbutils.fs.mkdirs(raw_files)

datasets = set()


def generate_base_data(dataset_obj: str, dataset_name: str, n_range: int) -> None:
    dbutils.fs.mkdirs("{}/{}".format(spark_raw_files, dataset_name))

    for _ in n_range:
        with open(
            "{}/{}/{}_{}.json".format(
                raw_files, dataset_name, dataset_name, str(uuid.uuid4())
            ),
            "w",
        ) as f:
            json.dump(dataset_obj.create(), f)

    print("{}/{} created successfuly".format(spark_raw_files, dataset_name))


def generate_derived_data(
    dataset_obj: str, dataset_name: str, list_base_ids=[]
) -> None:
    dbutils.fs.mkdirs("{}/{}".format(spark_raw_files, dataset_name))

    for base_id in list_base_ids:
        derived_data = dataset_obj.create(base_id)
        with open(
            "{}/{}/{}_{}.json".format(
                raw_files, dataset_name, dataset_name, str(uuid.uuid4())
            ),
            "w",
        ) as f:
            json.dump(derived_data, f)

    print("{}/{} created successfuly".format(spark_raw_files, dataset_name))


def get_distinct_database_ids(dataset_name: str) -> list:
    dir = "{}/{}".format(spark_raw_files, dataset_name)
    # list_distinct_ids = []
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


def clear_dataset(dataset: str) -> None:
    dbutils.fs.rm("{}/{}".format(spark_raw_files, dataset), True)


def clear_all_datasets() -> None:
    for dataset in datasets:
        clear_dataset(dataset)
        print("{} deleted successfully".format(dataset))


# account = account.account()
# num_accounts = 2
# generate_base_data(account, "account", range(0, num_accounts))
datasets.add("account")

"""list_distinct_account_ids = [
    a.account_id
    for a in spark.read.json("{}/account/account_*.json".format(spark_raw_files))
    .select("account_id")
    .distinct()
    .collect()
]
print(list_distinct_account_ids)"""


# contact = contact.contact()
# generate_derived_data(contact, "contact", list_distinct_account_ids)
# datasets.add("contact")
"""list_distinct_contact_ids = [
    c.contact_id
    for c in spark.read.json("{}/contact/contact_*.json".format(spark_raw_files))
    .select("contact_id")
    .distinct()
    .collect()
]
print(list_distinct_contact_ids)"""

print(get_distinct_database_ids("account"))


### Clearing all data
# clear_all_datasets()

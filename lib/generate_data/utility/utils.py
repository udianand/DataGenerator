import subprocess
import importlib

module_crm = "crm"
module_faker = "Faker"


def file_exists(dir) -> bool:
    try:
        dbutils.fs.ls(dir)
    except:
        return False
    return True


def pip_install(name):
    subprocess.call(["pip", "install", name])


def base_and_derived_datasets() -> dict:
    datasets = dict()
    datasets["account"] = "contact"
    return datasets


def get_class_instance(str_class_name: str):
    class_path = ".".join([module_crm, str_class_name])
    cls = getattr(importlib.import_module(class_path), str_class_name)
    return cls()

import secrets
import random
from datetime import datetime


class account:
    def __init__(self, num_samples=10):
        self.num_samples = num_samples
        self.len_account_id = 11
        self.account_status = ["Open", "Close"]
        self.account_types = ["Checking", "Investment"]
        self.source_system = ["Online", "In-Person", "Mobile"]

    def generate_account_ids(self) -> str:
        return "a" + secrets.token_hex(self.len_account_id)

    def create(self):
        account_data = {
            "id": self.generate_account_ids(),
            "status": random.choice(self.account_status),
            "type": random.choice(self.account_types),
            "source_system": random.choice(self.source_system),
            "account_created_at": datetime.now().isoformat(),
            "account_modified_at": datetime.now().isoformat(),
        }

        return account_data

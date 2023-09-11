import secrets
import random

from faker import Faker
from datetime import datetime

from call_log import financial_advisor
from call_log import robo_advisor
from call_log import online_trading_platform


class contact:
    def __init__(self):
        self.fake = Faker()
        self.len_contact_id = 11
        self.call_log_types = [
            "financial_advisor",
            "robo_advisor",
            "online_trading_platform",
        ]
        self.call_log_type = random.choice(self.call_log_types)

    def generate_contact_ids(self) -> str:
        return "c" + secrets.token_hex(self.len_contact_id)

    def generate_annual_revenue(self) -> int:
        match self.call_log_type:
            case "financial_advisor":
                return random.randint(5000000, 10000000)
            case "robo_advisor":
                return random.randint(100000, 500000)
            case "online_trading_platform":
                return random.randint(500000, 1000000)

    def generate_call_log(self) -> str:
        match self.call_log_type:
            case "financial_advisor":
                return financial_advisor.generate_fa_call_log()
            case "robo_advisor":
                return robo_advisor.generate_robo_advisor_call_log()
            case "online_trading_platform":
                return online_trading_platform.generate_otp_call_log()

    def create(self, account_id="XXXXXXXXXXX"):
        contact_data = {
            "id": self.generate_contact_ids(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "ssn": self.fake.ssn(),
            "account_id": account_id,
            "annual_revenue": self.generate_annual_revenue(),
            "address": self.fake.address(),
            "call_log": self.generate_call_log(),
            "contact_created_at": datetime.now().isoformat(),
            "contact_modified_at": datetime.now().isoformat(),
        }

        return contact_data

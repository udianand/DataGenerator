# DataGenerator
Generates Dummy CRM Data on Databricks

Generates Account and Contact data in json format

To generate data please run file 'generate_data.py'
To delete the generated data please run file 'delete_generated_data.py'

Account data model :-
account_data = {
            "id": account_id,
            "status": active/inactive account,
            "type": checking/investment
            "source_system": inperson/mobile/web
            "account_created_at": Date-Time when account was created,
            "account_modified_at": Date-Time when account was modified,
        }

Contact data model :-
contact_data = {
            "id": contact_id,
            "first_name": First Name,
            "last_name": Last Name,
            "ssn": SSN,
            "account_id": Corresponding Account ID
            "annual_revenue": Annual Revenue,
            "address": Fake Address,
            "call_log": Call Log Transcript in json,
            "contact_created_at":  Date-Time when account was created
            "contact_modified_at":  Date-Time when account was modified,
        }



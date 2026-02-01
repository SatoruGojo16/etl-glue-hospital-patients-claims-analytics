from dateutil.relativedelta import *
import json
import boto3 as b
from faker import Faker

fake = Faker()
stream_name = "kinesis-event-stream"
kinesis_client = b.client("kinesis")
london_boroughs = [
    "Barking and Dagenham",
    "Barnet",
    "Bexley",
    "Brent",
    "Bromley",
    "Camden",
    "Croydon",
    "Ealing",
    "Enfield",
    "Greenwich",
    "Hackney",
    "Hammersmith and Fulham",
    "Haringey",
    "Harrow",
    "Havering",
    "Hillingdon",
    "Hounslow",
    "Islington",
    "Kensington and Chelsea",
    "Kingston upon Thames",
    "Lambeth",
    "Lewisham",
    "Merton",
    "Newham",
    "Redbridge",
    "Richmond upon Thames",
    "Southwark",
    "Sutton",
    "Tower Hamlets",
    "Waltham Forest",
    "Wandsworth",
    "Westminster",
    "City of London",
]
input_jsons = []
for batch_round in range(1, fake.random_int(min=9, max=10)):
    print(f"Batch Count {batch_round}\n")
    upload_count = 0
    for _ in range(0, fake.random_int(min=1, max=10)):
        input_json = {}
        # Patienets Data
        input_json["partition_key"] = fake.uuid4()
        input_json["patient_id"] = fake.random_int(min=1000, max=9999)
        input_json["name_prefix"] = fake.prefix()
        input_json["first_name"] = fake.first_name()
        input_json["last_name"] = fake.last_name()
        input_json["date_of_birth"] = (
            fake.date_of_birth(minimum_age=18, maximum_age=65)
        ).strftime("%d-%m-%Y")
        input_json["phone_number"] = "+44" + fake.bothify(text="##########")
        input_json["email_id"] = fake.email()
        # Policy Data
        input_json["policy_id"] = fake.random_int(min=1000, max=9999)
        input_json["policy_start_date"] = fake.date_between("-20y", "+5y").strftime(
            "%d/%m/%Y"
        )
        input_json["policy_end_date"] = "2031/01/01"
        input_json["preimum_amount"] = "$" + fake.numerify("$00")
        input_json["coverage_limit"] = "$" + fake.numerify("$$000")
        # Address Data
        input_json["address_id"] = fake.random_int(min=1000, max=9999)
        input_json["addressline"] = f"{fake.building_number()} {fake.street_name()}"
        input_json["city"] = "London"
        input_json["state"] = "England"
        input_json["borough"] = fake.random_choices(london_boroughs, length=1)[0]
        # Claim Data
        input_json["claim_id"] = fake.random_int(min=1000, max=9999)
        input_json["claim_initialized_date"] = fake.date_between(
            "-20y", "+5y"
        ).strftime("%d/%m/%Y")
        input_json["claim_request_amount"] = "$" + str(
            fake.random_int(min=1000, max=99999)
        )
        input_json["claim_status"] = fake.random_choices(
            [
                "Accepted",
                "Rejected",
                "Under Process",
                "Initalized",
                "Settled",
                "Received",
            ],
            length=1,
        )[0]
        if ("Rejected") in input_json["claim_status"]:
            input_json["claim_rejected_reason"] = fake.random_choices(
                ["Policy Expired", "Policy Not Created", ""], length=1
            )[0]
        else:
            input_json["claim_rejected_reason"] = fake.random_choices([""], length=1)[0]

        json_dataset = json.dumps(input_json)
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json_dataset,
            PartitionKey=input_json["partition_key"],
        )
        upload_count = upload_count + 1
        # with open(f'../data/landing_zone/{input_json["partition_key"]}.json','w+') as f:
        # f.write(json.dumps(input_json, indent=4))
        print(
            f"Uploaded Patient ID `{input_json['patient_id']}` to Shard ID `{response['ShardId']}` with Sequence Number `{response['SequenceNumber']}`"
        )
    print(f"\nUploaded {upload_count} customer details to the stream")

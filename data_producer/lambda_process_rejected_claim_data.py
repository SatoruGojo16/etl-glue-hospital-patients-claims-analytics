import json
import base64


def process_claim_json_data(claim_data):
    # Processing the claim rejected reason from code before writing to s3
    claim_data.pop("partition_key")
    claim_reject_code = str(claim_data["RECORD_REJECTED_CODE"])
    claim_reject_reason = None
    if claim_reject_code == "101":
        claim_reject_reason = "Patient ID is Invalid"
    elif claim_reject_code == "102":
        claim_reject_reason = "Policy ID is Invalid"
    elif claim_reject_code == "103":
        claim_reject_reason = "Claim ID is Invalid"
    elif claim_reject_code == "104":
        claim_reject_reason = "Address ID is Invalid"
    elif claim_reject_code == "105":
        claim_reject_reason = "Claim Request Amount should not be Zero(0)"
    else:
        claim_reject_reason = "Undefined Reject Reason"
    claim_data["RECORD_REJECTED_REASON"] = claim_reject_reason
    return claim_data["RECORD_REJECTED_REASON"], claim_data


def lambda_handler(event, context):
    records = []
    for record in event["records"]:
        # Data Extract - Base64 data decoded from Firehose bytes decoded to UTF-8 for JSON data manipulation
        payload = json.loads(base64.b64decode(record["data"]).decode("utf-8"))
        # Data Trasnform
        claim_rejected_reason, data = process_claim_json_data(payload)

        # Data Loading - Encoding JSON to UTF-8 bytes to serliazed format of Base64 bytes for Firehose bytes decoded to UTF-8 for support in JSON
        # json.dumps is used since the Producer converts data from JSON to str before transmitting data
        output_record = {
            "recordId": record["recordId"],
            "claim_partition_id": data["partition_key"],
            "claim_rejected_reason": claim_rejected_reason,
            "rejected_claim": base64.b64encode(json.dumps(data).encode("utf-8")).decode(
                "utf-8"
            ),
        }
        records.append(output_record)
    print("Successfully processed {} records.".format(len(event["records"])))
    return {"records": records}

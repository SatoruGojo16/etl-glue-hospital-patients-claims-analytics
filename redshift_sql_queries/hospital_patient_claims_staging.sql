DROP TABLE IF EXISTS staging_patient;
CREATE TABLE staging_patient (
  patient_id varchar,
  name_prefix varchar,
  first_name varchar,
  last_name varchar,
  patient_full_name varchar,
  date_of_birth varchar,
  phone_number varchar,
  email_id varchar
);

DROP TABLE IF EXISTS staging_policy;
CREATE TABLE staging_policy (
  policy_id varchar,
  policy_start_date varchar,
  policy_end_date varchar,
  premium_amount varchar,
  coverage_limit varchar
);

DROP TABLE IF EXISTS staging_address;
CREATE TABLE staging_address (
  address_id varchar,
  addressline varchar,
  borough varchar,
  borough_level varchar,
  borough_latitude varchar,
  borough_longitude varchar,
  borough_abbrev varchar,
  borough_code varchar,
  city varchar,
  state varchar
);

DROP TABLE IF EXISTS staging_claims;
CREATE TABLE staging_claims (
  claim_id varchar,
  high_risk_claim_flag  varchar,
  claim_initialized_date varchar,
  claim_request_amount varchar,
  claim_status varchar,
  claim_rejected_reason varchar
);

DROP TABLE IF EXISTS staging_patient;
CREATE TABLE staging_patient (
  patient_id varchar,
  name varchar,
  date_of_birth varchar,
  phone_number varchar,
  email_id varchar
);

DROP TABLE IF EXISTS staging_policy;
CREATE TABLE staging_policy (
  policy_id varchar,
  policy_start_date varchar,
  policy_expire_date varchar,
  premium_amount varchar,
  coverage_limit varchar
);

DROP TABLE IF EXISTS staging_address;
CREATE TABLE staging_address (
  address_id varchar,
  borough varchar,
  region varchar,
  latitude varchar,
  longitude varchar
);

DROP TABLE IF EXISTS staging_claims;
CREATE TABLE staging_claims (
  claim_id varchar,
  claim_initialized_date varchar,
  claim_request_amount varchar,
  claim_status varchar
);

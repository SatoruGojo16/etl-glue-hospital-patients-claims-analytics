// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table dim_patient {
  patient_ref_key integer [primary key]
  patient_id varchar
  name_prefix varchar
  first_name varchar
  last_name varchar
  patient_full_name varchar
  date_of_birth varchar
  phone_number varchar
  email_id varchar
  effective_start_date varchar
  effective_end_date varchar
  is_current varchar
}

Table dim_date {
  date_id integer [primary key]
  full_date varchar
  year varchar
  month varchar
  day varchar
  week varchar
  quarter varchar
}

Table dim_policy{
  policy_ref_key integer [primary key]
  policy_id varchar
  policy_start_date varchar
  policy_end_date varchar
  premium_amount varchar
  coverage_limit varchar
  effective_start_date varchar
  effective_end_date varchar
  is_current varchar
}

Table dim_address {
  address_ref_key integer [primary key]
  address_id varchar
  addressline varchar
  borough varchar
  borough_level varchar
  borough_latitude varchar
  borough_longitude varchar
  borough_abbrev varchar
  borough_code varchar
  city varchar
  state varchar
  effective_start_date varchar
  effective_end_date varchar
  is_current varchar
}

Table dim_claims {
  claim_ref_key integer [primary key]
  claim_id varchar
  high_risk_claim_flag  varchar
  claim_initialized_date varchar
  claim_request_amount varchar
  claim_status varchar
  claim_rejected_reason varchar
}

Table fact_claims_hist
{
   fact_claim_id int [primary key]
   patient_id int 
   address_id int 
   policy_ref_id int
   claim_id int 
   last_updated_date int
}


Ref: "fact_claims_hist"."last_updated_date" < "dim_date"."date_id"

Ref: "fact_claims_hist"."policy_ref_id" < "dim_policy"."policy_ref_key"

Ref: "fact_claims_hist"."claim_id" < "dim_claims"."claim_id"

Ref: "fact_claims_hist"."address_id" < "dim_address"."address_ref_key"

Ref: "fact_claims_hist"."patient_id" < "dim_patient"."patient_ref_key"

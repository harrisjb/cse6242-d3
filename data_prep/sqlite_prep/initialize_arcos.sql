-- ***************************************
-- This is a simple import script to work with the opioid data set using SQLite
-- data is read raw and we add a column 'trans_year' to facilitate faster processing by year

-- DDL for Opioid Dataset
.headers on


DROP TABLE IF EXISTS dea_arcos_wpost;

CREATE TABLE dea_arcos_wpost (
    REPORTER_DEA_NO TEXT,
    REPORTER_BUS_ACT TEXT,
    REPORTER_NAME TEXT,
    REPORTER_ADDL_CO_INFO TEXT,
    REPORTER_ADDRESS1 TEXT,
    REPORTER_ADDRESS2 TEXT,
    REPORTER_CITY TEXT,
    REPORTER_STATE TEXT,
    REPORTER_ZIP TEXT,
    REPORTER_COUNTY TEXT,
    BUYER_DEA_NO TEXT,
    BUYER_BUS_ACT TEXT,
    BUYER_NAME TEXT,
    BUYER_ADDL_CO_INFO TEXT,
    BUYER_ADDRESS1 TEXT,
    BUYER_ADDRESS2 TEXT,
    BUYER_CITY TEXT,
    BUYER_STATE TEXT,
    BUYER_ZIP TEXT,
    BUYER_COUNTY TEXT,
    TRANSACTION_CODE TEXT,
    DRUG_CODE TEXT,
    NDC_NO TEXT,
    DRUG_NAME TEXT,
    QUANTITY INTEGER,
    UNIT TEXT,
    ACTION_INDICATOR TEXT,
    ORDER_FORM_NO TEXT,
    CORRECTION_NO TEXT,
    STRENGTH TEXT,
    TRANSACTION_DATE TEXT,
    CALC_BASE_WT_IN_GM DOUBLE,
    DOSAGE_UNIT INTEGER,
    TRANSACTION_ID TEXT,
    Product_Name TEXT,
    Ingredient_Name TEXT,
    Measure TEXT,
    MME_Conversion_Factor TEXT,
    Combined_Labeler_Name TEXT,
    Revised_Company_Name TEXT,
    Reporter_family TEXT,
    dos_str DOUBLE
 );

.separator "\t"
.import ./arcos_all_washpost.tsv dea_arcos_wpost
.schema dea_arcos_wpost

-- Check Substring Statement
-- SELECT  REPORTER_DEA_NO, substr(TRANSACTION_DATE, -4) FROM pills LIMIT 10;

-- Add the Year as a separate column to improve query performance
ALTER TABLE dea_arcos_wpost
   ADD trans_year INTEGER;

UPDATE dea_arcos_wpost
   SET trans_year = substr(TRANSACTION_DATE, -4);

CREATE INDEX pills_buyer_zip ON dea_arcos_wpost (BUYER_ZIP);



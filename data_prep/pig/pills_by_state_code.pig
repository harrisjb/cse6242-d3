pills = LOAD  '/mnt/data1/Data/opioid_data/arcos_all_washpost.tsv' AS(
    REPORTER_DEA_NO:chararray,
    REPORTER_BUS_ACT:chararray,
    REPORTER_NAME:chararray,
    REPORTER_ADDL_CO_INFO:chararray,
    REPORTER_ADDRESS1:chararray,
    REPORTER_ADDRESS2:chararray,
    REPORTER_CITY:chararray,
    REPORTER_STATE:chararray,
    REPORTER_ZIP:chararray,
    REPORTER_COUNTY:chararray,
    BUYER_DEA_NO:chararray,
    BUYER_BUS_ACT:chararray,
    BUYER_NAME:chararray,
    BUYER_ADDL_CO_INFO:chararray,
    BUYER_ADDRESS1:chararray,
    BUYER_ADDRESS2:chararray,
    BUYER_CITY:chararray,
    BUYER_STATE:chararray,
    BUYER_ZIP:chararray,
    BUYER_COUNTY:chararray,
    TRANSACTION_CODE:chararray,
    DRUG_CODE:chararray,
    NDC_NO:chararray,
    DRUG_NAME:chararray,
    QUANTITY:int,
    UNIT:chararray,
    ACTION_INDICATOR:chararray,
    ORDER_FORM_NO:chararray,
    CORRECTION_NO:chararray,
    STRENGTH:chararray,
    TRANSACTION_DATE:chararray,
    CALC_BASE_WT_IN_GM:float,
    DOSAGE_UNIT:int,
    TRANSACTION_ID:chararray,
    Product_Name:chararray,
    Ingredient_Name:chararray,
    Measure:chararray,
    MME_Conversion_Factor:chararray,
    Combined_Labeler_Name:chararray,
    Revised_Company_Name:chararray,
    Reporter_family:chararray,
    dos_str:float
 );

-- SELECT Keep only the columns that are needed --
pills_sold = FOREACH pills GENERATE BUYER_STATE, SUBSTRING(TRANSACTION_DATE, (int)SIZE(TRANSACTION_DATE)-4, (int)SIZE(TRANSACTION_DATE)) as TRANS_YEAR, QUANTITY;

-- LIMIT reesults to 15
--top15 = LIMIT pills_sold 15;


-- WHERE
pills_where_year_2006 = FILTER pills_sold  BY TRANS_YEAR == '2006';

-- GROUP BY
group_buyer_state = GROUP pills_where_year_2006 BY BUYER_STATE;
total_pills_by_state = FOREACH group_buyer_state GENERATE FLATTEN(group) as BUYER_STATE, SUM(pills_where_year_2006.QUANTITY) as TOTAL_PILLS;

-- ORDER BY
results = ORDER total_pills_by_state BY TOTAL_PILLS DESC, BUYER_STATE ASC;

STORE results INTO './output' USING PigStorage('\t');

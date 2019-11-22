## Washington Post opioid data

You can find some background data [here](
https://www.washingtonpost.com/national/2019/07/20/opioid-files/?noredirect=on) on opioid data set.


You can download the complete data set from [here](
https://d2ty8gaf6rmowa.cloudfront.net/dea-pain-pill-database/bulk/arcos_all_washpost.tsv.gz)

Note that the data set is **7GB** compressed and **75GB** uncompressed.

There are 178,598,027 Rows of Data

And 42 features (listed below)

```
REPORTER_DEA_NO       (No Null fields)
REPORTER_BUS_ACT      (99% of Fields have value DISTRIBUTOR)
REPORTER_NAME         (494 Unique Names no Nulls)
REPORTER_ADDL_CO_INFO (96% Null)
REPORTER_ADDRESS1     (No Nulls)
REPORTER_ADDRESS2
REPORTER_CITY         (418 Cities no nulls)
REPORTER_STATE        (50 States)
REPORTER_ZIP          (504 Zip Codes)
REPORTER_COUNTY       (248 Counties)
BUYER_DEA_NO          (No Nulls)
BUYER_BUS_ACT         (CHAIN, RETAIL, PRACTIONER)
BUYER_NAME            (108,520 Unique Buyers)
BUYER_ADDL_CO_INFO    (96% Null)
BUYER_ADDRESS1        (135,109 Unique Addresses)
BUYER_ADDRESS2
BUYER_CITY            (10,534 Unique Cities 1 Null)
BUYER_STATE           (57 States)
BUYER_ZIP             (17,456 Zip codes)
BUYER_COUNTY          (1,863 Counties)
TRANSACTION_CODE      ('S' for the Entire Dataset)
DRUG_CODE             ('9193' or '9143' for the Entire dataset)                
DRUG_NAME             ('HYDRCODONE',OXYCODONE aligns with DRUG_CODE)
NDC_NO                (41,151 Unique Values)
QUANTITY              (Quantity in # of Tablets)
UNIT                  (TAB for Entire dataset)
ACTION_INDICATOR      (99% Null)
ORDER_FORM_NO         (61% Null)
CORRECTION_NO         (99% Null)
STRENGTH              (74% Null and 24% '0000')
TRANSACTION_DATE      (Date)
CALC_BASE_WT_IN_GM    (5,604 Unique Values no Nulls ??)
DOSAGE_UNIT           (3,115 Unique Values no Nulls ??)
TRANSACTION_ID        (No Nulls)
Product_Name          (No Nulls Product with Tablet Size in MG)
Ingredient_Name       (Aligns with DRUG_NAME,DRUG_CODE)
Measure               ('TAB' for the Entire Dataset )
MME_Conversion_Factor ('1.0' or '1.5' for the Entire Dataset)
Combined_Labeler_Name (90 Unique Values)
Revised_Company_Name  (86 Unique Values)
Reporter_family       (396 Unique Values)
dos_str               (Seems to Align with Dosage in MG. 18 Unique Values)
```


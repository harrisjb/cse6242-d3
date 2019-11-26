select Reporter_family, sum(DOSAGE_UNIT) as total_pills
   from pills
   where
        BUYER_BUS_ACT in (
            'RETAIL PHARMACY',
            'CHAIN PHARMACY',
            'PRACTITIONER',
            'PRACTITIONER-DW/30',
            'PRACTITIONER-DW/100',
            'PRACTITIONER-DW/275'
        ) and
        TRANSACTION_CODE == 'S' and
        Measure == 'TAB' and
        DRUG_NAME in ('OXYCODONE', 'HYDROCODONE') and
        REPORTER_BUS_ACT == 'DISTRIBUTOR'
    group by Reporter_family
    order by total_pills desc
    limit 100;



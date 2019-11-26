-- ***************************************
-- This is a simple import script to work with the county codes using SQLite
-- The data contains State and County Names matched to the arcos dataset

-- DDL for County Data
.headers on


DROP TABLE IF EXISTS county;

CREATE TABLE county (
    State TEXT,
    County TEXT,
    County_code TEXT
 );

.separator ","
.import ./arcos_buyer_county_codes.csv county
.schema county

create view pills_county as
   select a.*, c.County_code
   from dea_arcos_wpost a
   left join County c
   on c.State = a.buyer_state and
      c.county = a.buyer_county;


-- Test the results --
select buyer_state, buyer_county, count(buyer_state)
    from pills_county
    where county_code is null
    group by buyer_state, buyer_county;



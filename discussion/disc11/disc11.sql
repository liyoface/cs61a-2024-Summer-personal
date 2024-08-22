create table cities as
    select 'Berkeley' as name, 'CA' as state, 12000 as population, 1878 as founded, 18.0 as area union
    select 'San Francisco'   , 'CA'         , 871000             , 1850           , 231.0 union
    select 'Los Angeles'     , 'CA'         , 3971000            , 1850           , 503.0 union
    select 'Seattle'         , 'WA'         , 609000             , 1869           , 143.0 union
    select 'Houston'         , 'TX'         , 2099451            , 1837           , 667.0 union
    select 'New York City'   , 'NY'         , 8550000            , 1624           , 468.0 union
    select 'Chicago'         , 'IL'         , 2696000            , 1833           , 234.0 union
    select 'Philadelphia'    , 'PA'         , 1567000            , 1701           , 142.0 union
    select 'Phoenix'         , 'AZ'         , 1446000            , 1881           , 518.0 union
    select 'San Antonio'     , 'TX'         , 1437000            , 1837           , 465.0 union
    select 'Dallas'          , 'TX'         , 1300000            , 1856           , 386.0 union
    select 'Jacksonville'    , 'FL'         , 822000             , 1832           , 875.0;

create table states as
    select 'California' as name, 'CA' as abbreviation, 39250000.0 as population union
    select 'Washington'        , 'WA'                , 7288000.0 union
    select 'Texas'             , 'TX'                , 27863000.0 union
    select 'New York'          , 'NY'                , 19795000.0 union
    select 'Illinois'          , 'IL'                , 12801000.0 union
    select 'Pennsylvania'      , 'PA'                , 12802503.0 union
    select 'Arizona'           , 'AZ'                , 6828000.0 union
    select 'Florida'           , 'FL'                , 20612000.0;

CREATE table california as
	SELECT * FROM cities WHERE state='CA';

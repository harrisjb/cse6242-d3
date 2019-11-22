# Census Data 2010

The data has been pulled from www.census.gov

to pull data yuo must first request an API key from [here](https://api.census.gov/data/key_signup.html)

Additional data can be found:
* https://www.census.gov/developers/

* https://censusreporter.org/topics/about-census/

* https://github.com/datadesk/census-data-downloader

You can pip install **censusdatadownloader** using

`pip install census-data-downloader`

`export CENSUS_API_KEY='<your API key>'`


censusdatadownloader --year 2010 race counties

censusdatadownloader --year 2010 population counties

censusdatadownloader --year 2010 medianage counties

censusdatadownloader --year 2010 medianhouseholdincome counties

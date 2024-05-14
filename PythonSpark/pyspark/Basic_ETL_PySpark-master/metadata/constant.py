# Importing the SparkSession class from the pyspark.sql module
from pyspark.sql import SparkSession

# Defining a function named spark_inst that returns a SparkSession instance
def spark_inst():
    # Creating a SparkSession instance with the following configurations:
    # - master: "local[*]" means running Spark locally with as many worker threads as logical cores on your machine
    # - appName: 'Spark' is the name of the Spark application
    # - getOrCreate(): This method returns an existing SparkSession if there is one, or creates a new one if necessary
    return SparkSession.builder.master("local[*]")\
           .appName('Spark')\
           .getOrCreate()


# As all df have 'country_code' column we use that columns to join df
JOIN_ON_COLUMNS=['country_code']
JOIN_TYPE="left"


# columns that will be left join with country_code column
SPEC_COLS=[
    "country_code",
    "country_name",
    "region",
    "surface_area",
    "independence_year",
    "country_population",
    "life_expectancy",
    "local_name",
    "head_of_state",
    "capital",
    "country_code_2",
    "city_id",
    "city_name",
    "city_district",
    "city_population",
    "language",
    "is_official_language",
    "language_percentage"  
]



CITY_COL_DICT={
          "ID": "city_id",
          "Name": "city_name",
          "CountryCode": "country_code",
          "District": "city_district",
          "Population": "city_population"
     }


COUNTRY_COL_DICT={
          "Code": "country_code",
          "Name": "country_name",
          "Continent": "continent",
          "Region": "region",
          "SurfaceArea": "surface_area",
          "IndepYear": "independence_year",
          "Population": "country_population",
          "LifeExpectancy": "life_expectancy",
          "GNP": "gross_national_product",
          "GNPOld": "old_gross_national_product",
          "LocalName": "local_name",
          "GovernmentForm": "government_form",
          "HeadOfState": "head_of_state",
          "Capital": "capital",
          "Code2": "country_code_2"
     }    


COUNTRY_LANGUAGE_COL_DICT={
          "CountryCode": "country_code",
          "Language": "language",
          "IsOfficial": "is_official_language",
          "Percentage": "language_percentage"
     }

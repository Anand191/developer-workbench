create database if not exists testdb;
use testdb;
create external table if not exists weather (
  MinTemp float,
  MaxTemp float,
  Rainfall float,
  Evaporation float,
  Sunshine float,
  WindGustDir string,
  WindGustSpeed float,
  WindDir9am string,
  WindDir3pm string,
  WindSpeed9am float,
  WindSpeed3pm float,
  Humidity9am float,
  Humidity3pm float,
  Pressure9am float,
  Pressure3pm float,
  Cloud9am float,
  Cloud3pm float,
  Temp9am float,
  Temp3pm float,
  RainToday string,
  RISK_MM float,
  RainTomorrow string
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/testdb.db/weather';
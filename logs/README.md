# GML BI Community Edition (Open Source)

## About this folder

This folder is used to register all events during data ingestion tasks.
Those events are saved in the `.log` files.

## How does it work

Those files are created when:

- the data is pulled from the Datalake, and
- the data is pushed to the Data Warehouse (OLAP database)

Below, we can see an example of the log file generated during data ingestion task:

- the data is pushed to the Data Warehouse (OLAP database)

```text
2023-06-02 08:16:57,824 - GML - INFO - ======================= START =======================
2023-06-02 08:16:57,824 - GML - INFO - Getting data from the local folder: /Users/lserra/PyProjects/gml_bi_ce/data/input/
2023-06-02 08:17:32,897 - GML - INFO - Total of 6206153 rows have been loaded
2023-06-02 08:17:32,898 - GML - INFO - =======================  END  =======================
```

**NOTES**:

- this app version does **NOT** generate log files, because data ingestion tasks it is
  **NOT** part of this solution.

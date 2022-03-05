# PDF EXTRACT TABLES

## Overview

A simple script which extracts the table data from a PDF document. 

## Functionality

- Each table is saved to a separate JSON file in the `tables` directory. 
- Filenames are based on the current date and time.
- Data extraction is performed using the "tabula-py" library.
- Extracted table data is represented in JSON using the "Table Schema" specification. 
- For more information visit https://specs.frictionlessdata.io/table-schema/#concepts.
- https://pypi.org/project/tableschema/

## Background

Data from tables is referred to hereafter as "tabular data".
Understanding how PDF documents are rendered in relation to sections of tabular data is key
to the problem that this script solves.

A lot of time is wasted on a daily basis copying and manipulating PDF documents with a 
combination of browser extensions, online extractor tools which seem to cause more problems
than they provide solutions, or redesigning the tables in unsuited applications like Microsoft
Word. 

## Table Schema

This script tries to adhere to the "Table Schema". A summary of the specification for representing
tabular data in the JSON format (RFC 4627) follows:

- A Table Schema is represented by a "descriptor".

- The descriptor must be a JSON object.

- It must contain a property "fields".

- "fields" must be an array.

- Each entry in the "fields" array must be a "field descriptor".

- The order of the elements in the "fields" array must be the same order as the tabular data column order.

- The number of elements in the "fields" array must be the same as the number of columns in the tabular data.

- The "descriptor" may have additional properties and may contain any number of other properties which are 
not included:

  "missingValues",
  "primaryKey",
  "foreignKeys"

- Types may be 
boolean, 
object, 
array, 
integer, 
string, 
number, 
boolean, 
date, 
time, 
datetime, 
year, 
yearmonth, 
duration, 
geopoint, 
any

## Work Breakdown Structure

### Preparation

1. Find sample to work from. (included in archive).
2. pip install tableschema
3. Refactor sample in archive folder.
4. Read https://github.com/frictionlessdata/frictionless-py
5. pip install tabula-py


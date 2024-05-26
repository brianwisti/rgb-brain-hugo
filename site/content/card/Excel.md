---
created: 2024-05-06 15:41:39-07:00
title: Excel
updated: 2024-05-06 15:43:47-07:00
---

## Summary

Desktop spreadsheet editor from *Microsoft*

## Jots

Used at all layers of [Data Analysis](Data%20Analysis.md) for small data management (small in computer terms, that is)

## Core Excel Functions

* Starting from and expanded somewhat on what *Data Analyst Roadmap* describes
* `SUM`
  * add a collection of values, including literals, cell references, and / or ranges
  * [SUM function - Microsoft Support](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
* `MIN` / `MAX`
  * [MIN function - Microsoft Support](https://support.microsoft.com/en-us/office/min-function-61635d12-920f-4ce2-a70f-96f202dcc152)
  * [MAX function - Microsoft Support](https://support.microsoft.com/en-us/office/max-function-e0012414-9ac8-4b34-9a47-73e662c08098)
  * provides insight into dataset range, identifies possible outliers, and helps understand data variability
* `AVERAGE`
  * returns the *mean* of its arguments
  * [AVERAGE function - Microsoft Support](https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6)
* `COUNT`
  * return the number of cells in argument list with values
  * [COUNT function - Microsoft Support](https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c)
* `CONCAT`
  * combines text from multiple ranges and / or strings
  * [CONCAT function - Microsoft Support](https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2)
* `TRIM`
  * Clean up whitespace in text by stripping spaces off the edges and ensuring there is only a single space between words in the text.
  * [TRIM function - Microsoft Support](https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9)
* `UPPER` / `LOWER` / `PROPER`
  * [UPPER function - Microsoft Support](https://support.microsoft.com/en-us/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6)
  * [LOWER function - Microsoft Support](https://support.microsoft.com/en-us/office/lower-function-3f21df02-a80c-44b2-afaf-81358f9fdeb4)
  * [PROPER function - Microsoft Support](https://support.microsoft.com/en-us/office/proper-function-52a5a283-e8b2-49be-8506-b2887b889f94)
* `REPLACE` / `SUBSTITUTE`
  * [REPLACE, REPLACEB functions - Microsoft Support](https://support.microsoft.com/en-us/office/replace-replaceb-functions-8d799074-2425-4a8a-84bc-82472868878a)
  * [SUBSTITUTE function - Microsoft Support](https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332)
* `VLOOKUP` / `HLOOKUP` / `XLOOKUP`
  * `XLOOKUP` is recommended over both `HLOOKUP` and `VLOOKUP`
  * Use the **XLOOKUP** function to find things in a table or range by row.
  * [XLOOKUP function - Microsoft Support](https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929)
  * Searches for a value in the top row of a table or an array of values, and then returns a value in the same column from a row you specify in the table or array.
  * [HLOOKUP function - Microsoft Support](https://support.microsoft.com/en-us/office/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f)
  * Use VLOOKUP when you need to find things in a table or a range by row.
  * [VLOOKUP function - Microsoft Support](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1)
* `IF`
* `DAYS`
  * Returns the number of days between two dates.
  * [DAYS function - Microsoft Support](https://support.microsoft.com/en-us/office/days-function-57740535-d549-4395-8728-0f07bff0b9df)
* `DATEDIF`
  * Calculates the number of days, months, or years between two dates.  (`DATEDIF` is a legacy function for ancient Lotus spreadsheets, and sometimes gets it wrong.)
  * [DATEDIF function - Microsoft Support](https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c)

## Related

[Excel help & learning](https://support.microsoft.com/en-us/excel)
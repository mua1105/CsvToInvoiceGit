# Timesheet CSV to Invoice Converter
This is a Python-Script that converts the .csv - export from the Timesheet app to a .pdf Invoice (in German language).

## Prerequisites:
- Working Python environment
- Working "latexmk" (see https://mg.readthedocs.io/latexmk.html for installation help)
## Getting started:
- Run "makePreset.py" and enter your information.
- Replace "signature.eps" with your own signature (use e.g. GIMP to convert to .eps)
- Export your .csv file in the format: (Date, HoursWorked)
- The Hourly rate is defined in csvToInvoiceConverter.pdf in line 9
- Great! You are ready to go! Run **py CsvToInvoiceConverter.py "yourcsv.csv"**
## Debugging:
If the export proccess isn't finnishing, latexmk might throw some errors.
To fix this, run (latexmk -pdf "yourfile.tex") and look at the errors

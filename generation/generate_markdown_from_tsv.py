import csv 
import os


def format_bibtex(bibtex):
    bibtex = bibtex.replace(",  ", ",\n  ")
    return bibtex

def make_section(title, authors, date, link, bibtex):
    authors = authors.replace(";", ",")
    section = f"""
### [{title}]({link}) ({date})

{authors}
```
{format_bibtex(bibtex)}
```"""
    return section

def make_prolouge():
    return """
# Awesome Barometric Touch [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This is a collection of all tactile sensors which are based on MEMS barometers.  To add your paper, please submit an issue with the necessary details.
"""



fname = os.path.join("generation", "Tactile Sensor Lit Review - review.tsv")
labels = []
data = []
with open(fname, 'r') as f:
    reader = csv.reader(f, delimiter='\t')

    for row in reader:
        if row[0] == "SensorName":
            labels = {name: idx for idx, name in enumerate(row)}
            continue

        elif row[1] == "":
            continue

        else:
            data.append(row)
        

print("col: ", len(data))
print("row: ", len(data[0]))

output_string = ""

output_string += make_prolouge()

for row in data:
    if row[labels["Sensor Type Introduced"]] == "Barometric":
        section = make_section(row[labels["Paper Name"]], row[labels["Authors"]], row[labels["Publication Year"]], row[labels["Link"]], row[labels["Bibtex"]])
        output_string += section

output_fname = "README.md"
with open(output_fname, "w") as f:
    f.write(output_string)

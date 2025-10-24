# OpenSpace Organizer

## Description

A company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. This script can runs everyday to re-assign everybody to a new seat.

## Features

- The script can be configured using the **Parameters** section at the beginning of the script.
- Script (in general cases) needn't user input. The name of  **input** file can be passed as a parameter through the command line
- If there are more people than seats - script can leave some random people behind (but only with the manual confirmation)
- If someone left **alone** at the table - we seat another person with him
- Script can output and compose the list of people in tree different formats (see section format below)
- Output can be both in console and in a file

## Formats and parameters

The main function in **main.py** is Openspace.output. 

The first parameter is mode wich is `int`:

**Modes:**
       **1** - Compose list by people in alphabet. order  
       **2** - Compose list by tables  
       **3** - Output list in json format  

The second parameter is output filename wich is `string`
In case of  string is `None` or empty, the output will be in the console.

## Usage

1. Clone the repository to your local machine.
2. To run the script, you can execute the `main.py` file from your command 	line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "out.txt" file in your root directory. 

## Timeline

The script was completed as a study project in October 2025.

## Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 




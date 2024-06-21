# ISBN 13&10 Checksum Calculator

## Overview

The **ISBN 13&10 Checksum Tool** is a Python-based utility for calculating the check digits for both ISBN-10 and ISBN-13 numbers. This tool helps users verify the validity of ISBN numbers by generating the correct check digit based on the initial part of the ISBN.

## Features

- Calculate the check digit for 9-digit ISBN-10 numbers.
- Calculate the check digit for 12-digit ISBN-13 numbers.
- User-friendly command-line interface.
- Option to exit the program at any time.

## Requirements

- Python 3.x

## How to Use

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python.
    
4. Follow the on-screen instructions:
    - Choose whether you want to calculate the check digit for an ISBN-10 or ISBN-13 number.
    - Enter the initial part of the ISBN number when prompted.
    - The tool will display the calculated check digit.

## Example Usage

```
Check digit for: [1]ISBN 10 [2]ISBN 13 [3]Exit: 1
Enter the 9 digit ISBN number: 030640615
ISBN check digit: X

Check digit for: [1]ISBN 10 [2]ISBN 13 [3]Exit: 2
Enter the 12 digit ISBN number: 978030640615
ISBN check digit: 7

Check digit for: [1]ISBN 10 [2]ISBN 13 [3]Exit: 3
Thank you!
```

## Code Explanation

The script consists of the following main parts:

1. **ISBN-13 Check Digit Calculation**:
    - Prompts the user to enter a 12-digit ISBN number.
    - Computes the check digit using the ISBN-13 algorithm.

2. **ISBN-10 Check Digit Calculation**:
    - Prompts the user to enter a 9-digit ISBN number.
    - Computes the check digit using the ISBN-10 algorithm.

3. **Main Loop**:
    - Provides a menu for the user to choose between calculating an ISBN-10 or ISBN-13 check digit, or exiting the tool.
    - Calls the appropriate functions based on the user's choice.

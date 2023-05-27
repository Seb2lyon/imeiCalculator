# imeiCalculator
This simple script is made to find and display the 15th digit of an IMEI when providing the 14 first digits.

Run on Python 3

Doesn't need any third-party module.

## Usage
```bash
imeiCalculator.py [-h] [-v] imei

positional arguments:
  imei           provide the 14 first digits of an IMEI.

options:
  -h, --help     show this help message and exit
  -v, --verbose  display the analysis of the Luhn algorithm.
  ```
## Examples

### Simple mode :

Input

python3 imeiCalculator.py 12345678912345

Output

```bash
The 15th IMEI digit is : 8
The complete IMEI number is : 123456789123458
 ```

### Verbose mode :

Input

python3 imeiCalculator.py 12345678912345 -v

Output

```bash
Luhn key = 0 ---> no match
Luhn key = 1 ---> no match
Luhn key = 2 ---> no match
Luhn key = 3 ---> no match
Luhn key = 4 ---> no match
Luhn key = 5 ---> no match
Luhn key = 6 ---> no match
Luhn key = 7 ---> no match
Luhn key = 8 ---> MATCH !!
Luhn key = 9 ---> no match

The 15th IMEI digit is : 8
The complete IMEI number is : 123456789123458

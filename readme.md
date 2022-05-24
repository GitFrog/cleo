# Canadian Address Cleanning Python Package (ADC) 
<p align="justify">
A spatial data cleaning package specially tailored for Canadian addresses. You might notice that there could be so many kinds of data input errors, such as missing postcode, misspelled street name, misspelled city name, and different types of abbreviations in the address column. It could quickly become a nightmare if we do not clean and standardize these raw address data. Dont worry! This package will help you standardize, autocorrect, and validate address data. 
</p>  

## Requirements
### Python Standard Libraries
 - Pandas
 - regex
 - python-dateutil>=2.7.3
 - pytz>=2017.3
 - numpy>=1.17.3
 - urllib3<1.27,>=1.21.1
 - certifi>=2017.4.17
 - idna<4,>=2.5
 - charset-normalizer~=2.0.0
 - six>=1.5
 
## Installation

```
pip install git+https://github.com/yangg1224/ADC.git
```

## Usage
Features:
* clean_postcode  --> upper case the string; remove the space in the middle; remove the dash
* validate_postal    --> create pattern to validate a postcode; Return True/False
* clean_address      --> standardize, autocorrect, and validate address
* clean_address_without_unitnum  --> standardize, autocorrect, and validate address, remove the unit number in the address
* component_addr      --> Batch process the address column & return six components back to the dataframe


## Examples
Please check the attachment in the code example folder. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgement
Special thanks to MCCSS, who paid me a salary to make this happen. /n
Special thanks to our wonderful team (Tarun, Lee, Michelle, Hong, Jehro, YiCheng)

## License
[MIT](https://choosealicense.com/licenses/mit/)

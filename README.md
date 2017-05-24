<!-- starttoc -->
# Table of contents
- [Dobject](#dobject)
    - [Install](#install)
    - [Usage](#usage)
- [Access all the dictionary keys like object attributes](#access-all-the-dictionary-keys-like-object-attributes)

<!-- endtoc -->

# Dobject

Easily convert dicts to objects. Access key values as object attributes.


## Install
```shell
pip install dobject
```


## Usage

```python
from dobject import DObject
import datetime

dict_data = {'data': [{'effective_date': datetime.datetime(2017, 3, 2, 0, 0),
           'new_symbol': 'MOMENT',
           'old_symbol': '2E'},
          {'effective_date': datetime.datetime(2017, 4, 27, 0, 0),
           'new_symbol': 'AAAG',
           'old_symbol': 'AAAGE'},
          {'effective_date': datetime.datetime(2016, 11, 30, 0, 0),
           'new_symbol': 'PIOI',
           'old_symbol': 'ACPW'}],
 'ticker_changes': [{'new_symbol': 'MOMENT', 'old_symbol': '2E'},
                    {'new_symbol': 'AAAG', 'old_symbol': 'AAAGE'},
                    {'new_symbol': 'PIOI', 'old_symbol': 'ACPW'}]}

obj = DObject(dict_data)

# Access all the dictionary keys like object attributes
print obj.ticker_changes[0].old_symbol
```

You could also access the values like you would with a dictionary.

```python
print obj['ticker_changes'][0]['old_symbol']
```


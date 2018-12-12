# enpass2lastpass.py

This is a simple Python script to convert an Enpass CSV export to a LastPass CSV import.

Tested only with Python 3.7.

## Limitations

This does not handle credit cards, SSIDs, or Android Autofill data.

This will convert logins and secure notes only.

## Usage

```
python enpass2lastpass.py <input file> <output file>
```

## License

MIT License. See LICENSE file.

## Warning

I make no guarantees as to the accuracy of this conversion - it worked well for my password file,
but there is no warranty, expressed or implied, on this code.

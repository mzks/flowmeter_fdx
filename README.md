# flowmeter fdx

Data logger for keyence FD-X flowmeter

## requirement
 - pyserial - `python -m pip install pyserial`
 - USB driver [keyence](keyence.co.jp) if needed.

## Usage 
To write data,
```
python main.py
```
Then send data from FD-X.
After sending, kill the script with Ctrl-C.
`output.csv` will be generated.

The extract notebook is `extract_data.ipynb`

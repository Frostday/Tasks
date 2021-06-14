# Spoken English to Written English Conversion
This Python module uses REST API to convert spoken English in text format to written English. For example, "five dollars" should be converted to $5 and "Triple A" should be written to "AAA" respectively.

# Installation and Setup
1. Fork the repo and clone it
```
git clone https://github.com/Frostday/Tasks.git
cd S2W
```
2. Activate your conda or virtual Python environment
3. To download the required packages run the commands below
```
pip install -r requirements.txt
```
4. Start the backend server
```
cd s2w_english
python api.py
```
5. Open a new terminal inside the S2W directory and run the following command
```
python run.py
```

# Usage
After starting the backend server:
```
from s2w_english.convert import convert_s2w

text = input("Enter spoken text: ")
out = convert_s2w(text)
print("Output: " + out)
```

# Future Updates
- Making converter more robust by adding dates functionality and more keywords like ruppees, millions etc.
- Using a deep learning model for doing these conversions instead of doing them manually.

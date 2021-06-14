# Spoken English to Written English Conversion
This Python module uses REST API to convert spoken English in text format to written English. For example, "five dollars" should be converted to $5 and "Triple A" should be written to "AAA" respectively.

# Installation and Setup
1. Fork the repo and clone it
```
git clone https://github.com/Frostday/Tasks.git
cd Classes-CLI
```
2. Activate your conda or virtual Python environment
3. To download the required packages run the commands below
```
pip install -r requirements.txt
```
4. Now you can use the CLI. Use the following command to see the help menu
```
python cli.py --help
```

# Usage
- Adding a new class object:
```
python cli.py add -n <name> -t <A/B/C>
```
- Deleting a class object
```
python cli.py delete -n <name>
```
- Executing a class object with data
```
python cli.py execute -n <name> -a [<a1>,<a2>,...]
```

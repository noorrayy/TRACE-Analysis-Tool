# TRACE Analysis Tool - Advanced Version

This is an advanced version of TRACE tool with GUI and CLI support.

## Features
- Trace execution of functions
- Generate logs, bar graphs, and Excel reports
- CLI and GUI versions available
- Example program included

## Installation
1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies:
   pip install -r requirements.txt

## Usage
### CLI:
1. Run your program that uses the tracer (examples/sample_program.py)
2. Run analysis:
   python main.py

### GUI:
1. Run GUI:
   python gui.py
2. Select your trace log file and click Analyze

## Example Output
- `results/trace_log.txt` - log file
- `results/execution_summary.png` - execution graph
- `results/execution_report.xlsx` - summary report

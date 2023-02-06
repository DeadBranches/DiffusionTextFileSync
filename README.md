## How to use

This script can be used as a standalone command line tool or imported as a module in your Python code. 

### Standalone command line tool

To use the script as a standalone tool, you can run the following command in your terminal:

    python copy_files_module.py input_dir reference_dir [-v|--verbose]

The first argument `input_dir` is the directory containing PNG files. The second argument `reference_dir` is the directory containing the corresponding text files. The optional `-v` or `--verbose` flag enables verbose output.

### As a module

To use the script as a module in your Python code, you can import it and call the `copy_files` function.

```
python
import copy_files_module

input_dir = 'path/to/input_dir'
reference_dir = 'path/to/reference_dir'
verbose = True

copy_files_module.copy_files(input_dir, reference_dir, verbose)
```

The `copy_files` function takes three arguments: `input_dir`, `reference_dir`, and `verbose`. `input_dir` is the directory containing PNG files. `reference_dir` is the directory containing the corresponding text files. `verbose` is a boolean value that, when set to True, enables verbose output.

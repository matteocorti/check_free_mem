
 (c) Matteo Corti, ETH Zurich, 2007-2012

 (c) Matteo Corti, 2007-2019

  see AUTHORS for the complete list of contributors

# check_free_mem

check_free_mem is a Nagios plugin that checks the amount of free real
memory on a Linux system

## Usage

```
check_free_mem --critical=critical --warning=warning
           [--verbose]
           [--version|--help]

Mandatory arguments:
 --critical,-c   critical   specify the minumal percentage free memory
 --warning,-w    warning    specify warning threshold for the percentage of free memory

Options:
 --version,V                print version number
 --verbose,-v               be more verbose (can be repeated)
```

## Bugs

Report bugs to https://github.com/matteocorti/check_free_mem/issues

# Pipeline

Run series of shell commands with Python. Work in progress.

Motivation for this was to have my own custom pipeline tool to run from PowerShell on Windows with Python Standard Library, but pipeline is now written so that it can be used in different platforms.

## Configuration

Commands to be executed are written in `config.json` file. Below are some examples:


Bash:
```
[
    "ls -l",
    "dig example.com"
]
```

PowerShell:
```
[
    "Get-ChildItem",
    "Resolve-DnsName example.com",
] 
```


## Dependencies

- Python 3

## Tests

Tested manually with: 

Python 3.9.1 on Windows

Python 3.6.9 on Linux

## TODO

- Output to a file

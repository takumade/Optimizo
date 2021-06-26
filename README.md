# Optimizo

 [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic)](http://python.org) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) 

Is a tool for optimizing Laravel projects



## How to install

1. Clone it 

```git clone https://github.com/takumade/Optimizo.git```

2. Navigate to it

```cd Optimizo```

3. Install requirements

```pip install -r requirements.txt```

4. Execute 

```python optimizo laravel -tcjsg```


## How to run

Optimizo accepts the following options and arguments

```
usage: optimizo [-h] [-t] [-c] [-j] [-s] [-g] [-u] project_type

Optimize Laravel project and push it to Github

positional arguments:
  project_type          type of project e.g laravel

optional arguments:
  -h, --help            show this help message and exit
  -t, --html            Optimize HTML
  -c, --css             Optimize CSS
  -j, --js              Optimize JS
  -s, --shared-hosting  Modifies laravel so its shared hosting ready. Works only with      
                        Laravel
  -g, --github          Push project to github.
  -u, --unoptimize      Unoptimize project back to the way it was.

Happy Optimizing!
```




## How to do tests

```
 python -m unittest discover tests
```

## Say hello

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40Code%20Mafia)](https://twitter.com/code_mafia_)

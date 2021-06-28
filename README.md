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
  project_type          type of project e.g larave, rn, flutter  

optional arguments:
  -h, --help            show this help message and exit
  -t, --html            Optimize HTML
  -c, --css             Optimize CSS
  -j, --js              Optimize JS
  -s, --shared          Modifies laravel so its shared hosting ready.       
                        Works only with Laravel
  -d, --dev             Modifies laravel so its dev ready. Works only if    
                        was modified to `shared hosting ready` by optimizo  
                        previously
  -g, --github          Push project to github.
  -w DIRECTORY, --directory DIRECTORY
                        Working directory. Directory with your project      

Happy Optimizing!
```


## How does it work

```
1. Fetches assets url from blade files   [✔️]
2. Finds the actual location of the assets   [ ]
3. Optimizes the assets and renames them e.g hello.js -> hello.min.js  [ ]
4. Rename assets name blade files e.g src="{{ asset('hello.js')  }}" -> src="{{ asset('hello.min.js')  }" [ ]
5. Change project to production [ ]
6. Change project to shared hosting ready [ ]
```




## How to do tests

```
 python -m unittest discover tests
```

## Say hello

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40Code%20Mafia)](https://twitter.com/code_mafia_)

# Optimizo
Optimizo its an tool that allows to set up instructions and run them later. In the mean you will have to run them manually


# How to Install
1. Clone it 

`git clone https://github.com/takumade/Optimizo.git`

2. Install Requirements

`cd Optimizo && pip install -r requirements`

3. Play

`python optimizo.py -h`



## How does it work

1. You create your config file
      `optimizo.py -c`   OR  `optimizo.py -c -w .`

    It will generate something like this:
    
```
{
    "develop": [{
        "name": "copy",
        "src": "C:\\xampp\\htdocs\\projects\\Optimizo\\config.py",
        "dst": "C:\\xampp\\htdocs\\projects\\Optimizo\\classes"
    }, {
        "name": "replace",
        "src": "C:\\xampp\\htdocs\\projects\\Optimizo\\config.py",
        "search": "excluded_folders",
        "replace": "excluded_beans"
}]}
```

2. You then add your instructions like this
     `optimizo.py -g develop -a`

     It will ask you for command name and extra details.
     You can also add multiple instructions like these

     **Note:*** If a group is not available it is added

3. Run your group of instruction
    `optimizo.py -r develop`
    
**Note:** If you know what you are doing you can manually modify `optimizo.json`
**Note:** Instructions are run one after the other.

## Instructions

Here is a list of supported intructions


| Instruction | Description | Implemented|
| ----------- | ----------- |------------|
| move | Move a file from one part to another | Yes
| copy | Copy a file from source to dest | Yes
| replace | Replace text in a file | Yes
| minify | Minify text in a file | Yes
| command | Execute a command | Yes


### Todo

- [x] Remove Ununsed files
- [x] Implement command instructions
- [x] Implement minify instructions
- [ ] Add setup.py
- [ ] Do a blog
            
### What am i doing with this tool
- I use it optimize my Laravel projects


import os
import json
import shutil
import re

class RunInstructions:
    def __init__(self, group, directory):
        self.group = group
        self.directory = directory
        self.filename = os.path.join(self.directory, "optimizo.json")
        
        self.fetch_instructions()
   

    def fetch_instructions(self):
        with open(self.filename) as readobj:
            try:
                data = json.load(readobj)
                
                if self.group in data.keys():
                    instructions = data[self.group]
                    self.run_instructions(instructions)
                else:
                    print("[-] Group doesnt exist...")
            except json.JSONDecodeError:
                print("[-] Please try adding an instruction")
            
    def run_instructions(self, instructions):
        for ins in instructions:
            ins_name = ins["name"]
            
            if ins_name == "move":
                self.move_ins(ins)
            elif ins_name == "copy":
                self.copy_ins(ins)
            elif ins_name == "replace":
                self.replace_ins(ins)
            
        print("[+] Done executing instructions")
                    

    def move_ins(self,obj):
        src_file = obj["src"]
        dst_path = obj["dst"]
        
        print("Moving {0} to {1}".format(src_file, dst_path))
        shutil.move(src_file, dst_path)
    
    def copy_ins(self,obj):
        src_file = obj["src"]
        dst_path = obj["dst"]
        
        print("Copy {0} to {1}".format(src_file, dst_path))
        shutil.copy(src_file, dst_path)
        
    
    def replace_ins(self, obj):
        file_name = obj["src"]
        search_str = obj["search"]
        repl_str = obj["replace"]
        
        print("[+] Replacing {0} with {1}".format(search_str, repl_str))
        
        with open(file_name, "r+") as f:
            text = f.read()
            text = re.sub(search_str, repl_str, text)
            f.seek(0)
            f.write(text)
            f.truncate()
        
    
    
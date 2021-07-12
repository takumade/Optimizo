import os
import json

class AddInstruction:
    def __init__(self,group, name, target_dir):
        self.group = group
        self.name = name
        self.target_dir = target_dir
        
        self.retry_adding = 0
        
        
        if (self.name == "move"):
            self.get_move()

        
        
    def add_instruction(self, instruction_object):
        filepath = os.path.join(self.target_dir, "optimizo.json")
        with open(filepath) as obj:
            try:
                data = json.load(obj)
                
                if self.group in data.keys():
                    data[self.group].append(instruction_object)
                else:
                    data[self.group] = []
                    data[self.group].append(instruction_object)
                    
                with open(filepath, "w") as outfile:
                    json.dump(data, outfile)
            except json.decoder.JSONDecodeError:
                with open(filepath, "w") as outfile:
                    data = {}
                    
                    with open(filepath, "w") as outfile:
                        json.dump(data, outfile)
                        
                if self.retry_adding < 2:
                    self.add_instruction(instruction_object)
                        
                
                    
        
        
    def get_move(self):
        source_file = input("Source File: ")
        dest_file = input("Dest Directory: ")
        
        
        
        if (os.path.exists(os.path.abspath(source_file))):
            self.add_instruction(
                {
                    "name": self.name,
                    "src": source_file,
                    "dst": dest_file
                }
            )
        else:
            print("[-] Source file doesnt exist, exiting...")
        
        
        
        
        
        
    
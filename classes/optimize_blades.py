import os
from tinydb import TinyDB, Query
import config
import re

import config

class OptimizeBlades:
    
    def __init__(self, seed_directory, session_id, db):
        self.seed_directory = seed_directory
        self.session_id = session_id
        self.db = db
        self.used_js_files = []
        self.used_css_files = []
        
        
    def append_to_used(self, lst):
        for f in lst:
            if f.endswith("js"):
                self.used_js_files.append(f)
                
            elif f.endswith("css"):
                self.used_css_files.append(f)
        
    
    def pull_css_files(self, txt):
        files =  re.findall("href.*\.css", txt)
        cleaned = self.clean_files(files)
        self.append_to_used(cleaned)
    
    def pull_js_files(self, txt):
        files =  re.findall("src.*\.js", txt)
        cleaned = self.clean_files(files)
        self.append_to_used(cleaned)
 
    def clean_files(self,files):
        new_files = []
        
        replace_dict = config.app_config["resource_clean"]

        for f in files:
            
            if (".min." in  f):
                continue
            else:
                cleaned_file =  f.strip().replace(" ", "") 
                
                for k in replace_dict.keys():
                    cleaned_file = cleaned_file.replace(
                        k,
                        replace_dict[k]
                    )
                
                new_files.append(cleaned_file)
                

        return new_files
            
                
    
    def begin_optimization(self):
        files_to_be_optimized = []
        folders_to_skip = config.app_config["excluded_folders"]
       
        for path, directories, files in os.walk(self.seed_directory):
            skip_loop = False
            
            for folder in folders_to_skip:
                if (path.endswith(folder) or folder in path):
                    skip_loop = True
                    break
                
            if (skip_loop):
                continue
            
            
            for file in files:
                abs_filepath = os.path.join(path, file)
                if (".blade." in abs_filepath):
                    files_to_be_optimized.append(abs_filepath)  
                
                    
                

                
        table = self.db.table('blade_files')
        table.insert({
            'session_id': self.session_id,
            'file_names': files_to_be_optimized 
        })
        
        self.pull_used_resources(files_to_be_optimized)
        
    
    
    
    
    def pull_used_resources(self, files):
     
        for file in files:
            with open(file, 'r') as f:
                try:
                    file_lines = f.readlines()
                    file_string = " ".join(file_lines)
                    self.pull_css_files(file_string)
                    self.pull_js_files(file_string)
                except UnicodeDecodeError:
                    print("[-] Error - Decode Error")
                
                
                
                
        
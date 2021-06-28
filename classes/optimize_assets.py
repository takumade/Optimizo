import os
from tinydb import TinyDB, Query
import config

class OptimizeAssets:
    
    def __init__(self, seed_directory, session_id, db):
        self.seed_directory = seed_directory
        self.session_id = session_id
        self.db = db
        
    
    def begin_optimization(self):
        # files = os.walk(self.seed_directory)
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
                
                if (".min." in abs_filepath):
                    continue
                
                if ((abs_filepath.endswith(".css") or abs_filepath.endswith(".js"))):
                    files_to_be_optimized.append(abs_filepath)
                
                # print('found %s' % abs_filepath)
                
        table = self.db.table('optimized_files')
        table.insert({
            'session_id': self.session_id,
            'file_names': files_to_be_optimized 
        })
        
        
        # Now begin optimizing files
                
        
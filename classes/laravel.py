import os

class Laravel:
    def __init__(self, optimize_html=True, development_ready=False, optimize_css=True, optimize_js=True, shared_hosting=True ):
        self.optimize_html = optimize_html
        self.optimize_js = optimize_js
        self.optimize_css = optimize_css
        self.shared_hosting = shared_hosting
        self.development_ready = development_ready
        
        self.cwd = ""
        
        
    def is_laravel_project(self):
        file_list = os.listdir()
        status = True
        
        if ("public" not in file_list):
            status = False
        
        if ("resources" not in file_list):
            status = False
            
        if ("composer.json" in file_list):
            with open(os.path.join(os.getcwd(), "composer.json")) as f:
                lines = f.readlines()
                file_str = " ".join(lines)
               
                if ( "laravel/framework" not in file_str):
                    status = False
        else:
            status = False
            
            
        return status
            
        
        
        
        
    
    def optimize(self, directory):
        # Change dir 
        absdir = os.path.abspath(directory)
        os.chdir(absdir)
        
        
        
        if (self.is_laravel_project()):
            print("[*] Optimizing project")
            self.optimize_project()
        else:
            print("[-] Not a laravel project. Quitting!!!")
        
        
        if (self.shared_hosting):
            self.make_development_ready()
            
    def unoptimize(self):
        self.unoptimize_project()
        
        if (self.development_ready):
            self.make_development_ready()
    
        
    def optimize_project(self):
        pass

    def make_shared_hosting_ready(self):
        pass
    
    def push_to_github(self):
        pass
    
    def unoptimize_project(self):
        pass

    def make_development_ready(self):
        pass
        
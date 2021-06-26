class Laravel:
    def __init__(self, optimize_html=True, development_ready=False, optimize_css=True, optimize_js=True, shared_hosting=True ):
        self.optimize_html = optimize_html
        self.optimize_js = optimize_js
        self.optimize_css = optimize_css
        self.shared_hosting = shared_hosting
        self.development_ready = development_ready
        
    
    def optimize(self):
        self.optimize_project()
        
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
        
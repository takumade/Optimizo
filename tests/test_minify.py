import unittest
import os

from classes import minify

class TestMinify(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMinify, self).__init__(*args, **kwargs)
        self.min = minify.Minify()
        
    def test_html_minify(self):
        self.assertEqual(self.min.html_str('  <p>yolo<a  href="/" >o </a >     <!-- hello --></p>'), '<p>yolo<a href="/" >o </a > </p>')
    
    def test_css_minify(self):
        self.assertEqual(self.min.css_str("body {width: 50px;}\np {margin-top: 1em;/* hi */  }"), '@charset "utf-8";body{width:50px}p{margin-top:1em}')
    
    def test_js_minify(self):
        self.assertEqual(self.min.js_str('var i = 1; i += 2 ;\n alert( "hello  "  ); //hi'), 'var i=1;i+=2;alert("hello  ");')
        
    def test_html_file_minify(self):
        self.min.html_file('./tests/test.html')
        
    def test_css_file_minify(self):
        self.min.css_file('./tests/test.css')
        
    def test_js_file_minify(self):
        self.min.js_file('./tests/test.js')
    

if __name__ == '__main__':
    unittest.main()
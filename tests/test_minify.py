import unittest

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
    

if __name__ == '__main__':
    unittest.main()
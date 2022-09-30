#constants
HTML_HEAD = """
    <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
        </head>
        <body> """ 

HTML_FOOT = """
    </body>
    </html>
"""

class RawPDF:
    def __init__(self, json_content) -> None:
        self.json_content = json_content
    
    
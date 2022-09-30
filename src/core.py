#for converting json into pdf
from presentation import Presentation
#my module for color for string
from props import bcolors

def exportJsonToFile(json_content):
    # get the content type of passed json
    if json_content['file']['raw-pdf'] == "True":
        # exporting just raw pdf (means the text will be at one page)
        ()
    else:
        # exporting slides (ppt or pdf)
        presentation = Presentation(json_content)
        
        match json_content['file']['export-format']:
            case "ppt":
                return presentation.exportPPT()
            case "pdf":
                return presentation.exportPDF()
            case _:
                pass # when there is an unrecognized file format

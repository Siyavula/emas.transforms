import cnxmlplus2shortcodecnxml
import shortcodecnxml2shortcodehtml
import shortcodehtml2html
import sys

SAVE_INTERMEDIATE = False

# Temp storage for output from transforms
class Data:
    text = None
    def setData(self, text):
        self.text = text
output = Data()

# Read filenames from command line
if len(sys.argv) not in [2, 3]:
    print 'Usage: %s filename.xml [output.html]'%sys.argv[0]
    sys.exit()
inputFilename = sys.argv[1]
if len(sys.argv) == 3:
    outputFilename = sys.argv[2]
else:
    outputFilename = 'output.html'

# Read input
with open(inputFilename, 'rt') as fp:
    cnxmlplus = fp.read()

# Transform
cnxmlplus2shortcodecnxml.cnxmlplus_to_shortcodecnxml().convert(cnxmlplus, output)
shortcodecnxml = output.text
if SAVE_INTERMEDIATE:
    with open(outputFilename + '.shortcodecnxml', 'wt') as fp:
        fp.write(shortcodecnxml)

shortcodecnxml2shortcodehtml.shortcodecnxml_to_shortcodehtml().convert(shortcodecnxml, output)
shortcodehtml = output.text
if SAVE_INTERMEDIATE:
    with open(outputFilename + '.shortcodehtml', 'wt') as fp:
        fp.write(shortcodehtml)

shortcodehtml2html.shortcodehtml_to_html().convert(shortcodehtml, output)
html = output.text

# Write output
with open(outputFilename,'wt') as fp:
    fp.write(html)

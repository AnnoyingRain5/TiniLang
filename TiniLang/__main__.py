import sys
import TiniLang

filename = sys.argv[-1]
sourcecode = TiniLang.load_source(filename)

if sourcecode:
    TiniLang.evaluate(sourcecode)

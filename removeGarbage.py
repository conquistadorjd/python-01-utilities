import string
tempvar = "PLOT NO-27-29,APEX CLG├╜├╜NANAKRAMGUDA,HYD,├╜├╜PIN-500032├╜├╜"
print tempvar
newvar = "".join(filter(lambda char: char in string.printable, tempvar))
print newvar
# Rebecca Norwood
# CS 351 - HW 3: Single Line Lexer (NO GUI)

# Keywords:	if	else	int	float
# Operators:	=	+	>	*
# Separators:	(	)	:	“   “	;

# Identifiers:	letters, or letters followed by digits
# Int_literal:	only integers
# Float_literal: 	only float
# String_literal:	only strings
#(\w+\s*)(?=\")

#r'[A-Za-z]+\d+|[A-Za-z]+': 'id'


def CutOneLineTokens(input):
    import re

    output = [] #Output list containing tokens with corresponding type

    #Created a dictionary to hold specific regex expressions with corresponding values (except string)
    tokenList = {r'\b(if|else|int|float)(?=\s|\t)': 'key',
                 r'[A-Za-z]+\d+|[A-Za-z]+': 'id',
                 r'[=+>*]': 'op',
                 r'^\d+(?![\d+\.])': 'lit', #int literal
                 r'\d+\.\d+': 'lit', #float literal
                 r'[():\";]': 'sep',
                 r'[\t]+|[ ]+': 'space'}

    tempString = input

    while len(tempString) != 0:
        for x in tokenList:
            token = re.match(x, tempString)
            if token:
                if tokenList[x] == 'space': #Remove spacing/tabs without appending to list
                    pos = token.end()
                    tempString = tempString[pos:]
                elif tokenList[x] == 'sep' and tempString[0] == '\"': #String condition to check for edge cases
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos = token.end()
                    tempString = tempString[pos:]
                    strRgx = re.match(r'^(.)+?(?=\")', tempString) #string lteral regex match
                    if strRgx:
                        output.append('<' + 'lit' + ',' + strRgx.group() + '>')
                        pos = strRgx.end()
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos += 1
                    tempString = tempString[pos:]
                else:
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos = token.end()
                    tempString = tempString[pos:]

    print('Output <type,token> list: ', output)


if __name__ == '__main__':
    CutOneLineTokens("int	A1=5")
    CutOneLineTokens("float BBB2	=1034.2")
    CutOneLineTokens("float	cresult	=	A1	+BBB2	*	BBB2")
    CutOneLineTokens("if	(cresult	>10):")
    CutOneLineTokens("		print(\"TinyPie    \"    )")
    CutOneLineTokens("print(\"Hello World!\" + \"I'm Rebecca\")")
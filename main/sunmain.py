# no comp theory stuffs already supports print and assignment printing and var print in 24 lines
ASSIGN_KEYWORD = "eq"
PRINT_KEYWORD  = "puts"

NEWLINE = "\n"

vars = {} #global to be accessible from outside

reader = open("source.ss","r")
sourceText = reader.read().split(NEWLINE)
txt = []
def lexParse(txt):
    global vars
    for statement in txt:
        words = statement.split()
        for index,current in enumerate(words): #puts "wreger" q
            if current == ASSIGN_KEYWORD:
                var = ' '.join(words[:index])
                value = ' '.join(words[index+1:])
                vars[var] = value
                
            elif current == PRINT_KEYWORD:
                for i in range(len(words)):
                    if words[i][0] != '"':
                        if words[i] in vars:
                            words[i] = vars[words[i]]
                print(' '.join(words[1:]).replace('"',''))
        
lexParse(sourceText)

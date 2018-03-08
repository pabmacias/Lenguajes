
L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z']

N = ['1','2','3','4','5','6','7','8','9']

valTok = []
tok = []
tokNames = ["Inicial", "Variable", "Entero", "Real", "Suma", "Resta", "Multiplicacion",
            "Asignacion", "Division", "Potencia", "Parentesis Abre", "Parentesis Cierra", "Comentario"]

table = [
            [['\n', ' '],         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', '$', '$', '/', '$', '(', '$', '$'],
            [    '\n'   , [L, N, '_', ' '],    '$'  ,         '$'      , '+', '‐', '*', '=', '/', '^', '(', ')', '$'],
            [    '\n'   ,        '$'      , [N, ' '],   ['.', 'E', 'e'], '+', '‐', '*', '=', '/', '^', '(', ')', '$'],
            [    '\n'   ,        '$'      ,    '$'  ,[N, ' ', 'E', 'e', '‐'], '+', '‐', '*', '=', '/', '^', '(', ')', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], ' ', '$', '$', '$', '$', '$', '(', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', ' ', '$', '$', '$', '$', '(', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', ' ', '$', '$', '$', '(', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', '$', ' ', '$', '$', '(', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', '$', '$', ' ', '$', '(', '$', '/'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', '$', '$', '$', ' ', '(', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '$', '$', '$', '$', '$', '$', ' ', '$', '$'],
            [     '$'   ,         L       , [N, '‐'],   ['.', 'E', 'e'], '+', '‐', '*', '=', '/', '^', '(', ' ', '$'],
            [    '\n'   ,        '$'      ,    '$'  ,         '$'      , '$', '$', '$', '$', '$', '$', '$', '$', [' ', L, N, '+', '‐', '*', '=', '/', '^', '(', ')']],
        ]

def checkToken(ent, prev):
    step = 0
    vi = 0
    for vt in valTok:
        print(tok[vi])
        print(tokNames[vt])
        vi += 1
    print("\n")
    for to in table[prev]:
        #print(step)
        for params in to:
            for p in params:
                #print(ent[0] + " = " + p)
                if (ent[0] == p):
                    if (len(valTok) > 0):
                        if (valTok[len(valTok)-1] != step):
                            if(valTok[len(valTok)-1] == 8 and step == 12):
                                valTok[len(valTok)-1] = step
                                tok[len(tok)-1] += ent[0]
                            elif(valTok[len(valTok)-1] == 2 and step == 3):
                                valTok[len(valTok)-1] = step
                                tok[len(tok)-1] += ent[0]
                            else:
                                valTok.append(step)
                                tok.append(ent[0])
                        else:
                            tok[len(tok)-1] += ent[0]
                    else:
                        valTok.append(step)
                        tok.append(ent[0])
                    if (len(ent) > 1):
                        checkToken(ent[1:], step)
                    else:
                        vi = 0
                        for vt in valTok:
                            print(tok[vi])
                            print(tokNames[vt])
                            vi += 1
        step += 1

#checkToken("a = 32.4 *(‐8.6 ‐ b)/       6.1E‐8", 0)
with open('tokens.txt', 'r') as myfile:
    data=myfile.read()
    checkToken(data, 0)

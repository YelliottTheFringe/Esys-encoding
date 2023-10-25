# eSYS module, for encryption
eSYSa=["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","!","A","B","C","O","H","E","D","_","-"," "]
eSYSb=[1,2,3,11,12,13,21,22,23,31,32,33,41,42,43,51,52,53,61,62,63,71,72,73,81,82,83,91,92,93,101,102,103,201,202,203,301,302,303,401,402,403,501,502,503,601,602,603]# base 3 system.

def encode_to_LST(plainTXT,key):
    plainLST=[]
    keyLST=[]
    cipherLST=[]
    for i in plainTXT:
        for x in range(len(eSYSa)):
            if i == eSYSa[x]:
                plainLST.append(eSYSb[x])
    appnum=0
    for i in key:
        for x in range(len(eSYSa)):
            if i == eSYSa[x]:
                keyLST.append(eSYSb[x])
                appnum+=1 

    inverter=1
    for i in plainLST:
        for b in keyLST:
            i-=int(b*inverter/10)
            inverter=(-inverter)
        inverter=-inverter
        cipherLST.append(i)

    for i in keyLST:
        cipherLST.append(i)
    cipherLST.append(appnum)
    return(cipherLST)

def encode_to_STR(plainTXT,key):
    plainLST=[]
    keyLST=[]
    cipherTXT=''
    for i in plainTXT:
        for x in range(len(eSYSa)):
            if i == eSYSa[x]:
                plainLST.append(eSYSb[x])
    appnum=0
    for i in key:
        for x in range(len(eSYSa)):
            if i == eSYSa[x]:
                keyLST.append(eSYSb[x])
                appnum+=1 

    inverter=1
    for i in plainLST:
        for b in keyLST:
            i-=int(b*inverter/10)
            inverter=(-inverter)
        inverter=-inverter
        cipherTXT+=str(i)
        cipherTXT+="n"

    for i in keyLST:
        cipherTXT+=str(i)
        cipherTXT+="n"
    cipherTXT+=str(appnum)
    return cipherTXT

def STRdecode_to_STR(cipherTXT):
    codeLST=[""]
    codeINTS=[]
    AplainLST=[]
    keyLST=[]
    ct=0
    plainTXT=""
    for i in cipherTXT:
        if not i =="n":
            codeLST[ct]+=i
        elif i=="n":
            ct+=1
            codeLST.append("")
    try:
        codeLST.remove('[]')
    except Exception as e:
        pass
    # transform to a list of strings
    for a in codeLST:
        codeINTS.append(int(a))
    keyln=codeINTS[-1]
    codeINTS.remove(keyln)
    # GET THE KEY
    for i in range(keyln):
        keyLST.append(codeINTS[-1])
        codeINTS.remove(codeINTS[-1])

    # reverse the mathmatical process
    inverter=1
    for i in codeINTS:
        for b in keyLST:
            i+=int(b*inverter/10)
            inverter=(-inverter)
        inverter=-inverter
        AplainLST.append(i)
    print(AplainLST)
    for b in AplainLST:
        for c in range(len(eSYSb)):
            if eSYSb[c]==b:
                plainTXT+=(eSYSa[c])
    return (plainTXT)    

def STRdecode_to_LST(cipherTXT):

    codeLST=[""]
    codeINTS=[]
    AplainLST=[]
    keyLST=[]
    ct=0
    BplainLST=[]
    for i in cipherTXT:
        if not i =="n":
            codeLST[ct]+=i
        elif i=="n":
            ct+=1
            codeLST.append("")
    codeLST.remove('')
    print(codeLST)
    # transform to a list of strings
    for a in codeLST:
        codeINTS.append(int(a))
    print(codeINTS)
    keyln=codeINTS[-1]
    codeINTS.remove(keyln)
    # GET THE KEY
    for i in range(keyln):
        keyLST.append(codeINTS[-1])
        codeINTS.remove(codeINTS[-1])
        print(i)

    # reverse the mathmatical process
    inverter=-1
    for i in codeINTS:
        for b in keyLST:
            i+=int(b*inverter/10)
            inverter=(-inverter)
        inverter=-inverter
        AplainLST.append(i)
    print(AplainLST)
    for b in AplainLST:
        for c in range(len(eSYSb)):
            if eSYSb[c]==b:
                BplainLST.append(eSYSa[c])
    return (BplainLST)    
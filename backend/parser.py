import math

OPS = {'+':1,'-':1,'*':2,'/':2,'%':2,'^':3}
FUNCS = {'sin':math.sin,'cos':math.cos,'tan':math.tan,'sqrt':math.sqrt,'log':math.log10}

def tokenize(expr):
    tokens=[]; i=0
    while i<len(expr):
        c=expr[i]
        if c.isspace(): i+=1; continue
        if c.isdigit() or c=='.':
            j=i
            while j<len(expr) and (expr[j].isdigit() or expr[j]=='.'): j+=1
            tokens.append(expr[i:j]); i=j; continue
        if c.isalpha():
            j=i
            while j<len(expr) and expr[j].isalpha(): j+=1
            tokens.append(expr[i:j]); i=j; continue
        tokens.append(c); i+=1
    return tokens

def to_postfix(tokens):
    out=[]; st=[]
    for t in tokens:
        if t.replace('.','',1).isdigit(): out.append(t)
        elif t in FUNCS: st.append(t)
        elif t in OPS:
            while st and st[-1] in OPS and OPS[st[-1]]>=OPS[t]: out.append(st.pop())
            st.append(t)
        elif t=='(':
            st.append(t)
        elif t==')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()
            if st and st[-1] in FUNCS: out.append(st.pop())
    while st: out.append(st.pop())
    return out

def eval_postfix(post):
    st=[]
    for t in post:
        if t.replace('.','',1).isdigit(): st.append(float(t))
        elif t in OPS:
            b=st.pop(); a=st.pop()
            st.append({'+':a+b,'-':a-b,'*':a*b,'/':a/b,'%':a%b,'^':a**b}[t])
        else:
            a=st.pop(); st.append(FUNCS[t](math.radians(a)) if t in ['sin','cos','tan'] else FUNCS[t](a))
    return round(st[-1],6)

def calculate(expr):
    return eval_postfix(to_postfix(tokenize(expr)))
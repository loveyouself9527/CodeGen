

#生成代码
def GenCode(sig):
    if(isOC(sig)):
        return GenOC(sig)
    else:
        return GenC(sig)

def isOC(sig):
    if "[" in sig:
        return True
    return False

def GetOCArgCount(sig):
    s1 = sig.split(":")
    print(s1)
    return len(s1) - 1

def GetClassName(sig):
    s1 = sig.split("[")
    s2 = s1[1]
    s3 = s2.split(" ")
    print("className==> " + s3[0])
    return s3[0]

def GetOCsigNature(sig):
    s1 = sig.split("[")
    s2 = s1[1]
    s3 = s2.split("]")
    print("sigNature==> " + s3[0])
    return s3[0]

def GetFunName(sig):
    ret = ""
    signature = GetOCsigNature(sig)
    s1 = signature.split(" ")
    s = s1[1]
    s2 = s.split(":")
    ret = GetClassName(sig) + "_"
    for item in s2:
        ret = ret + item + "_"
    return ret

def GetArgsType(sig):
    #(id a1, SEL a2, id a3, id a4, id a5)
    s = sig.split("(")
    s1 = s[1]
    s2 = s1.split(")")
    s3 = s2[0]
    s5 = s3.split(",")
    return s5[2:]

def GetArgTypeById(sig,index):
    ret = GetArgsType(sig)
    return ret[index]

def GetPrintArgs(sig):
    ret = "\n"
    pattern = '''console.log("abcd1 a22==> " + a23)\n'''
    fnName = GetFunName(sig)
    argCount = GetOCArgCount(sig)
    for i in range(argCount):
        argType = GetArgTypeById(sig,i)
        arg = ""
        if "id" in argType:
            arg =  f"ObjC.Object(args[{i+2}])"
        else:
            arg = f"(args[{i+2}])"
        p1 = pattern.replace("abcd1",fnName)
        p1 = p1.replace("a22","a"+ str(i+2))
        p1 = p1.replace("a23",arg)
        ret = ret + p1
    print(ret + "xxx")
    return ret

#是否是类方法
def isClassFun(sig):
    if "+" in sig:
        return True
    else:
        return False

def GenOCClanssFunCode(sig):
    argCount = GetOCArgCount(sig)
    className = GetClassName(sig)
    sigNature = GetOCsigNature(sig)
    fnName = GetFunName(sig)
    PrintArgs = GetPrintArgs(sig)
    args = "\n"
    for i in range(argCount + 2):
        args = args + "\tthis.a" + str(i) + " = " + "args[" + str(i) + "]\n"

    s1 = f'var {fnName} = ObjC.classes["{className}"]["{sigNature}"];'
    patternOC ='''Interceptor.attach(abcd1.implementation, {
        onEnter: function (args) {
            console.log("\\n" + "--".repeat(32));
            var module = Process.findModuleByAddress(this.context.lr);
            var off = this.context.lr.sub(module.base)
            console.log("===offset===>" + off)
            // console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join("\\n\\t"));
            abcd2
            abcd3
        },
        onLeave: function(returnValues) {
        }
    });
    '''
    patternOC = patternOC.replace("abcd1",fnName)
    patternOC = patternOC.replace("abcd2", args)
    patternOC = patternOC.replace("abcd3", PrintArgs)
    retcode = s1 + "\n" + patternOC
    print(retcode)
    return retcode


#void __cdecl +[FGESDK sendRequestWithCmd:data:complete:](id a1, SEL a2, id a3, id a4, id a5)
def GenOC(sig):
    if(isClassFun(sig)):
        #类方法
        return GenOCClanssFunCode(sig)
    else:
        #常用方法
        return GenC(sig)

def GetC_funName(sig):
    s0 = sig.split("sub_")[1]
    return "sub_" + s0.split("(")[0]

def GetC_funOffset(sig):
    name = GetC_funName(sig)
    return "0x" + name.split("sub_")[1]

def GetC_argsCount(sig):
    return len(sig.split(","))

def GetC_argTypeByIndex(sig,index):
    s = sig.split("(")[1]
    s1 = s.split(")")[0]
    arrs = s1.split(",")
    return arrs[index]

def GetCPrintArgs(sig):
    funName = GetC_funName(sig)
    ret = ""
    args = "\n"
    for i in range(GetC_argsCount(sig)):
        args = args + "\tthis.a" + str(i) + " = " + "args[" + str(i) + "]\n"
    ret = ret + args
    for i in range(GetC_argsCount(sig)):
        pattern = f'console.log("{funName} a{i}==> " + (args[{i}]))'
        ret = ret + pattern + "\n"
    return ret

#_QWORD *__fastcall sub_2BEEF4(char *a1, const char *a2)
def GenC(sig):
    funName = GetC_funName(sig)
    funOffset = GetC_funOffset(sig)
    print(funName)

    PrintArgs = GetCPrintArgs(sig)

    retval = f'console.log("{funName} ret ==> (returnValues)")'

    pattern = '''Interceptor.attach(base.add(offset), {
        onEnter: function (args) {
            console.log("\\n"+"--".repeat(32));
            var module = Process.findModuleByAddress(this.context.lr);
            var off = this.context.lr.sub(module.base)
            console.log("===offset===>" + off)
            //console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join("\\n\\t"));
            abcd2
        },
        onLeave: function(returnValues) {
            abcd3
        }
    });'''

    patternC = pattern.replace("offset",funOffset)
    patternC = patternC.replace("abcd2", PrintArgs)
    patternC = patternC.replace("abcd3", retval)
    print(patternC)
    return patternC
    pass


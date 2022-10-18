import execjs

node=execjs.get()

ctx=node.compile(open('./wechat.js',encoding='utf-8').read())

funcName='getPwd("{0}")'.format('12345678')

pwd=ctx.eval(funcName)
print("加密之后:",pwd)
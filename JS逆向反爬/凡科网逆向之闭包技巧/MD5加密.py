import execjs
node=execjs.get()
ctx=node.compile(open('./fanke.js',encoding='utf-8').read())
funcName='md5("{0}")'.format('654321')
pwd=ctx.eval(funcName)
print(pwd)
#密码为123456
#e10adc3949ba59abbe56e057f20f883e
#密码为654321
#c33367701511b4f6020ec61ded352059
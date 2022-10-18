import execjs
import hashlib

# d
node=execjs.get()
# A.signature:__g._encrypt加密
# with open(r'01.js', 'r' ,encoding='utf-8') as f:
#     ctx1 = execjs.compile(f.read(), cwd=r'C:\Windows\System32\node_modules')
# encrypt_str = ctx1.call('aa')
# print(encrypt_str)# aXYyNg98gwxxb0O80BtBNcrqrLtYNwSqMLF0nJ9qnG2p
#x-zse-96

#
# print(ctx)
# print(ctx.call('aa'))
i = {'url': "https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_ugc&token=MS4wLjABAAAAZ4Hwu5YDysuwNnR85W69NIETIiucQctQRaxwxXneD18&max_behot_time=0&aid=24&app_name=toutiao_web"}

a=execjs.compile("""

function I(o){
    const jsdom = require("jsdom");
    const { JSDOM } = jsdom;
    const dom = new JSDOM('<script src="toutiao.js"></script>');
    window = dom.window;
	var i = (null === (n = window.byted_acrawler) || void 0 === n ? void 0 : null === (r = n.sign) || void 0 === r ? void 0 : r.call(n, o)) || "";
	console.log("dvbb")
	return i
}
""", cwd=r'C:\Windows\System32\node_modules')

print(a.call("aa",i))

# funcName = 'getPwd("{0}","{1}")'.format('123456',key)
# pwd = ctx.eval(funcName)

# print(pwd)
#
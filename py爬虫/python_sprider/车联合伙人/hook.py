# frida 安装并启动完了----》判断一下，我们刚刚找到的加密密码的函数对不对


###### # ###### # ###### # ###### # 1  新建一个py文件，写入###### # ###### # ###### # ###### #
import frida
import sys

rdev = frida.get_remote_device()
# ----- 上面是固定的
session = rdev.attach("油联合伙人")  # 改成app名字

#### 变化的是src，核心是它### 不同app写法不一样，hook不同函数也不一样  js代码

scr = """
Java.perform(function () {
    //use中写要hook的函数的包名下的类名
    var SecurityUtil = Java.use("com.yltx.oil.partner.utils.Md5");

    //替换类中的方法
    SecurityUtil.md5.implementation = function(str){
        console.log("传入的参数：",str);
        var res = this.md5(str); //调用原来的函数
        console.log("返回值：",res);
        return str;
    }
});
"""

# ----=下面也是固定的
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
sys.stdin.read()


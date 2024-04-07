# frida 安装并启动完了----》判断一下，我们刚刚找到的加密密码的函数对不对


###### # ###### # ###### # ###### # 1  新建一个py文件，写入###### # ###### # ###### # ###### #
import frida
import sys

rdev = frida.get_remote_device()
# ----- 上面是固定的
session = rdev.attach("车智赢+")  # 改成app名字

#### 变化的是src，核心是它### 不同app写法不一样，hook不同函数也不一样  js代码

scr = """
Java.perform(function () {
    //use中写要hook的函数的包名下的类名
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");

    //替换类中的方法
    SecurityUtil.encodeMD5.implementation = function(str){
        console.log("传入的参数：",str);
        var res = this.encodeMD5(str); //调用原来的函数
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


##### 2 手机端server必须启动##### ##### ##### #####
##### 3 启动要hook的app ######
#### 4 运行pyton代码######
#### 5 操作可能会使用咱们hook函数的操作### 他就会触发
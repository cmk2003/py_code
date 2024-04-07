
import frida
import sys

rdev = frida.get_remote_device()
# 写成spawn ，放到列表中  app的包名
pid = rdev.spawn(["com.che168.autotradercloud"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {
    // 包.类
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");
    SecurityUtil.encodeMD5.implementation = function(str){
        console.log("明文：",str);
        var res = this.encodeMD5(str);
        console.log("md5加密结果=",res);
        return res;
    }
});
"""



script = session.create_script(scr)
def on_message(message, data):
    print(message, data)
script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()
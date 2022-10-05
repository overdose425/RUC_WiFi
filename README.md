# RUC WiFi: 鹿大校园网自动认证 / 定时连接

## 链接

[overdose425/RUC_WiFi: 深澜认证协议下自动认证校园网 / 校园网定时重连 (github.com)](https://github.com/overdose425/RUC_WiFi)

## 起因

跟鹿大在读的女友出门玩时，心疼她为了工作每次都要背个游戏本出门，不便且厚重，遂寄希望于远程连接在校园的电脑。然而鹿大的校园网断线频率实在太高，为了省心地解决该问题，我参考北航校园网下设置自动连接的方案，编写了鹿大校园网连接脚本。在此处感谢原po作者们！

## 参考

原项目：https://github.com/huxiaofan1223/jxnu_srun  
实现主要参考：https://github.com/FuryMartin/BUAA_WIFI

## 改动

1. 修改了相关url以适配RUC校园网
2. 编码部分debug

## 使用

1. 修改ruc_wifi.py中username和password值为你的网关账号密码
2. 运行ruc_wifi.py 或 运行wifi.bat

## 自动

**【windows下实现】** *感谢原作者@FuryMartin*

1. 按键盘上的`win+S`键，直接打字搜索`任务计划程序`并打开
  
2. 点击`任务计划程序`窗口右上角的创建任务
  
3. 勾选`常规`-`不管用户是否登录都要运行`
  
4. 点击`触发器`-`新建`，将开始任务下拉选择`工作站解锁时`，并设置重复任务时间为`5分钟`，且`永不`停止
  
5. 点击`操作`-`新建`，点击`浏览`，将程序路径设置为wifi.vbe的绝对路径，【特别注意】`起始于`选项设置为本项目文件夹的绝对路径
  ![](https://raw.githubusercontent.com/overdose425/ImgStg/main/2022/10/05-09-57-02-mmc_tjJxoT1363.png)
  
6. 取消勾选条件-`只有在计算机使用交流电源时才启动此任务`
  
7. 点击`确定`

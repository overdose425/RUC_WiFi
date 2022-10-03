# 参考
原项目：https://github.com/huxiaofan1223/jxnu_srun
实现主要参考：https://github.com/FuryMartin/BUAA_WIFI

# 改动
1. 修改了相关url以适配人大网络
2. 编码部分debug

# 使用
1. 修改ruc_wifi.py中username和password值为你的网关账号密码
2. 运行ruc_wifi.py

# windows系统下自动连接
*感谢原作者@FuryMartin*
1.按键盘上的*win+S*键，直接打字搜索"任务计划程序"并打开
2.点击"任务计划程序"窗口右上角的创建任务
3.勾选*常规*-*不管用户是否登录都要运行*
4.点击*触发器*-*新建*，将开始任务下拉选择工作站解锁时，并设置重复任务时间为5分钟，且永不停止
5.点击*操作*-*新建*，点击*浏览*，将程序路径设置为wifi.vbe的绝对路径
6.取消勾选条件-*只有在计算机使用交流电源时才启动此任务*
7.点击*确定*

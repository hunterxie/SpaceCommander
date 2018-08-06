# SpaceCommander
OC代码格式化工具，个人爱好去掉了git hook，格式化代码可根据自己认为适当时机进行，不影响正常提交
<br>
1、cd到git厂库所在目录<br>
```
xll$ cd /Users/xxx/Desktop/github/SpaceCommandDemo 
```
2、clone SpaceCommander到该目录
```
git clone https://github.com/hunterxie/SpaceCommander.git
```
3、执行SpaceCommander目录下的setup-repo.sh脚本
```
xxx:SpaceCommandDemo xxx$ /Users/xxx/Desktop/github/SpaceCommander/setup-repo.sh 
```
执行以上脚本目的是在git根目录下创建.clang-format的快捷方式，同时配置.gitignore添加SpaceCommander和.clang-format两个忽略文件<br>
4、该步骤可选：选择配置你不想参与格式化的文件。创建.formatting-directory-ignore文件到git厂库根目录，打开文件添加需要忽略格式化的文件或文件夹，可参考https://github.com/hunterxie/SpaceCommandDemo<br>
5、执行你想要的git操作，只需要保证在git commit之前 执行format-objc-files.sh脚本即可，该脚本可将git暂存区内所有修改的内容都格式化。本版本已经去掉了git hook，不会干扰提交。如果不执行脚本也依然能够实现正常提交流程。<br>

## 其他介绍
format-objc-files.sh 格式化git所有add的修改过的文件<br>
format-objc-files-in-repo.sh 格式化全工程，忽略文件除外<br>
format-objc-file.sh 格式化单一文件，直接空格跟之间文件路径<br>
.clang-format文件是配置格式化语法，可根据自己的公司要求定制自己的格式化规范<br>

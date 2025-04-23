# Fonts_Migration_Tool
适用于 Windows 的小工具：分析 Fonts 文件夹以迁移字体文件

## 概述
主要的使用场景：更换了新的电脑，想要迁移自行在系统目录安装的字体文件，但不想不小心动到系统字体。

## 使用方法
运行此程序的计算机是“迁移源”（source），而要迁移到的计算机是“迁移目标”（target）。

首先，请在迁移目标上，运行这个命令来生成 Fonts 文件夹的内容清单：

```
dir /b C:\Windows\Fonts > RemoteFonts.txt
```

然后请将生成出的 `RemoteFonts.txt` 文件拷贝到迁移源。

接下来，在迁移源上运行 `Tools.py` 程序。它将读入 `RemoteFonts.txt` 文件，分析出需要迁移的字体文件，并将它们复制到 `FontExport` 文件夹中。

最后，将 `FontExport` 文件夹中的字体文件，有选择性地手动复制进迁移目标的 `Fonts` 文件夹中即可。

## 注意事项
强烈不建议手动操作任何系统自带的字体。如果 `FontExport` 文件夹中包含了任何系统字体，建议删除它们而不是复制到迁移目标。你应该只迁移自己手动安装的字体。

本工具只会处理位于 `C:\Windows\Fonts` 目录下的，被“系统全局安装”的字体。如果你“仅为当前用户安装字体”过，它们是被存储在 `%LOCALAPPDATA%\Microsoft\Windows\Fonts` 目录下的，工具不会处理这些字体，并且也不需要。直接把它整个复制到目标即可，一般不会有问题。

## 免责声明
请自担风险使用此工具。作者不对使用此工具造成的任何损害负责。

Use this tool at your own risk. The author is not responsible for any damage caused by the use of this tool.
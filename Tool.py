import os
import shutil

def load_remote_files():
    """加载远程文件列表并处理大小写（自动使用当前目录的RemoteFonts.txt）"""
    remote_txt_path = os.path.join(os.getcwd(), 'RemoteFonts.txt')
    try:
        with open(remote_txt_path, 'r', encoding='utf-8') as f:
            remote_files = [os.path.basename(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError("找不到 RemoteFonts.txt 文件，请确保它位于程序所在目录")
    except UnicodeDecodeError:
        raise ValueError("文件编码错误，请确保 RemoteFonts.txt 使用 UTF-8 编码")

    remote_lower = {}
    for name in remote_files:
        lower_name = name.lower()
        if lower_name not in remote_lower:
            remote_lower[lower_name] = name
    return remote_lower

def get_local_files():
    """获取本地字体文件并处理大小写"""
    fonts_dir = r'C:\Windows\Fonts'
    try:
        entries = os.scandir(fonts_dir)
    except PermissionError:
        raise PermissionError("无法访问系统字体目录，请检查权限")

    local_lower = {}
    for entry in entries:
        if entry.is_file():
            lower_name = entry.name.lower()
            if lower_name not in local_lower:
                local_lower[lower_name] = entry.name
    return local_lower

def export_files(files_to_export):
    """导出文件到当前目录的FontExport文件夹"""
    fonts_dir = r'C:\Windows\Fonts'
    export_dir = os.path.join(os.getcwd(), 'FontExport')
    
    try:
        os.makedirs(export_dir, exist_ok=True)
    except OSError as e:
        raise OSError(f"无法创建导出目录：{str(e)}")

    exported = []
    for filename in files_to_export:
        src = os.path.join(fonts_dir, filename)
        dst = os.path.join(export_dir, filename)
        try:
            shutil.copy2(src, dst)
            exported.append(filename)
        except FileNotFoundError:
            print(f"警告：文件 {filename} 无法读取，已跳过")
        except Exception as e:
            print(f"复制 {filename} 失败：{str(e)}")
    return exported

def main():
    try:
        print("正在加载远程文件列表...")
        remote = load_remote_files()
    except Exception as e:
        print(f"加载远程文件失败：{str(e)}")
        return

    try:
        print("正在扫描本地字体...")
        local = get_local_files()
    except Exception as e:
        print(f"扫描本地字体失败：{str(e)}")
        return

    # 计算差异
    remote_set = set(remote.keys())
    local_set = set(local.keys())
    
    remote_only = remote_set - local_set
    local_only = local_set - remote_set

    # 显示结果
    print("\n【远端有而本地无的文件】")
    for key in sorted(remote_only):
        print(f" - {remote[key]}")

    print("\n【本地有而远端无的文件】")
    for key in sorted(local_only):
        print(f" - {local[key]}")

    # 自动导出功能
    if local_only:
        print("\n正在导出本地独有文件...")
        files_to_export = [local[key] for key in local_only]
        try:
            exported = export_files(files_to_export)
            export_path = os.path.abspath(os.path.join(os.getcwd(), 'FontExport'))
            print(f"\n成功导出 {len(exported)}/{len(files_to_export)} 个文件到：\n{export_path}")
        except Exception as e:
            print(f"导出过程中发生错误：{str(e)}")
    else:
        print("\n没有需要导出的本地独有文件")

if __name__ == "__main__":
    print("Fonts Migration Tool")
    print("by Remi 2025")
    print("=" * 40)
    main()
    input("\n按 Enter 键退出...")


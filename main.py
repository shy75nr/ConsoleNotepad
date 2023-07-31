import os
import sys
import traceback

import itertools
import colorama
import subprocess


def get_text(string, length):
    print(string)
    a = []
    while True:
        try:
            if 0 < length < 10:
                input_text = f'  {length}  '
            elif 9 < length < 100:
                input_text = f' {length}  '
            elif 99 < length < 1000:
                input_text = f' {length} '
            else:
                input_text = f'{length} '
            a.append(input(input_text))
            length += 1
        except(KeyboardInterrupt, EOFError):
            break
    return a


def read(path):
    try:
        try:
            read_file(path, 'gbk')
        except (UnicodeError, UnicodeDecodeError):
            try:
                read_file(path, 'gb2312')
            except (UnicodeError, UnicodeDecodeError):
                try:
                    read_file(path, 'utf-8')
                except (UnicodeError, UnicodeDecodeError):
                    try:
                        read_file(path, 'ANSI')
                    except (UnicodeError, UnicodeDecodeError):
                        print(colorama.Fore.RED + '文件读取错误!')
    except FileNotFoundError:
        print(colorama.Fore.RED + '文件不存在,可能是因为未创建或未保存')


def get_path():
    try:
        path = sys.argv[1]
        read(path)
    except IndexError:
        path = ''
    if path == '':
        try:
            with open(os.path.dirname(sys.argv[0]) + '\\notepad.log', 'rt') as fo:
                paths = fo.readlines()[-20: -1]
                path = paths[-1]
        except FileNotFoundError:
            open(os.path.dirname(sys.argv[0]) + '\\notepad.log', 'wt').close()
            path = input('请输入操作的文件: ')
            with open(os.path.dirname(sys.argv[0]) + '\\notepad.log', 'at')as fo:
                fo.write('\n' + path)
        except IndexError:
            path = ''
    return path


def read_file(file,encoding):
    nums = 186672
    print('\n')
    with open(file.strip(), 'rt', encoding=encoding) as fo:
        read = fo.read()
        if len(read) > nums:
            fo.seek(0)
            for i in range(len(read) // nums + 1):
                print(f'\r{fo.read(nums)}')
                input(colorama.Fore.GREEN + '----More----')
                print(colorama.Fore.WHITE)
        else:
            print(read)


def math():
    while True:
        try:
            print('\r\n')
            try:
                a = input('''选择操作----------------------------------------------------------------
请选择操作:
0. 退出工具
1. 累加计算
2. 累乘计算
3. 判断质数
>>> ''')
                a = int(a)
            except ValueError:
                if a == '':
                    while True:
                        a = input('>>> ')
                        try:
                            a = int(a)
                        except ValueError:
                            pass
                        else:
                            break
                else:
                    print(colorama.Fore.RED + '输入错误!')
                    continue
            match a:
                case 0:
                    print("退出程序! ")
                    break
                case 1:
                    bg, ed = input('请输入起始数值,用空格分开: ').split(' ', 1)
                    try:
                        bg, ed = eval(bg), eval(ed)
                    except ValueError:
                        print(colorama.Fore.RED + '输入的不是数字! ')
                    else:
                        print('计算结果: {}'.format(sum([i for i in range(bg, ed + 1)])))
                case 2:
                    bg, ed = input('请输入起始数值,用空格分开: ').split(' ', 1)
                    try:
                        bg, ed = eval(bg), eval(ed)
                    except ValueError:
                        print(colorama.Fore.RED + '输入的不是数字! ' + colorama.Fore.WHITE)
                    else:
                        x = 1
                        for i in range(bg, ed + 1):
                            x *= i
                        print('计算结果: {}'.format(x))
                case 3:
                    try:
                        num = eval(input('请输入要判断的数字: '))
                    except ValueError:
                        print(colorama.Fore.RED + '输入的不是数字! ' + colorama.Fore.WHITE)
                    else:
                        if num % 1 == 0:
                            if num != 2:
                                for i in range(2, int(pow(num, 0.5)) + 1):
                                    if num % i == 0:
                                        print('是质数')
                                        break
                                else:
                                    print('不是质数')
                            else:
                                print('不是质数')
                        else:
                            print(colorama.Fore.RED + '输入的不是整数! ' + colorama.Fore.WHITE)
                case x:
                    print(colorama.Fore.RED + '输入错误! ' + colorama.Fore.WHITE)
        except KeyboardInterrupt:
            print("\n退出程序! ")
            break


colorama.init(True)
os.system('title 记事本')
strings = []
print('欢迎使用记事本!')
path = get_path()
help_info = '''帮助:
产品名 | 记事本
版本号 | 4.0.0
许可证 | Copyright (C) 2023
生产商 | 个人
更新日志:
2022.12.3 开始写第一行代码
2022.12.4 记事本初代完成
2022.12.6 增加切换文件
2023.7.23 增加上次打开文件
2023.7.24 修复重大Bug
2023.7.25 增加cmd
2023.7.26 增加数学工具
'''
print('当前操作的路径为: {}\n当前操作的文件为: {}'.format(os.path.dirname(sys.argv[0]), path))
while True:
    try:
        print('\r')
        try:
            a = input('''选择操作----------------------------------------------------------------
请选择操作:
0. 退出程序
1. 写入文件
2. 追加写入
3. 读取文件
4. 切换文件
5. 保存文件
6. 追加保存
7. 另存文件
8. 使用终端
9. 新建文件
10.更改操作路径
11.数学工具
12.获取帮助
>>> ''')
            a = int(a)
        except ValueError:
            if a == '':
                while True:
                    a = input('>>> ')
                    try:
                        a = int(a)
                    except ValueError:
                        pass
                    else:
                        break
            else:
                print(colorama.Fore.RED + '输入错误!')
                continue
        match a:
            case 0:
                break
            case 1:
                strings = get_text(
                    '请输入写入的内容 (换行)Ctrl+C退出\n写入文件----------------------------------------------------------------', 1)
            case 2:
                strings = strings.extend(get_text(
                    '请输入写入的内容 (换行)Ctrl+C退出\n写入文件----------------------------------------------------------------', len(strings) + 1))
            case 3:
                read(path)
            case 4:
                ex_path = input('请输入操作的文件: ')
                if ex_path != '':
                    path = ex_path
                print('当前操作的文件为: {}'.format(path))
                with open(os.path.dirname(sys.argv[0]) + '\\notepad.log', 'at')as fo:
                    fo.write('\n' + path)
            case 5:
                if input('这个操作将覆盖文件原有内容,是否继续(y/n)?').lower() == 'y':
                    try:
                        with open(path, 'wt') as fo:
                            for i in strings:
                                fo.write(i + '\n')
                        print('保存成功')
                    except Exception as ex:
                        print(colorama.Fore.RED + '保存失败: {}'.format(ex))
                else:
                    print('用户取消了保存')
            case 6:
                with open(path, 'at') as fo:
                    for i in strings:
                        fo.write(i + '\n')
            case 7:
                path = input('请输入操作的文件: ')
                print('当前操作的文件为: {}'.format(path))
                with open(path, 'wt') as fo:
                    for i in strings:
                        fo.write(i + '\n')
            case 8:
                print('若要新建线程,请使用start命令\ncmd----------------------------------------------------------------')
                exit_code = subprocess.call('powershell')
                print('\n----------------------------------------------------------------\n')
                if exit_code == 0:
                    print('进程已结束,退出代码为{}'.format(exit_code))
                else:
                    print(colorama.Fore.RED + '进程已结束,退出代码为{}'.format(exit_code))
            case 9:
                file = input('新建文件----------------------------------------------------------------\n请输入你要新建的文件: ')
                try:
                    open(file, 'wt').close()
                except Exception as ex:
                    print(colorama.Fore.RED + '新建失败!')
            case 10:
                path_ = input('请输入要更改的操作路径: ')
                if os.path.isdir(path_):
                    os.chdir(path_)
                    print('操作路径更改成功')
                else:
                    print('路径不存在')
            case 11:
                math()
            case 12:
                print(colorama.Fore.GREEN + help_info + colorama.Fore.WHITE)
            case x:
                print(colorama.Fore.RED + '输入错误!' + colorama.Fore.WHITE)
    except KeyboardInterrupt:
        break
print('\n退出程序!')
os.system('pause')
sys.exit(0)

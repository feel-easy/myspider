
import subprocess

class ShellException(Exception): # 自定义shell异常类
    def __init__(self, code, stdout='', stderr=''):
        self.code = code
        self.stdout = stdout
        self.stderr = stderr
    def __str__(self):
        return 'exit code %d - %s' % (self.code, self.stderr)

def run_command(command):
    # 执行一个命令 并等待它执行完毕
    proc = subprocess.Popen(command.split(' '),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    proc.wait()

    # 从shell中获取标准输出和标准异常
    stdout, stderr = proc.communicate()

    # 如果shell返回一个不是0的退出信号，就抛出一个异常
    if proc.returncode != 0:
        raise ShellException(proc.returncode, stdout, stderr)
    return stdout # 返回shell的标准输出

# run_command('rm bucunzaidefile')
"""注意：在win10下抛出'FileNotFoundError: [WinError 2] 系统找不到指定的文件。'
在linux下可以抛出24行的异常信息"""


class AcceptableErrorCodes():
    def __init__(self, *error_codes):
        self.error_codes = error_codes
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            return True
        if not issubclass(exc_type, ShellException):
            return False
        return exc_val.code in self.error_codes

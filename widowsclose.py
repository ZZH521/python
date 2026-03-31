import os
import time
import threading
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

# 关机任务函数
def shutdown_timer(seconds):
    #time.sleep(seconds)
    # 执行系统关机命令
    os.system(f"shutdown /s /t {seconds}")

# 开始定时关机
def start_shutdown():
    try:
        # 获取输入的分钟数并转为秒
        minutes = int(entry.get())
        if minutes <= 0:
            messagebox.showerror("错误", "请输入大于0的数字！")
            return
        
        seconds = minutes * 60
        # 显示提示
        var.set(f"已设置：{minutes} 分钟后自动关机")
        # 启动后台线程（不卡住界面）
        thread = threading.Thread(target=shutdown_timer, args=(seconds,))
        thread.daemon = True
        thread.start()
        
    except ValueError:
        messagebox.showerror("错误", "请输入有效数字！")

# 取消关机
def cancel_shutdown():
    os.system("shutdown /a")
    var.set("已取消自动关机！")

def on_closing():
    if messagebox.askokcancel("退出", "确定要退出吗？"):
        cancel_shutdown()  # 退出前取消定时关机
        window.destroy()

# ------------------- GUI界面 -------------------
window = Tk()
window.title("Windows 定时关机工具")
window.geometry("400x180")  # 窗口大小
window.resizable(False, False)

# 提示文字
Label(window, text="请输入定时关机时间（分钟）：", font=("微软雅黑", 12)).pack(pady=10)

# 输入框
entry = Entry(window, font=("微软雅黑", 12), width=10)
entry.pack(pady=5)

# 状态显示
var = StringVar()
var.set("状态：等待设置")
Label(window, textvariable=var, font=("微软雅黑", 11), fg="blue").pack(pady=5)

# 按钮
Button(window, text="开始定时关机", font=("微软雅黑", 11), command=start_shutdown, bg="#4CAF50", fg="white").pack(pady=3)
Button(window, text="取消关机", font=("微软雅黑", 11), command=cancel_shutdown, bg="#f44336", fg="white").pack(pady=3)
# 绑定窗口关闭事件
window.protocol("WM_DELETE_WINDOW", on_closing)
# 运行窗口
window.mainloop()
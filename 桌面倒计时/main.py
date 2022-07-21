import time
import tkinter as tk
from threading import Thread


def get_time(handle):
    while True:
        s = handle.endtime - int(time.time())
        days = int(s / 86400)
        hours = int((s % 86400) / 3600)
        mins = int((s % 3600) / 60)
        handle.LabelDays.config(text=f'{days} 天')
        handle.LabelHours.config(text=f'{hours} 时')
        handle.LabelMins.config(text=f'{mins} 分')
        handle.LabelS.config(text=f'共计 {format(s, ",")} 秒')
        time.sleep(1)


class APP():
    def __init__(self):
        with open('config', 'r', encoding='utf8') as f:
            self.Target = f.readline().strip()
            self.endtime = eval(f.readline().strip())
        self.window = tk.Tk()
        self.window.geometry('405x270+1128+290')
        self.set_Line()
        self.set_text()
        self.set_layout()
        self.set_others()

    def set_Line(self):
        self.CanvasBg = tk.Canvas(self.window, bg='#f9aea8', width=405, height=270)
        self.CanvasBg.place(x=0, y=0)
        self.CanvasBg.create_line(0, 73, 405, 73, fill='white')
        self.CanvasBg.create_line(0, 200, 405, 200, fill='white')

    def set_text(self):
        self.LabelTitle = tk.Label(self.window, text=f'距离 {self.Target} 还有', bg='#f9aea8', fg='white', font=('方正青铜体简体', 17))
        self.LabelDays = tk.Label(self.window, text='00 天', bg='#f9aea8', fg='white', font=('方正青铜体简体', 17))
        self.LabelHours = tk.Label(self.window, text='00 时', bg='#f9aea8', fg='white', font=('方正青铜体简体', 17))
        self.LabelMins = tk.Label(self.window, text='00 分', bg='#f9aea8', fg='white', font=('方正青铜体简体', 17))
        self.LabelS = tk.Label(self.window, text='共计 000,000 秒', bg='#f9aea8', fg='white', font=('方正青铜体简体', 17))

    def set_layout(self):
        tk.Label(self.window, bg='#f9aea8').pack(expand='yes')
        self.LabelTitle.pack(expand='yes')
        self.LabelDays.pack(expand='yes')
        self.LabelHours.pack(expand='yes')
        self.LabelMins.pack(expand='yes')
        self.LabelS.pack(expand='yes')
        tk.Label(self.window, bg='#f9aea8').pack()

    def set_others(self):
        self.window.resizable(0, 0)
        self.window.overrideredirect(True)
        self.LabelTitle.bind("<Button-1>", self.updata_window)
        Thread(target=get_time, args=(self,)).start()

    def updata_window(self, event):
        self.UpdataWindow = tk.Toplevel()
        self.UpdataWindow['bg'] = '#f6ccb4'
        self.UpdataWindow.title('修  改')
        self.UpdataWindow.geometry('240x140')

        self.EntryTarget = tk.Entry(self.UpdataWindow)
        self.EntryEndtime = tk.Entry(self.UpdataWindow)

        tk.Label(self.UpdataWindow, bg='#f6ccb4', text='目  标').grid(row=1, column=1, pady=10, padx=5)
        self.EntryTarget.grid(row=1, column=2)
        tk.Label(self.UpdataWindow, bg='#f6ccb4', text='时间截').grid(row=2, column=1, pady=10, padx=5)
        self.EntryEndtime.grid(row=2, column=2)
        tk.Button(self.UpdataWindow, bg='#f9aea8', fg='white', width='19', text='修改', command=self.updata).grid(row=3, column=2)

    def updata(self):
        if self.EntryEndtime.get():
            self.Target = self.EntryTarget.get()
            self.endtime = eval(self.EntryEndtime.get())
            self.LabelTitle.config(text=f'距离 {self.Target} 还有')
            self.UpdataWindow.destroy()
            with open('config', 'w', encoding='utf8') as f:
                f.write(f'{self.Target}\n{self.endtime}')


if __name__ == '__main__':
    myapp = APP()
    myapp.window.mainloop()

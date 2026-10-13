import tkinter as tk, random as r, time, platform as p
#下面文字内容可以自行修改
messages = [
    "就算你不见了，我也会一直找，一直找", "你是我心中至景，此生挚爱", "小姐姐怎么不说话了", "姐姐，别着急拒绝嘛", "姐姐，你夸我一句就这么难吗",
    "律师姐姐～", "姐姐，你脸红咯", "我错了还不行嘛，姐姐", "我这里永远是你的退路", "我问你，你对我，到底有没有一点真心",
    "我永远都不会放开你", "不要说那些我不爱听的话", "我才是姐姐最重要的宝贝", "有人抢走了我的心，我要画下她的样子，让所有人都知道她的罪行",
    "我会给你超越世间一切总和的幸福", "所以再抱紧我一点吧", "这是我们之间的约定吗", "所以，我们逃吧", "既然姐姐已经做出承诺，就不能再后悔",
    "你还没有回答我的问题呢", "你会一直陪着我吗", "我就想找你不可以吗", "姐姐，今天辛苦你了", "我当然相信姐姐的能力啦",
    "所以你要拒绝我吗", "你终于发现了我的好了", "怎么样，有没有更喜欢我呀", "把目光都集中在我身上", "你还会继续陪着我吗",
    "时间还有很多，你可别偷偷溜走哦", "我肯定要一辈子都缠着姐姐的", "蹦蹦～，我就出现啦", "亲爱的，你答应了？一辈子不许反悔",
    "现在我的眼睛里全部都是你", "姐姐", "我最最最喜欢你了", "你想与我在一起吗",
    "不愿意也没机会了", "我永远都不会放开你", "该怎么办呢姐姐", "姐姐，我真的好舍不得你",
    "我这一辈子都栽在姐姐手里了", "唉，只是缠一辈子啊", "所以姐姐，你可能要包容一辈子这样贪心的我咯", "姐姐，你绝对不能跟我分手，我绝对不同意"
]
#颜色也可以自行修改，搜RGB色号
morandi_colors = [
    "#8A2BE2", "#7851A9", "#9A9AD9", "#DEC9DE", "#7851A9",
    "#9966CC", "#DEAAD3", "#C9A0DC", "#A885C3", "#CFBCE2"
]

root = tk.Tk()
root.withdraw()

for _ in range(99):
    w = tk.Toplevel()
    W, H = w.winfo_screenwidth(), w.winfo_screenheight()
    a, b = r.randint(200, 400), r.randint(80, 150)
    w.title("亲爱的")
    w.geometry(f"{a}x{b}+{r.randrange(W-a)}+{r.randrange(H-b)}")
    f = {"Darwin": "STXingkai", "Windows": "行楷"}.get(p.system(), "WenQuanYi Zen Hei")
    tk.Label(w, text=r.choice(messages), bg=r.choice(morandi_colors), fg="black",
             font=(f, max(20, min(30, min(a, b) // 20))), wraplength=a - 20,
             justify="center").pack(fill="both", expand=True)
    w.after(r.randint(10000, 30000), w.destroy)
    w.update()
    time.sleep(.1)

root.mainloop()

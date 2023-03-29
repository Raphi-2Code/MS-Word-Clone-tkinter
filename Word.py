from tkhtmlview import *
import markdown, os
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
import tkinter.messagebox as mb
import tkinterweb
root=tk.Tk()
root.title("Word - Untitled")
html="Write here..."
images=[]
def save():
    file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                             filetypes=[('Text documents', '*.txt')])
    try:
        f = open(file, 'x', encoding='utf-8')
        f.write(thtml.get(1.0,"end"))
        f.close()
        d=open((str(file).rstrip(".txt")+".img_files"),'x')
        d.write(f"{images}")
        d.close()
    except:
        f = open(file, 'w', encoding='utf-8')
        f.write(thtml.get(1.0,"end"))
        f.close()
        d=open((str(file).rstrip(".txt")+".img_files"),'w')
        d.write(f"{images}")
        d.close()
    root.title("Word - "+os.path.basename(file))
def openFile():
    global images, html
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('Text documents', '*.txt')])
    root.title("Word - "+os.path.basename(file))
    thtml.delete(1.0, "end")
    f = open(file, 'r', encoding='utf-8')
    images=eval(open((str(file).rstrip(".txt")+".img_files"),'r').read())
    html=f.read()
    idX=0
    i=0
    gg=list(html)
    print(images)
    k=0
    for x in html:
        if x=="�":
            if idX+1>len(images)-1:
                gg[i]=" "
                print("s")
            else:
                k+=1
                image=images[abs(2-idX if k!=1 else idX+1)]
                gg[i]=image+str("�")
                idX+=1
            if len(images)==1:
                image=images[0]
                gg[i]=image+str("�")
                idX+=1
        i+=1
    html="".join(gg)
    html=html.replace("\n",markdown.markdown(f"![]('')"))
    html=html.replace(" ","  ")
    renderImages()
    thtml.set_html(html)
    renderImages()
    f.close()
menu=tk.Menu(root,tearoff=0)
entry = tk.Entry(root)
entry.pack()
button=None
packed=False
menu.add_command(label="Save",command=save)
menu.add_command(label="Open",command=openFile)
menu.add_command(label="Research",command=lambda :exec("""
if packed==False:
    frame.pack(fill="both", expand=True)
    packed=True
a = entry.get()
frame.load_website(f'{a}')

"""))
menu.add_command(label="Settings",command=lambda: mb.showinfo("","-Max Images: 2\n-Bold Text?: Yes\nDeveloper:Raphi-2Code"))
root.config(menu=menu)

frame = tkinterweb.HtmlFrame(root)
def addImage():
    global html
    try:
        file=markdown.markdown(f"![]({fd.askopenfilename(initialdir = '/',title = 'Please open image:',filetypes=(('all files','*.*'),('image files',('*.png','*.jpg','*.jpeg','*.jfif','*.gif','.bmp'))))})")
        thtml.set_html(html + file+"�")
        html+="�"
        images.append(file)
        renderImages()
    except:
        mb.showinfo("","Too much images! 🙉")
def font():
    change_font_input=sd.askstring('Word','Enter text:')
    my_list=list(change_font_input)
    for i in range(len(my_list)):
        if my_list[i]=='a':
            my_list[i]='𝐚'
        if my_list[i]=='b':
            my_list[i]='𝐛'
        if my_list[i]=='c':
            my_list[i]='𝐜'
        if my_list[i]=='d':
            my_list[i]='𝐝'
        if my_list[i]=='e':
            my_list[i]='𝐞'
        if my_list[i]=='f':
            my_list[i]='𝐟'
        if my_list[i]=='g':
            my_list[i]='𝐠'
        if my_list[i]=='h':
            my_list[i]='𝐡'
        if my_list[i]=='i':
            my_list[i]='𝐢'
        if my_list[i]=='j':
            my_list[i]='𝐣'
        if my_list[i]=='k':
            my_list[i]='𝐤'
        if my_list[i]=='l':
            my_list[i]='𝐥'
        if my_list[i]=='m':
            my_list[i]='𝐦'
        if my_list[i]=='n':
            my_list[i]='𝐧'
        if my_list[i]=='o':
            my_list[i]='𝐨'
        if my_list[i]=='p':
            my_list[i]='𝐩'
        if my_list[i]=='q':
            my_list[i]='𝐪'
        if my_list[i]=='r':
            my_list[i]='𝐫'
        if my_list[i]=='s':
            my_list[i]='𝐬'
        if my_list[i]=='t':
            my_list[i]='𝐭'
        if my_list[i]=='u':
            my_list[i]='𝐮'
        if my_list[i]=='v':
            my_list[i]='𝐯'
        if my_list[i]=='w':
            my_list[i]='𝐰'
        if my_list[i]=='x':
            my_list[i]='𝐱'
        if my_list[i]=='y':
            my_list[i]='𝐲'
        if my_list[i]=='z':
            my_list[i]='𝐳'
        if my_list[i]=='A':
            my_list[i]='𝐀'
        if my_list[i]=='B':
            my_list[i]='𝐁'
        if my_list[i]=='C':
            my_list[i]='𝐂'
        if my_list[i]=='D':
            my_list[i]='𝐃'
        if my_list[i]=='E':
            my_list[i]='𝐄'
        if my_list[i]=='F':
            my_list[i]='𝐅'
        if my_list[i]=='G':
            my_list[i]='𝐆'
        if my_list[i]=='H':
            my_list[i]='𝐇'
        if my_list[i]=='I':
            my_list[i]='𝐈'
        if my_list[i]=='J':
            my_list[i]='𝐉'
        if my_list[i]=='K':
            my_list[i]='𝐊'
        if my_list[i]=='L':
            my_list[i]='𝐋'
        if my_list[i]=='M':
            my_list[i]='𝐌'
        if my_list[i]=='N':
            my_list[i]='𝐍'
        if my_list[i]=='O':
            my_list[i]='𝐎'
        if my_list[i]=='P':
            my_list[i]='𝐏'
        if my_list[i]=='Q':
            my_list[i]='𝐐'
        if my_list[i]=='R':
            my_list[i]='𝐑'
        if my_list[i]=='S':
            my_list[i]='𝐒'
        if my_list[i]=='T':
            my_list[i]='𝐓'
        if my_list[i]=='U':
            my_list[i]='𝐔'
        if my_list[i]=='V':
            my_list[i]='𝐕'
        if my_list[i]=='W':
            my_list[i]='𝐖'
        if my_list[i]=='X':
            my_list[i]='𝐗'
        if my_list[i]=='Y':
            my_list[i]='𝐘'
        if my_list[i]=='Z':
            my_list[i]='𝐙'
        if my_list[i]=='1':
            my_list[i]='𝟏'
        if my_list[i]=='2':
            my_list[i]='𝟐'
        if my_list[i]=='3':
            my_list[i]='𝟑'
        if my_list[i]=='4':
            my_list[i]='𝟒'
        if my_list[i]=='5':
            my_list[i]='𝟓'
        if my_list[i]=='6':
            my_list[i]='𝟔'
        if my_list[i]=='7':
            my_list[i]='𝟕'
        if my_list[i]=='8':
            my_list[i]='𝟖'
        if my_list[i]=='9':
            my_list[i]='𝟗'
        if my_list[i]=='0':
            my_list[i]='𝟎'
    thtml.insert(thtml.index("insert"),"".join(map(str,my_list)))
tk.Button(master=root,text="Add Image",command=addImage).pack()
tk.Button(master=root,text="Add Bold Text",command=font).pack()
thtml=HTMLScrolledText(master=root)
thtml.set_html(html)
thtml.pack()
def renderImages():
    global html
    i=0
    ic=0
    for char in html:
        ic+=1
        if char=="�":
            i+=1
            df=list(html)
            df[ic-1]=images[i-1]+str("�")
            html="".join(df)
def pp(key):
    global html
    html = thtml.get(1.0, "end")
    insert = thtml.index("insert")
    insert = insert.replace(".", "\n")
    insertlist = insert.splitlines()
    if not insertlist[1] == "0":
        insertlist[1] = str(int(insertlist[1]) - 1)
    insertlist[0] += "."
    insert = "".join(insertlist)
    if key.keysym=="BackSpace":
        if thtml.get(insert,thtml.index("insert"))=="�":
            thtml.set_html(html.rstrip().rstrip())
        print(insert,thtml.index("insert"))
    html=html.replace("\n",markdown.markdown(f"![]('')"))
    html=html.replace(" ","  ")
    renderImages()
thtml.bind("<Key>",pp)
root.mainloop()

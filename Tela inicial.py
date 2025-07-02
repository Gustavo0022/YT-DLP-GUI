from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
from SalvarVideo import SalvarVideo
from SalvarAudio import SalvarAudio
import subprocess


def pastaSalvamento():
    global local 
    local = filedialog.askdirectory(title="Selecione a pasta para salvar")
    
    caixaLocal.delete(0,END)
    caixaLocal.insert(0,local)

def habilitarOpcoes():
    formato480.config(state = NORMAL)
    formato720.config(state=NORMAL)
    #formato72060.config(state=NORMAL)
    formato1080.config(state=NORMAL)
    #formato108060.config(state=NORMAL)
def desabilitarOpcoes():
    formato480.config(state=DISABLED)
    formato720.config(state=DISABLED)
    #formato72060.config(state=DISABLED)
    formato1080.config(state=DISABLED)
    #formato108060.config(state=DISABLED)
    videoRadio.set

def baixar():

    if formatoEscolhido.get() == 1:
        erro = SalvarVideo(link.get(),local, qualidadeVideo.get())
        subprocess.Popen(r'explorer /select,' + local)
    elif formatoEscolhido.get() == 2:
        erro = SalvarAudio(link.get(),local)
        subprocess.Popen(r'explorer /select,' + local)



root = ThemedTk(theme="adapta")



root.title("Youtube Downloader")
#root.geometry("600x200")

layout = ttk.Frame(root, padding= "12 12 12 12")
layout.grid(column=0, row=0, sticky=(N,W,E,S))

ttk.Label(layout, text="Insira o link do vídeo").grid(column= 0, row= 0,columnspan=3)

#Caixa de texto para inserir o link

link = StringVar()
caixaLink = ttk.Entry(layout,width=40,textvariable= link )
caixaLink.grid(column=0, row=1, sticky=(N,W,E,S),columnspan=3)

#Caixa de texto para salvamento e botão de diálogo de pasta

ttk.Label(layout, text="Insira local onde deseja salvar").grid(column= 0, row= 2,columnspan=3)

localTexto = StringVar()
caixaLocal = ttk.Entry(layout, width = 30,textvariable=localTexto)
caixaLocal.grid(column=0, row=3, columnspan=2)

botao = ttk.Button(layout,text="Procurar...",width=8, command=pastaSalvamento)
botao.grid(column=2,row=3)

#Botões de seleção de vídeo ou áudio

formatoEscolhido = IntVar(None,2)
qualidadeVideo = IntVar(None,5)

formatoLabel = ttk.Label(layout, text="Formato:").grid(column=0,row=4)
videoRadio = ttk.Radiobutton(layout,text="Vídeo",variable=formatoEscolhido,value=1,command=habilitarOpcoes)
videoRadio.grid(column=1,row=4)
audioRadio = ttk.Radiobutton(layout,text="Áudio",variable=formatoEscolhido, value=2,command=desabilitarOpcoes)
audioRadio.grid(column=2,row=4)

# Coluna com formatos de vídeo


formato480 = ttk.Radiobutton(layout,text="MP4 480p", variable=qualidadeVideo, value= 1, state=DISABLED)
formato480.grid(column=4, row=1,sticky="EW")
formato720 = ttk.Radiobutton(layout,text="MP4 720p", variable=qualidadeVideo, value= 2, state=DISABLED)
formato720.grid(column=4, row=2,sticky="EW")
#formato72060 = ttk.Radiobutton(layout,text="MP4 720p60", variable=qualidadeVideo, value= 3, state=DISABLED)
#formato72060.grid(column=4, row=3,sticky="EW")
formato1080 = ttk.Radiobutton(layout,text="MP4 1080p", variable=qualidadeVideo, value= 4, state=DISABLED)
formato1080.grid(column=4, row=4,sticky="EW")
#formato108060 = ttk.Radiobutton(layout,text="MP4 1080p60", variable=qualidadeVideo, value= 5, state=DISABLED)
#formato108060.grid(column=4, row=5,sticky="EW")

#Botão baixar

botaoBaixar = ttk.Button(layout,text="Baixar", command=baixar)

botaoBaixar.grid(column=0,row=5,columnspan=3,rowspan=2,sticky="NWSE")

root.mainloop()
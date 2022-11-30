#importar tkinter:
from tkinter import *
# importing mudule to be able to deal with images
from PIL import ImageTk , Image
# importando mesagebox:
from tkinter import messagebox
import os 

#os.path.join("imagens", "logo.ico") concatena partes do caminho no formato do SO usado ( cada vírgula, seria as \\)

#root : a janela principal do programa
root = Tk()

#root.title() dá um título pro programa
root.title("Find me if you can" )

#ícone do jogo
root.iconbitmap(os.path.join("imagens", "logo.ico"))

#imagens:
#inicial:
img_inicial = ImageTk.PhotoImage(Image.open("imagens\\tela_inicial.jpg"))
#mapa: 
mapa_img = ImageTk.PhotoImage(Image.open("imagens\\mapa.jpg"))
#fases:
Fase_0 = ImageTk.PhotoImage(Image.open("imagens\\fases\\leminski.jpg"))
Fase_1 = ImageTk.PhotoImage(Image.open("imagens\\fases\\fase_1.jpg"))
Fase_2 = ImageTk.PhotoImage(Image.open("imagens\\fases\\fase_2.jpg"))
Fase_3 = ImageTk.PhotoImage(Image.open("imagens\\fases\\fase_3.jpg"))
Fase_4 = ImageTk.PhotoImage(Image.open("imagens\\fases\\fase_4.jpg"))
Fase_5 = ImageTk.PhotoImage(Image.open("imagens\\fases\\fase_5.jpg"))

#listas:
#lista das fases:
fases = [
    Fase_0,
    Fase_1,
    Fase_2,
    Fase_3,
    Fase_4,
    Fase_5
]

#lista das respostas:
respostas = [
    "leminski",
    "r1",
    "r2",
    "r3",
    "r4",
    "r5",
]

# lista das coordenadas:
coordenadas = [
    "00000",
    "11111",
    "22222",
    "33333",
    "44444",
    "55555",

]
# label janela principal
jan1_label = Label(image = img_inicial)
jan1_label.grid(row = 0, column=0 , rowspan = 3, columnspan = 3)

#label para os botões da janela principal
widget_label = Label() 

# criando variável x:


#start button função:
def start():
    global jan1_label
    global start_button
    global mapa_button
    global resposta_entry
    global x
    #deletando a imagem inicial:
    jan1_label.grid_forget()
    #jan1_label recebe a próxima imagem (Fase 1):
    jan1_label = Label(root, image= fases[0])
    jan1_label.grid( row = 1, column=0,  columnspan=3, )
    # x vai para 0
    x = 0
    # start button é deletado da tela: 
    start_button.destroy()
    
    #colocando botões da tela principal das fases:
    mapa_button.grid( row = 2, column =2)
    resposta_entry.grid(row = 0, column=1)
    resposta_button.grid(row = 0, column = 2 )
    x = IntVar(0)

   
# open map função:
def open_map():
    global mapa_img
    global coordenada_entry
    global coordenada_button
    global mapa_wind
    #creating a new window:
    mapa_wind = Toplevel()

    # label pro mapa:
    mapa_label = Label(mapa_wind,image= mapa_img )

    mapa_wind.title("Mapinha")
    mapa_wind.iconbitmap("imagens\\logo.ico")

    #criando widgets da tela do mapa:
    #botão testar coordenada:
    coordenada_button = Button(mapa_wind, text = "Give it a try", command = tentar_coordenada)
    coordenada_entry = Entry(mapa_wind, width = 50)
    #putting things inside the mapa_wind:
    mapa_label.grid(row =0, column =0, columnspan = 3)
    coordenada_button.grid(row=1, column = 2)
    coordenada_entry.grid(row=1, column = 1)

# botão de resposta função:
def tentar_resposta():
    global resposta_entry
    global respostas
    global x
    global coordenadas

    if resposta_entry.get() == respostas[x]:
        messagebox.showinfo("Coordenate =", str(coordenadas[x+1]))
    if resposta_entry.get() != respostas[x]:
        messagebox.showerror("Ooops", "Nop, that's not the answer")

# botão de coordenada função:
def tentar_coordenada():
    global coordenada_entry
    global respostas
    global x
    global coordenadas
    global correspondencia
    global prox_fase
    global mapa_wind

    correspondencia = False
    for a in range (len(coordenadas)):
        if coordenada_entry.get() == coordenadas[a]:
            x = a
            messagebox.showinfo("Congrats!", "right way!")
            correspondencia = True
            #função próxima fase é ativada 
            prox_fase()
            mapa_wind.destroy()
            break
            
    
    if correspondencia == False:
        messagebox.showerror("Ooops", "Wrong coodenate")
    
def prox_fase():
    global x
    global jan1_label

    #deletando a imagem da fase anterior:
    jan1_label.grid_forget()
    #jan1_label recebe a próxima imagem (Fase 1):
    jan1_label = Label(root, image= fases[x])
    jan1_label.grid( row = 1, column=0,  columnspan=3, )




# coisinhas da tela inicial:   
#start button:
start_button = Button(root, text= "RU readdy? Start Here", command = start)
start_button.grid(row = 2, column = 1)

# coisinhas da tela de mapa ( pr poder citar depois):
# coordenada entry:




# coisinhas da tela de fases:
# botão abrir mapa
mapa_button = Button(root, text= "Open Map", command = open_map )

#botão testar resposta:
resposta_button = Button(root, text = "Give it a try", command= tentar_resposta )

# resposta entry:
resposta_entry = Entry(root, width = 50)



#criate a loop that keeps the screen showing
root.mainloop()
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funções:
    def limparTela(self):
        self.entryCodigo.delete(0, END)
        self.entryNome.delete(0, END)
        self.entryTelefone.delete(0, END)
        self.entryCidade.delete(0, END)

    def conectarDB(self):
        self.conect = sqlite3.connect('Clientes.db')
        self.cursor = self.conect.cursor()
        print('Conectando ao banco de dados')
    
    def desconectarDB(self):
        self.conect.close()
        print('Desconectando o Banco de Dados')
    
    def montarTabelas(self):
        self.conectarDB()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(64) NOT NULL, 
                telefone INTEGER(20),
                cidade CHAR(64)        
            );
        """)
        self.conect.commit()
        print('Banco de dados criado')
        self.desconectarDB()

    def novoCliente(self):
        self.codigo = self.entryCodigo.get()
        self.nome = self.entryNome.get()
        self.telefone = self.entryTelefone.get()
        self.cidade = self.entryCidade.get()
        
        self.conectarDB()
        self.cursor.execute("""
            INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES(?, ?, ?)
        """, (self.nome, self.telefone, self.cidade))
        self.conect.commit()
        self.desconectarDB()
        self.selectLista()
        self.limparTela()
    
    def selectLista(self):
        self.listaClientes.delete(*self.listaClientes.get_children())
        self.conectarDB()
        lista = self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC
        """)
        for i in lista:
            self.listaClientes.insert('', END, values= i)
        self.desconectarDB()




class Aplicação(Funções):
    def __init__(self):
        self.root = root
        self.tela()
        self.framesDaTela()
        self.widgetsFrame1()
        self.listaFram2()
        self.montarTabelas()
        self.selectLista()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background = "#1e3743")
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height = 700)
        self.root.minsize(width = 600, height = 400)

    def framesDaTela(self):
        self.frame1 = Frame(self.root, bd = 4, bg = "#dfe3ee", highlightbackground = "#759fe6", highlightthickness = 3)
        self.frame1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        self.frame2 = Frame(self.root, bd = 4, bg = "#dfe3ee", highlightbackground = "#759fe6", highlightthickness = 3)
        self.frame2.place(relx = 0.02, rely = 0.50, relwidth = 0.96, relheight = 0.46)

    def widgetsFrame1(self):
        self.labelCodigo = Label(self.frame1, text = "Código", bg = "#dfe3ee", fg= '#107db2')
        self.labelCodigo.place(relx = 0.05, rely = 0.03, relwidth= 0.08)
        self.entryCodigo = Entry(self.frame1)
        self.entryCodigo.place(relx = 0.05, rely = 0.15, relwidth= 0.08)


        self.labelNome = Label(self.frame1, text = "Nome", bg = "#dfe3ee", fg= '#107db2')
        self.labelNome.place(relx = 0.05, rely = 0.36, relwidth= 0.08)
        self.entryNome = Entry(self.frame1)
        self.entryNome.place(relx = 0.05, rely = 0.48, relwidth= 0.75)


        self.labelTelefone = Label(self.frame1, text = "Telefone", bg = "#dfe3ee", fg= '#107db2')
        self.labelTelefone.place(relx = 0.05, rely = 0.6, relwidth= 0.08)
        self.entryTelefone = Entry(self.frame1)
        self.entryTelefone.place(relx = 0.05, rely = 0.72, relwidth= 0.25)

        
        self.labelCidade = Label(self.frame1, text = "Cidade", bg = "#dfe3ee", fg= '#107db2')
        self.labelCidade.place(relx = 0.4, rely = 0.6, relwidth= 0.08)
        self.entryCidade = Entry(self.frame1)
        self.entryCidade.place(relx = 0.4, rely = 0.72, relwidth= 0.4)

        self.limpar = Button(self.frame1, text = 'Limpar', bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.limparTela)
        self.limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        self.buscar = Button(self.frame1, text = 'Buscar', bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.buscar.place(relx = 0.32, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        
        self.novo = Button(self.frame1, text = 'Novo', bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.novoCliente)
        self.novo.place(relx = 0.56, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        self.alterar = Button(self.frame1, text = 'Alterar', bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.alterar.place(relx = 0.68, rely = 0.1, relwidth = 0.1, relheight = 0.15)

        self.apagar = Button(self.frame1, text = 'Apagar', bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'))
        self.apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)

    def listaFram2(self):
        self.listaClientes = ttk.Treeview(self.frame2, height= 3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaClientes.heading('#0', text= '')
        self.listaClientes.heading('#1', text= 'Código')
        self.listaClientes.heading('#2', text= 'Nome')
        self.listaClientes.heading('#3', text= 'Telefone')
        self.listaClientes.heading('#4', text= 'Cidade')
        
        self.listaClientes.column('#0', width= 1)
        self.listaClientes.column('#1', width= 50)
        self.listaClientes.column('#2', width= 200)
        self.listaClientes.column('#3', width= 125)
        self.listaClientes.column('#4', width= 125)
                
        self.listaClientes.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

        self.scroolLista = Scrollbar(self.frame2, orient= 'vertical')
        self.listaClientes.configure(yscroll= self.scroolLista.set)
        self.scroolLista.place(relx= 0.96, rely= 0.1, relwidth= 0.04, relheight= 0.85)

    




Aplicação()
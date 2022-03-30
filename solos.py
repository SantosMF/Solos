#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 15:22:02 2021
@author: marcio marciofs600@gmail.com
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
class Interface:
    def __init__(self):
        self.window = tk.Tk() # Cria a janela principal
        self.window.title('Solos-1.0')
        self.window.minsize(1000,600) #tamanho mínimo
        self.window.maxsize(1000,600) #tamanho máximo = mínimo = fixo
        self.menubar = tk.Menu(self.window) # barra de menu
        self.arquivo = tk.Menu(self.menubar, tearoff=False)
        self.arquivo.add_command(label='Ajuda', command=self.Ajuda)
        self.arquivo.add_command(label='Sobre',command=self.Sobre)
        self.arquivo.add_command(label='Fechar',command=self.Fechar)
        self.menubar.add_cascade(label = 'Arquivos', menu=self.arquivo)
        self.window.config(menu = self.menubar)
##-----------grupo entrada de dados-------------------------------------------
        self.dados = tk.LabelFrame(self.window, text='dados da análise química')
        self.dados.place(x=5, y=10, width=410, height=480)
#--------------------------coluna 1-------------------------------------------
        self.labelph = tk.Label(self.dados, text='pH')
        self.labelph.place(x=10, y=10)
        self.enterPH = tk.Entry(self.dados, bd=1, justify='right')
        self.enterPH.place(x=10, y=30, width=140,height=31)
        self.enterPH.insert(0,'0')
        self.labelp = tk.Label(self.dados, text='P  (mg/dm³)')
        self.labelp.place(x=10, y=65)
        self.enterP = tk.Entry(self.dados, bd=1, justify='right')
        self.enterP.place(x=10, y=85, width=140,height=31)
        self.enterP.insert(0,'0')
        self.labelK = tk.Label(self.dados, text='K  (mg/dm³)')
        self.labelK.place(x=10, y=120)
        self.enterK = tk.Entry(self.dados, bd=1, justify='right')
        self.enterK.place(x=10, y=140, width=140,height=31)
        self.enterK.insert(0,'0')
        self.labelCa = tk.Label(self.dados, text='Ca  (cmolc/dm³)')
        self.labelCa.place(x=10, y=175)
        self.enterCa = tk.Entry(self.dados, bd=1, justify='right')
        self.enterCa.place(x=10, y=195, width=140,height=31)
        self.enterCa.insert(0,'0')
        self.labelMg = tk.Label(self.dados, text='Mg  (cmolc/dm³)')
        self.labelMg.place(x=10, y=230)
        self.enterMg = tk.Entry(self.dados, bd=1, justify='right')
        self.enterMg.place(x=10, y=250, width=140,height=31)
        self.enterMg.insert(0,'0')
        self.labelAl = tk.Label(self.dados, text='Al  (cmolc/dm³)')
        self.labelAl.place(x=10, y=285)
        self.enterAl = tk.Entry(self.dados, bd=1, justify='right')
        self.enterAl.place(x=10, y=305, width=140,height=31)
        self.enterAl.insert(0,'0')
        self.labelAlH = tk.Label(self.dados, text='H + Al  (cmolc/dm³)')
        self.labelAlH.place(x=10, y=340)
        self.enterAlH = tk.Entry(self.dados, bd=1, justify='right')
        self.enterAlH.place(x=10, y=360, width=140,height=31)
        self.enterAlH.insert(0,'0')
        self.labelMO = tk.Label(self.dados, text='M.O  (dag/kg)')
        self.labelMO.place(x=10, y=395)
        self.enterMO = tk.Entry(self.dados, bd=1, justify='right')
        self.enterMO.place(x=10, y=415, width=140,height=31)
        self.enterMO.insert(0,'0')
##-----------------------------coluna 2---------------------------------------
        self.labelPrem = tk.Label(self.dados, text='P-rem  (mg/dm³)')
        self.labelPrem.place(x=205, y=10)
        self.enterPrem = tk.Entry(self.dados, bd=1, justify='right')
        self.enterPrem.place(x=205, y=30, width=140,height=31)
        self.enterPrem.insert(0,'0')
        self.labelS = tk.Label(self.dados, text='S  (mg/dm³)')
        self.labelS.place(x=205, y=65)
        self.enterS = tk.Entry(self.dados, bd=1, justify='right')
        self.enterS.place(x=205, y=85, width=140,height=31)
        self.enterS.insert(0,'0')
        self.labelMn = tk.Label(self.dados,  text='Mn  (mg/dm³)')
        self.labelMn.place(x=205, y=120)
        self.enterMn = tk.Entry(self.dados,bg='#BDBDBD',bd=1, justify='right')
        self.enterMn.place(x=205, y=140, width=140,height=31)
        self.enterMn.insert(0,'0')
        self.labelCu = tk.Label(self.dados, text='Cu  (mg/dm³)')
        self.labelCu.place(x=205, y=175)
        self.enterCu = tk.Entry(self.dados,bg='#BDBDBD',bd=1, justify='right')
        self.enterCu.place(x=205, y=195, width=140,height=31)
        self.enterCu.insert(0,'0')
        self.labelFe = tk.Label(self.dados, text='Fe  (mg/dm³)')
        self.labelFe.place(x=205, y=230)
        self.enterFe = tk.Entry(self.dados,bg='#BDBDBD',bd=1, justify='right')
        self.enterFe.place(x=205, y=250, width=140,height=31)
        self.enterFe.insert(0,'0')
        self.labelZn = tk.Label(self.dados, text='Zn  (mg/dm³)')
        self.labelZn.place(x=205, y=285)
        self.enterZn = tk.Entry(self.dados,bg='#BDBDBD',bd=1, justify='right')
        self.enterZn.place(x=205, y=305, width=140,height=31)
        self.enterZn.insert(0,'0')
        self.labelB = tk.Label(self.dados, text='B  (mg/dm³)')
        self.labelB.place(x=205, y=340)
        self.enterB = tk.Entry(self.dados,bg='#BDBDBD',bd=1, justify='right')
        self.enterB.place(x=205, y=360, width=140,height=31)
        self.enterB.insert(0,'0')

        self.labelcombo = tk.Label(self.dados, text='Tipo de Cultura')
        self.labelcombo.place(x=205, y=400)
        self.valores = ['Hortaliças', 'Culturas perenes', 'Culturas florestais']
        self.combobox = ttk.Combobox(self.window, values=self.valores)
        self.combobox.place(x=215,y=450, width=140, height=30)
        self.combobox.insert(0,'Culturas perenes')
        self.combobox.configure(state='readonly')

        self.prnt = tk.Label(self.window, text='P.R.N.T')
        self.prnt.place(x=10, y=515)
        self.prnt = tk.Entry(self.window,bg='#BDBDBD',bd=1, justify='right')
        self.prnt.place(x=80, y=515, width=70,height=31)
        self.prnt.insert(0,'85')
##-----------combobox calcular e salvar---------------------------------------
        self.Framebtn = tk.LabelFrame(self.window, text='Cálculos')
        self.Framebtn.place(x=205, y=490, width=210,height=60)
        self.btnCalcular = tk.Button(self.Framebtn, text="Calcular", command = self.Calcular)
        self.btnCalcular.place(x=5, y=2, width=80, height=30)
        self.btnSalvar = tk.Button(self.Framebtn, text="Salvar", command = self.Salvar)
        self.btnSalvar.place(x=120, y=2, width=80, height=30)
#------------caixa de texto---------------------------------------------------
        self.frameTxt = tk.Frame(self.window, background="white")
        self.frameTxt.place(x=420, y=1, width=579,height=560)
        self.Texto = tk.Text(self.frameTxt,bd=2)
        self.Texto.place(x=0, y=0, width=579,height=560)
#-------------Exibir janela em looping--------------------------------------
        tk.mainloop()
#---------------------- final da interface -----------------------------------
#----------------------- início dos métodos ----------------------------------
    def Ajuda(self):
        msg = """Para mais informações veja: <insert to link>.
        """
        tk.messagebox.showinfo(title="Ajuda", message=msg)
    def Sobre(self):
        msgs = """Programa para interpretar análise de solos """
        tk.messagebox.showinfo(title="Solos-1.0", message=msgs)
    def Fechar(self):
        self.window.destroy()

    def Calcular(self):
        self.Texto.delete('1.0', 'end')
        try:
            resultado = self.Resolver()
            self.Texto.insert('1.0',resultado)
        except ZeroDivisionError:
            msg = "K, Ca, Mg, Al e H + Al não podem ser nulos."
            tk.messagebox.showerror(title="Erro", message=msg)

    def Resolver(self):
        cultura = self.combobox.get()
        pH = float(self.enterPH.get())
        P  = float(self.enterP.get())
        K = float(self.enterK.get())*0.002558 ##converte mg/dm^3 para cmolc/dm^3
        Ca = float(self.enterCa.get())
        Mg = float(self.enterMg.get())
        Al = float(self.enterAl.get())
        HAl = float(self.enterAlH.get())
        MO = float(self.enterMO.get())
       # C_O = float(self.enterPH.get())
        Zn = float(self.enterZn.get())
        Fe = float(self.enterFe.get())
        Mn = float(self.enterMn.get())
        Cu = float(self.enterCu.get())
        B = float(self.enterB.get())
        S = float(self.enterS.get())
        R = float(self.enterPrem.get())
        PRNT = float(self.prnt.get())
        SB =  K + Ca + Mg
        t = SB + Al
        T = SB + HAl
#----------------------pH-----------------------------------------------------
        if pH <= 5.4: ph = "elevada"
        elif pH > 5.4 and pH <= 6: ph = "média"
        elif pH > 6: ph = "baixa"
#------------------------Alumínio---------------------------------------------
        if Al <= 0.5: al = "baixo"
        elif Al > 0.5 and Al <= 1: al = "médio"
        elif Al > 1: al = "alto"
#---------------------Alumínio + hidrogênio-----------------------------------
        if HAl <= 2.5: hal = "baixo"
        elif HAl > 2.5 and HAl <= 5: hal = "médio"
        elif HAl > 5: hal = "alto"
#-------------ctc efetiva-----------------------------------------------------
        if t <= 2: ctc = "Baixa"
        elif t > 2 and t <= 4: ctc = "Média"
        elif t > 4: ctc = "Alta"
#-------------ctc total-------------------------------------------------------
        if T <= 5: CTC = "Baixa"
        elif T > 5 and T <= 15: CTC = "Média"
        elif T > 15: CTC = "Alta"
#-------------saturação por base----------------------------------------------
        V = (SB/T)*100
        if V <= 50: sb = "Baixa"
        elif V > 50 and V <= 70: sb = "Média"
        elif V > 70: sb = "Alta"
#-------------saturação por Alumíno-------------------------------------------
        m = (Al/t)*100
        if m <= 50: sAl = "Baixa"
        elif m > 50 and m <= 70: sAl = "Média"
        elif m > 70: sAl = "Alta"
#--------------fósforo remanescente-------------------------------------------
        if R <= 20: textura = "Argilosa"
        elif R > 20 and R <= 40: textura = "Média"
        elif R > 40: textura = "Arenosa"
##-----------------------macronutrientes--------------------------------------
#----------------------------Fósforo------------------------------------------
        if P <= 5: p = "Baixo"
        elif P > 5 and P <= 10: p = "Médio"
        elif P > 10: p = "Alto"
#-----------------------------Cálcio------------------------------------------
        if Ca <= 1.5: ca = "Baixo"
        elif Ca > 1.5 and Ca <= 3.5: ca = "Médio"
        elif Ca > 3.5: ca = "Alto"
#--------------------------Magnésio-------------------------------------------
        if Mg <= 0.5: mg = "Baixo"
        elif Mg > 0.5 and Mg <= 1.0: mg = "Médio"
        elif Mg > 1.0: mg = "Alto"
#----------------------------Potássio-----------------------------------------
        if K <= 0.077: k = "Baixo"
        elif K > 0.077 and K <= 0.154: k = "Médio"
        elif K > 0.154: k = "Alto"
#---------------------------Enxofre-------------------------------------------
        if S <= 5: s = "Baixo"
        elif S > 5 and S <= 10: s = "Médio"
        elif S > 10: s = "Alto"
#------------------------Matéria Orgânica-------------------------------------
        if MO <= 1.5: mo = "Baixa"
        elif MO > 1.5 and MO <= 3: mo = "Média"
        elif MO > 3: mo = "Alta"
##-----------------------micronutrientes--------------------------------------
#------------------------------Boro-------------------------------------------
        if B <= 0.35: mb = "Baixo"
        elif B > 0.35 and B <= 0.90: mb = "Médio"
        elif B > 0.90: mb = "Alto"
#-----------------------------Zinco-------------------------------------------
        if Zn <= 1: zn = "Baixo"
        elif Zn > 1 and Zn <= 2.20: zn = "Médio"
        elif Zn > 2.20: zn = "Alto"
#-----------------------------Cobre-------------------------------------------
        if Cu <= 0.8: cu = "Baixo"
        elif Cu > 0.8 and Cu <= 1.80: cu = "Médio"
        elif Cu > 1.80: cu = "Alto"
#-----------------------------Ferro-------------------------------------------
        if Fe <= 20: fe = "Baixo"
        elif Fe > 20 and Fe <= 45: fe = "Médio"
        elif Fe > 45: fe = "Alto"
#----------------------------Manganês-----------------------------------------
        if Mn <= 5: mn = "Baixo"
        elif Mn > 5 and Mn <= 12: mn = "Médio"
        elif Mn > 12: mn = "Alto"
#-------------------relação Ca:Mg---------------------------------------------
        CaMg = Ca/Mg
        if CaMg <= 3: camg = "baixa"
        elif CaMg > 3 and CaMg <= 4: camg = "boa"
        elif CaMg > 4: camg = "alta"
#-------------------necessidade de calagem------------------------------------
        if cultura == 'Hortaliças':
            V2 = 80
            NC = ((V2 - V)*T)/PRNT
        elif cultura == 'Culturas perenes':
            V2 = 70
            NC = ((V2 - V)*T)/PRNT
        elif cultura == 'Culturas florestais':
            V2 = 60
            NC = ((V2 - V)*T)/PRNT
        if camg == "baixa": recomendado = 'Calcítico'
        elif camg == 'boa': recomendado = 'Magnesiano'
        elif camg == 'alta': recomendado = 'Dolomítico'
        if NC < 0: NC = 0
        if NC == 0: recomendado = ''
#-----------------------------------------------------------------------------
        resposta = f'''# Interpretação de Análise química
----------------------------------------------------------------------
# Elemento                  :       valor           :   classificação
----------------------------------------------------------------------
acidez [pH (H2O)]           =     {pH:^10.3f}        :     {ph}
acidez potencial  [H+Al]    =     {HAl:^10.3f}        :     {hal}
Alumínio  (Al^3+)           =     {Al:^10.3f}        :     {al}
Textura do solo (P-rem)     =     {R:^10.3f}        :     {textura}
Saturação por base      %   =     {V:^10.3f}        :     {sb}
Saturação por Alumínio  %   =     {m:^10.3f}        :     {sAl}
CTC total                   =     {T:^10.3f}        :     {CTC}
CTC efetiva                 =     {t:^10.3f}        :     {ctc}
Proporção Ca:Mg             =     {CaMg:^10.3f}        :     {camg}
----------------------------------------------------------------------
Fósforo  (mg/dm³)           =     {P:^10.3f}        :     {p}
Potássio (cmolc/dm³)        =     {K:^10.3f}        :     {k}
Cálcio   (cmolc/dm³)        =     {Ca:^10.3f}        :     {ca}
Magnésio (cmolc/dm³)        =     {Mg:^10.3f}        :     {mg}
Enxofre                     =     {S:^10.3f}        :     {s}
Matéria orgânica            =     {MO:^10.3f}        :     {mo}
----------------------------------------------------------------------
Boro                        =     {B:^10.3f}        :     {mb}
Zinco                       =     {Zn:^10.3f}        :     {zn}
Cobre                       =     {Cu:^10.3f}        :     {cu}
Ferro                       =     {Fe:^10.3f}        :     {fe}
Manganês                    =     {Mn:^10.3f}        :     {mn}
-----------------------------------------------------------------------
Necessidade de Calagem (PRNT:{PRNT:.0f}%)  = {NC:^5.3f} t/ha
Tipo de Calcário recomendado:      = {recomendado}
'''
        return resposta
    def Salvar(self):
        try:
            filetypes = ( ('dados', '*.dat'),   ('todos', '*.*'))
            name=fd.asksaveasfile(mode='w',defaultextension=".dat",filetypes= filetypes)
            texto=str(self.Texto.get('1.0','end'))
            name.write(texto)
            name.close
            msg = "Dados salvos!"
            tk.messagebox.showinfo(title="Info", message=msg)
        except AttributeError:
            pass

##-----------------Finaliza a gui---------------------------------------------
Interface() ## executa a interface

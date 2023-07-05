import ply.yacc as yacc
import os
import codecs
import re
from lexer_entrega import tokens
from sys import stdin
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import filedialog

def p_INICIO(p):
    '''INICIO : doctype HTML'''
    print("Regla INICIO")
    
def p_HTML(p):
    ''' HTML : html_apertura atributo_lang leng HEAD html_cierre s_mayor'''
    print("Regla HTML") 
    
def p_HEAD(p):
    '''HEAD : head_apertura GLOBAL_ATT s_mayor METACHAR TITLE head_cierre s_mayor BODY
            | head_apertura s_mayor METACHAR TITLE head_cierre s_mayor BODY
            | head_apertura GLOBAL_ATT s_mayor METACHAR head_cierre s_mayor BODY
            | head_apertura s_mayor METACHAR head_cierre s_mayor BODY '''
    print("Regla HEAD")


def p_METACHAR(p):
    '''METACHAR : meta GLOBAL_ATT atributo_charset utf s_mayor
                | meta atributo_charset utf s_mayor
                | meta GLOBAL_ATT atributo_charset utf s_mayor META_NAME
                | meta atributo_charset utf s_mayor META_NAME'''
    print("Regla METACHAR")
   
def p_META_NAME(p):
    '''META_NAME : meta GLOBAL_ATT atributo_name CONTENT_AT atributo_content CONTENT_AT s_mayor META_NAME
                | meta GLOBAL_ATT atributo_name CONTENT_AT atributo_content CONTENT_AT s_mayor
                | meta atributo_name CONTENT_AT atributo_content CONTENT_AT s_mayor META_NAME
                | meta atributo_name CONTENT_AT atributo_content CONTENT_AT s_mayor '''
    print("Regla META_NAME")

def p_CONTENT_AT(p):
    '''CONTENT_AT : content_at
                 | num_enatributo '''
    print("Regla CONTENT_AT")


def p_TITLE(p):
    '''TITLE : title_apertura GLOBAL_ATT s_mayor texto title_cierre s_mayor
             | title_apertura s_mayor texto title_cierre s_mayor'''
    print("Regla TITLE")

def p_BODY(p):
    '''BODY : body_apertura GLOBAL_ATT s_mayor E body_cierre s_mayor
            | body_apertura s_mayor E body_cierre s_mayor'''
    print("Regla BODY")

    
def p_E(p):
    '''E : P
         | H1
         | H2
         | H3
         | H4
         | H5
         | H6
         | STRONG
         | EM
         | BR
         | MARK
         | UL
         | OL
         | TABLE
         | SECTION
         | IMG
         | DIV
         | A
         | HR '''
    print("Regla E")



def p_SECTION(p):
    '''SECTION : section_apertura GLOBAL_ATT s_mayor E section_cierre s_mayor
               | section_apertura GLOBAL_ATT s_mayor E section_cierre s_mayor E
               | section_apertura s_mayor E section_cierre s_mayor E
               | section_apertura s_mayor E section_cierre s_mayor '''
    print("Regla SECTION")
    
  
def p_GLOBAL_ATT(p):
    '''GLOBAL_ATT : 
                  | atributo_class CONTENT_AT
                  | id_att CONTENT_AT
                  | atributo_class CONTENT_AT id_att CONTENT_AT '''
    print("Regla GLOBAL-ATT")


def p_DIV(p):
    '''DIV : div_apertura GLOBAL_ATT s_mayor E div_cierre s_mayor
           | div_apertura GLOBAL_ATT s_mayor E div_cierre s_mayor E
           | div_apertura s_mayor E div_cierre s_mayor
           | div_apertura s_mayor E div_cierre s_mayor E '''
    print("Regla DIV")


def p_P(p):
    '''P : p_apertura GLOBAL_ATT s_mayor TEXTOENTRE p_cierre s_mayor
         | p_apertura GLOBAL_ATT s_mayor TEXTOENTRE p_cierre s_mayor E
         | p_apertura s_mayor TEXTOENTRE p_cierre s_mayor
         | p_apertura s_mayor TEXTOENTRE p_cierre s_mayor E
         | p_apertura GLOBAL_ATT s_mayor p_cierre s_mayor
         | p_apertura GLOBAL_ATT s_mayor p_cierre s_mayor E
         | p_apertura s_mayor p_cierre s_mayor
         | p_apertura s_mayor p_cierre s_mayor E'''
    print("Regla P")


def p_TEXTOENTRE(p):
    '''TEXTOENTRE : texto E
                  | E texto
                  | texto
                  | E
                  | texto E TEXTOENTRE
                  | E texto TEXTOENTRE'''
    print("Regla TEXTOENTRE")


    
def p_H1(p):
    '''H1 : h1_apertura GLOBAL_ATT s_mayor texto h1_cierre s_mayor
          | h1_apertura GLOBAL_ATT s_mayor texto h1_cierre s_mayor E
          | h1_apertura s_mayor texto h1_cierre s_mayor
          | h1_apertura s_mayor texto h1_cierre s_mayor E
          | h1_apertura GLOBAL_ATT s_mayor h1_cierre s_mayor
          | h1_apertura GLOBAL_ATT s_mayor h1_cierre s_mayor E
          | h1_apertura s_mayor h1_cierre s_mayor
          | h1_apertura s_mayor h1_cierre s_mayor E'''
    print("Regla H1")

def p_H2(p):
    '''H2 : h2_apertura GLOBAL_ATT s_mayor texto h2_cierre s_mayor
          | h2_apertura GLOBAL_ATT s_mayor texto h2_cierre s_mayor E
          | h2_apertura s_mayor texto h2_cierre s_mayor
          | h2_apertura s_mayor texto h2_cierre s_mayor E
          | h2_apertura GLOBAL_ATT s_mayor h2_cierre s_mayor
          | h2_apertura GLOBAL_ATT s_mayor h2_cierre s_mayor E
          | h2_apertura s_mayor h2_cierre s_mayor
          | h2_apertura s_mayor h2_cierre s_mayor E'''
    print("Regla H2")


def p_H3(p):
    '''H3 : h3_apertura GLOBAL_ATT s_mayor texto h3_cierre s_mayor
          | h3_apertura GLOBAL_ATT s_mayor texto h3_cierre s_mayor E
          | h3_apertura s_mayor texto h3_cierre s_mayor
          | h3_apertura s_mayor texto h3_cierre s_mayor E
          | h3_apertura GLOBAL_ATT s_mayor h3_cierre s_mayor
          | h1_apertura GLOBAL_ATT s_mayor h3_cierre s_mayor E
          | h3_apertura s_mayor h3_cierre s_mayor
          | h3_apertura s_mayor h3_cierre s_mayor E'''
    print("Regla H3")
    
def p_H4(p):
    '''H4 : h4_apertura GLOBAL_ATT s_mayor texto h4_cierre s_mayor
          | h4_apertura GLOBAL_ATT s_mayor texto h4_cierre s_mayor E
          | h4_apertura s_mayor texto h4_cierre s_mayor
          | h4_apertura s_mayor texto h4_cierre s_mayor E
          | h4_apertura GLOBAL_ATT s_mayor h4_cierre s_mayor
          | h4_apertura GLOBAL_ATT s_mayor h4_cierre s_mayor E
          | h4_apertura s_mayor h4_cierre s_mayor
          | h4_apertura s_mayor h4_cierre s_mayor E'''
    print("Regla H4")

def p_H5(p):
    '''H5 : h5_apertura GLOBAL_ATT s_mayor texto h5_cierre s_mayor
          | h5_apertura GLOBAL_ATT s_mayor texto h5_cierre s_mayor E
          | h5_apertura s_mayor texto h5_cierre s_mayor
          | h5_apertura s_mayor texto h5_cierre s_mayor E
          | h5_apertura GLOBAL_ATT s_mayor h5_cierre s_mayor
          | h5_apertura GLOBAL_ATT s_mayor h5_cierre s_mayor E
          | h5_apertura s_mayor h5_cierre s_mayor
          | h5_apertura s_mayor h5_cierre s_mayor E'''
    print("Regla H5")

def p_H6(p):
    '''H6 : h6_apertura GLOBAL_ATT s_mayor texto h6_cierre s_mayor
          | h6_apertura GLOBAL_ATT s_mayor texto h6_cierre s_mayor E
          | h6_apertura s_mayor texto h6_cierre s_mayor
          | h6_apertura s_mayor texto h6_cierre s_mayor E
          | h6_apertura GLOBAL_ATT s_mayor h6_cierre s_mayor
          | h6_apertura GLOBAL_ATT s_mayor h6_cierre s_mayor E
          | h6_apertura s_mayor h6_cierre s_mayor
          | h6_apertura s_mayor h6_cierre s_mayor E'''
    print("Regla H6")


def p_STRONG(p):
    '''STRONG : strong_apertura GLOBAL_ATT s_mayor TEXTOENTRE strong_cierre s_mayor
              | strong_apertura GLOBAL_ATT s_mayor TEXTOENTRE strong_cierre s_mayor E
              | strong_apertura s_mayor TEXTOENTRE strong_cierre s_mayor
              | strong_apertura s_mayor TEXTOENTRE strong_cierre s_mayor E
              | strong_apertura GLOBAL_ATT s_mayor strong_cierre s_mayor
              | strong_apertura GLOBAL_ATT s_mayor strong_cierre s_mayor E
              | strong_apertura s_mayor strong_cierre s_mayor
              | strong_apertura s_mayor strong_cierre s_mayor E'''
    print("Regla STRONG")
    

def p_EM(p):
    '''EM : em_apertura GLOBAL_ATT s_mayor TEXTOENTRE em_cierre s_mayor
          | em_apertura GLOBAL_ATT s_mayor TEXTOENTRE em_cierre s_mayor E
          | em_apertura s_mayor TEXTOENTRE em_cierre s_mayor
          | em_apertura s_mayor TEXTOENTRE em_cierre s_mayor E
          | em_apertura GLOBAL_ATT s_mayor em_cierre s_mayor
          | em_apertura GLOBAL_ATT s_mayor em_cierre s_mayor E
          | em_apertura s_mayor em_cierre s_mayor
          | em_apertura s_mayor em_cierre s_mayor E'''
    print("Regla EM")

    

def p_MARK(p):
    '''MARK : mark_apertura GLOBAL_ATT s_mayor TEXTOENTRE mark_cierre s_mayor
            | mark_apertura GLOBAL_ATT s_mayor TEXTOENTRE mark_cierre s_mayor E
            | mark_apertura s_mayor TEXTOENTRE mark_cierre s_mayor
            | mark_apertura s_mayor TEXTOENTRE mark_cierre s_mayor E
            | mark_apertura GLOBAL_ATT s_mayor mark_cierre s_mayor
            | mark_apertura GLOBAL_ATT s_mayor mark_cierre s_mayor E
            | mark_apertura s_mayor mark_cierre s_mayor
            | mark_apertura s_mayor mark_cierre s_mayor E'''
    print("Regla MARK")

def p_HR(p):
    '''HR : hr_tag GLOBAL_ATT s_mayor
          | hr_tag GLOBAL_ATT s_mayor E 
          | hr_tag s_mayor
          | hr_tag s_mayor E'''
    print("Regla HR")

def p_BR(p):
        '''BR : br_tag GLOBAL_ATT s_mayor
              | br_tag GLOBAL_ATT s_mayor E 
              | br_tag s_mayor
              | br_tag s_mayor E'''
        print("Regla BR")
        

def p_A(p):
    '''A : a_apertura GLOBAL_ATT A_ATT s_mayor TEXTOENTRE a_cierre s_mayor
         | a_apertura A_ATT s_mayor TEXTOENTRE a_cierre s_mayor
         | a_apertura GLOBAL_ATT A_ATT s_mayor TEXTOENTRE a_cierre s_mayor E
         | a_apertura A_ATT s_mayor TEXTOENTRE a_cierre s_mayor E 
         | a_apertura GLOBAL_ATT A_ATT s_mayor a_cierre s_mayor
         | a_apertura A_ATT s_mayor a_cierre s_mayor
         | a_apertura GLOBAL_ATT A_ATT s_mayor a_cierre s_mayor E
         | a_apertura A_ATT s_mayor a_cierre s_mayor E '''
    print("Regla A")


def p_URL(p):
    ''' URL : url
            | url_relativa
            | url_alt '''
    print("Regla URL")


def p_A_ATT(p):
    '''A_ATT : atributo_href URL TARGET
             | atributo_href URL '''
    print("Regla A_ATT")

def p_TARGET(p): 
    '''TARGET : atributo_targetblank
              | atributo_targetself
              | atributo_targetparent
              | atributo_targettop '''
    print("Regla TARGET")


def p_IMG(p):
    '''IMG : img GLOBAL_ATT IMG_ATT s_mayor
           | img IMG_ATT s_mayor
           | img GLOBAL_ATT IMG_ATT s_mayor E
           | img IMG_ATT s_mayor E '''
    print("Regla IMG")


def p_IMG_ATT(p):
    '''IMG_ATT : atributo_alt CONTENT_AT src_atributo URL atributo_width num_enatributo atributo_height num_enatributo
               | atributo_alt CONTENT_AT src_atributo URL atributo_width num_enatributo
               | atributo_alt CONTENT_AT src_atributo URL atributo_height num_enatributo
               | atributo_alt CONTENT_AT src_atributo URL
               | src_atributo URL atributo_width num_enatributo atributo_height num_enatributo
               | src_atributo URL atributo_width num_enatributo 
               | src_atributo URL atributo_height num_enatributo
               | src_atributo URL'''
    print("Regla IMG_ATT")

def p_TABLE(p):
    ''' TABLE : table_apertura GLOBAL_ATT atributo_border num_enatributo s_mayor TABLE_CONT table_cierre s_mayor
              | table_apertura atributo_border num_enatributo s_mayor TABLE_CONT table_cierre s_mayor
              | table_apertura s_mayor TABLE_CONT table_cierre s_mayor
              | table_apertura GLOBAL_ATT atributo_border num_enatributo s_mayor TABLE_CONT table_cierre s_mayor E
              | table_apertura atributo_border num_enatributo s_mayor TABLE_CONT table_cierre s_mayor E
              | table_apertura s_mayor TABLE_CONT table_cierre s_mayor E  '''
    print("Regla TABLE")

def p_TABLE_CONT(p):
    ''' TABLE_CONT : THEAD
                   | TR '''
    print("Regla TABLE-CONT")
    
def p_THEAD(p):
    ''' THEAD : thead_apertura GLOBAL_ATT s_mayor TR thead_cierre s_mayor TBODY
              | thead_apertura s_mayor TR thead_cierre s_mayor TBODY
              | thead_apertura GLOBAL_ATT s_mayor TR thead_cierre s_mayor TFOOT
              | thead_apertura s_mayor TR thead_cierre s_mayor TFOOT'''
    print("Regla THEAD")

def p_TR(p):
    ''' TR : tr_apertura GLOBAL_ATT s_mayor TR_CONT tr_cierre s_mayor
           | tr_apertura GLOBAL_ATT s_mayor TR_CONT tr_cierre s_mayor TR
           | tr_apertura s_mayor TR_CONT tr_cierre s_mayor
           | tr_apertura s_mayor TR_CONT tr_cierre s_mayor TR '''
    print("Regla TR")

def p_TR_CONT(p):
    ''' TR_CONT : TH
                | TD
                | TH TR_CONT
                | TD TR_CONT '''
    print("Regla TR_CONT")


def p_TD(p):
    ''' TD : td_apertura GLOBAL_ATT s_mayor TEXTOENTRE td_cierre s_mayor
           | td_apertura s_mayor TEXTOENTRE td_cierre s_mayor
           | td_apertura GLOBAL_ATT s_mayor td_cierre s_mayor
           | td_apertura s_mayor td_cierre s_mayor '''
    print("Regla TD")


def p_TH(p):
    ''' TH : th_apertura GLOBAL_ATT s_mayor TEXTOENTRE th_cierre s_mayor
           | th_apertura s_mayor TEXTOENTRE th_cierre s_mayor
           | th_apertura GLOBAL_ATT s_mayor th_cierre s_mayor
           | th_apertura s_mayor th_cierre s_mayor'''
    print("Regla TH")
    
def p_TBODY(p):
    ''' TBODY : tbody_apertura GLOBAL_ATT s_mayor TR  tbody_cierre s_mayor TFOOT
              | tbody_apertura s_mayor TR  tbody_cierre s_mayor TFOOT
              | tbody_apertura GLOBAL_ATT s_mayor TR  tbody_cierre s_mayor
              | tbody_apertura s_mayor TR  tbody_cierre s_mayor '''
    print("Regla TBODY")

def p_TFOOT(p):
    ''' TFOOT : tfoot_apertura GLOBAL_ATT s_mayor TR tfoot_cierre s_mayor
              | tfoot_apertura TR tfoot_cierre s_mayor '''
    print("Regla TFOOT")

def p_UL(p):
    ''' UL : ul_apertura GLOBAL_ATT s_mayor LI ul_cierre s_mayor
           | ul_apertura GLOBAL_ATT s_mayor LI ul_cierre s_mayor E
           | ul_apertura s_mayor LI ul_cierre s_mayor
           | ul_apertura s_mayor LI ul_cierre s_mayor E '''
    print("Regla UL")


def p_LI(p):
    ''' LI : li_apertura GLOBAL_ATT s_mayor TEXTOENTRE li_cierre s_mayor
           | li_apertura GLOBAL_ATT LI_ATT s_mayor TEXTOENTRE li_cierre s_mayor
           | li_apertura s_mayor TEXTOENTRE li_cierre s_mayor
           | li_apertura LI_ATT s_mayor TEXTOENTRE li_cierre s_mayor
           | li_apertura GLOBAL_ATT s_mayor TEXTOENTRE li_cierre s_mayor LI
           | li_apertura GLOBAL_ATT LI_ATT s_mayor TEXTOENTRE li_cierre s_mayor LI
           | li_apertura s_mayor TEXTOENTRE li_cierre s_mayor LI
           | li_apertura LI_ATT s_mayor TEXTOENTRE li_cierre s_mayor LI 
           | li_apertura GLOBAL_ATT s_mayor li_cierre s_mayor
           | li_apertura GLOBAL_ATT LI_ATT s_mayor li_cierre s_mayor
           | li_apertura s_mayor li_cierre s_mayor
           | li_apertura LI_ATT s_mayor li_cierre s_mayor
           | li_apertura GLOBAL_ATT s_mayor li_cierre s_mayor LI
           | li_apertura GLOBAL_ATT s_mayor LI_ATT li_cierre s_mayor LI
           | li_apertura s_mayor li_cierre s_mayor LI
           | li_apertura LI_ATT s_mayor li_cierre s_mayor LI '''
    print("Regla LI")

def p_LI_ATT(p):
    ''' LI_ATT : atributo_value num_enatributo  '''
    print("Regla LI-ATT")

def p_OL(p):
    ''' OL : ol_apertura GLOBAL_ATT TYPE LI ol_cierre s_mayor
           | ol_apertura GLOBAL_ATT s_mayor LI ol_cierre s_mayor
           | ol_apertura TYPE s_mayor LI ol_cierre s_mayor
           | ol_apertura s_mayor LI ol_cierre s_mayor
           | ol_apertura GLOBAL_ATT TYPE LI ol_cierre s_mayor E 
           | ol_apertura GLOBAL_ATT s_mayor LI ol_cierre s_mayor E 
           | ol_apertura TYPE s_mayor LI ol_cierre s_mayor E
           | ol_apertura s_mayor LI ol_cierre s_mayor E '''
    print("Regla OL")

def p_TYPE(p):
    ''' TYPE : atributo_type'''
    print("Regla TYPE")
    

def p_error(p):
    print("Error de sintaxis en linea ", p.lineno, "posición ", p.lexpos, " : ", p.value)

ventana = tkinter.Tk()
ventana.geometry("800x600")
ventana.title('Parser')

def tokens_directo(pasar):
     text20 = pasar.get('1.0', END)
     parser = yacc.yacc()
     result = parser.parse(text20)  
    
def ingresar_texto():
     cajatexto = tkinter.Text(ventana, height=25, width=100)
     cajatexto.pack(expand=True, fill=BOTH)
     boton3 = tkinter.Button(ventana, text = "Enviar", command = lambda: tokens_directo(cajatexto))
     boton3.pack()
    

boton1 = tkinter.Button(ventana, text = "Ingreso directo", command = ingresar_texto)
boton1.pack()   

def abrir_archivo():
     ventana.filename = filedialog.askopenfilename(initialdir="C:/Users/", filetypes =(("Archivo html", "*.html"),("Todos los archivos","*.*")), title = "Elija un archivo.")

     try:
         fp = codecs.open(ventana.filename, "r", "windows-1252")
         string = fp.read()
     except Exception:
         fp = codecs.open(ventana.filename, "r", "utf-8")
         string = fp.read()
     

     fp.close()
     parser = yacc.yacc()
     result = parser.parse(string)
     
            
boton2 = tkinter.Button(ventana, text = "Abrir archivo", command = abrir_archivo)
boton2.pack()


ventana.mainloop()



     



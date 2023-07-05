import ply.lex as lex
import re
import codecs
import os
import sys
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import filedialog


tokens = [
    'texto',
    'content_at',
    'url',
    'tag_format',
    'leng',
    'atributo',
    's_mayor',
    'utf',
    'atributo_type',
    'atributo_target',
    'doctype',
    'url_alt',
    'url_relativa',
    'num_enatributo',
 ]


reserved = {'<html'
            : "html_apertura", 'charset=':'charset_att', 'name=':'name_att', '<h1':'h1_apertura', '</h1':'h1_cierre', '<h2':'h2_apertura', '</h2':'h2_cierre',
               '<h3':'h3_apertura', '</h3':'h3_cierre', '<h4':'h4_apertura', '</h4>':'h4_cierre', '<h5':'h5_apertura', '</h5':'h5_cierre', '<h6':'h6_apertura', '</h6':'h6_cierre', 
            '<p': 'p_apertura','</p': 'p_cierre', '<body':'body_apertura', 'id=': 'id_att', '</body': 'body_cierre', '<title' : 'title_apertura', '</title': 'title_cierre', '<meta': 'meta', '<section' : 'section_apertura',
            '</section' : 'section_cierre', '<div' : 'div_apertura', '</div' : 'div_cierre', '<em': 'em_apertura', '</em' : 'em_cierre', '<mark':'mark_apertura', '</mark':'mark_cierre', '<hr':'hr_tag',
             '<br':'br_tag', '<strong':'strong_apertura', '</strong':'strong_cierre', '<a':'a_apertura', '</a':'a_cierre', '<li':'li_apertura', '</li':'li_cierre', '<ol':'ol_apertura', '</ol':'ol_cierre', '<ul':'ul_apertura', '</ul':'ul_cierre',
            '<img':'img', '<tbody':'tbody_apertura', '</tbody':'tbody_cierre', '<thead':'thead_apertura', '</thead':'thead_cierre', '<tfoot':'tfoot_apertura', '</tfoot':'tfoot_cierre', '<tr':'tr_apertura', '</tr':'tr_cierre', '<td':'td_apertura', '</td':'td_cierre'
            , '<th':'th_apertura', '</th':'th_cierre', 'id=':'id_att', 'class=':'class_att', 'lang=': 'lang_att', '<head': 'head_apertura', '</head':'head_cierre', '</html':'html_cierre', '<table':'table_apertura', '</table':'table_cierre',
            'class=':'atributo_class', 'lang=':'atributo_lang', 'charset=':'atributo_charset', 'name=':'atributo_name', 'href=':'atributo_href', 'target="_blank"':'atributo_targetblank', 'target="_parent"':'atributo_targetparent',
            'target="_self':'atributo_targetself', 'target="_top':'atributo_targettop', 'width=':'atributo_width', 'height=':'atributo_height', 'border=':'atributo_border', 'alt=':'atributo_alt', 'src=':'src_atributo', 'value=':'atributo_value',
            'content=':'atributo_content' }

tokens = tokens+list(reserved.values())


def t_utf(t):
     r'("|”)(UTF|utf|Utf|UTf|utF|uTF|uTf)-8("|”)[ ]*'
     t.type = reserved.get(t.value.lower(),'utf')
     return t

def t_num_enatributo(t):
     r'"[0-9]+[ ]*"'
     t.type = reserved.get(t.value.lower(),'num_enatributo')
     return t

def t_leng(t):
     r'("|”)[ ]*[a-zA-Z][a-zA-Z]("|”)[ ]*>'
     t.type = reserved.get(t.value.lower(),'leng')
     return t

def t_atributo_target(t):
     r'[ ]*[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]="_[a-zA-Z]+("|”)'
     while ' ' in t.value:
          new = t.value.replace(" ", "")
          t.value = new
     t.type = reserved.get(t.value.lower(),'atributo_target')
     return t

def t_atributo_type(t):
     r'[ ]*[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]=("|”)(a|A|i|I|1)("|”)[ ]*'
     while ' ' in t.value:
          new = t.value.replace(" ", "")
          t.value = new
     t.type = reserved.get(t.value.lower(),'atributo_type')
     return t

def t_atributo(t):
     r'([ ]*[a-zA-Z]+=)'
     while ' ' in t.value:
          new = t.value.replace(" ", "")
          t.value = new
     t.type = reserved.get(t.value.lower(),'atributo')
     #conviene comentar este if cuando se va a usar el parser y dejar solo return t
     
     if t.type == 'atributo': 
          print("Error. Atributo mal escrito: ", t.value)
     else:
          return t
        
     #return t

def t_doctype(t):
     r'<![a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][ ][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]>'
     return t


def t_tag_format(t):
     r'[ ]*<[ ]*[a-zA-Z/0-9]+[ ]*'
     while ' ' in t.value:
          new = t.value.replace(" ", "")
          t.value = new
     t.type = reserved.get(t.value.lower(),'tag_format')
     #conviene comentar este if cuando se va a usar el parser y dejar solo return t
     if t.type == 'tag_format':
          print("Error. Tag mal escrito:", t.value)
     else:
          return t
     #return t

def t_content_at(t):
     r'([ ]*("|”|")[a-zA-Z 0-9,áéíóúÁÉÍÓÚ]+("|”|")[ ]*)'
     t.type = reserved.get(t.value.lower(),'content_at')
     return t

def t_url_alt(t):
     r'[ ]*("\#|”\#|"\#)[a-zA-Z0-9 ]+("|”|")[ ]*'
     t.type = reserved.get(t.value.lower(),'url_alt')
     return t

def t_url(t):
     r'[ ]*("|”)(http://|https://|ftp://|ftps://)[a-zA-Z0-9.]+(:0-9)*[-&0-9/a-zA-Z_|.=;/?]*("|”)[ ]*'
     t.type = reserved.get(t.value.lower(),'url')
     return t

def t_url_relativa(t):
     r'[ ]*("|”)[a-zA-Z0-9/]+.[a-zA-Z]+[ ]*("|”)[ ]*'
     t.type = reserved.get(t.value.lower(),'url_relativa')
     return t

def t_texto(t):
     r'[\v\s\r\t\na-zA-Z/0-9._+áéíóú,ñÁÉÍÓÚ: "@()\'#¿?!¡:-]+'
     t.type = reserved.get(t.value.lower(),'texto')
     
     novacio = False
     cad = t.value
     [*cad]
     for p in [*cad]:
          if p != '\t' and p != '\n' and p!= '\r' and p!= ' ':
               novacio = True
        
     
     if t.value == '\n':
          pass
     else:
          if novacio == True:
               while '\n' in t.value:
                    new = t.value.replace('\n', "   ")
                    t.value = new
               while '\t' in t.value:
                    new = t.value.replace('\t', " ")
                    t.value = new
               while '\r' in t.value:
                    new = t.value.replace('\r', " ")
                    t.value = new
               return t
          else:
               pass
     

t_s_mayor = '>'

def t_error(t):
        #este print conviene comentar cuando se va a usar el parser  
	print ("caracter invalido '%s'" %t.value[0])
	t.lexer.skip(1)

#dejar comentado esto, hasta ventana.mainloop, cuando se va a ejecutar el parser. Descomentar cuando se quiere usar solo el lexer

ventana = tkinter.Tk()
ventana.geometry("800x600")
ventana.title('Lexer')

def tokens_directo(pasar):
     text20 = pasar.get('1.0', END)
     analyzer = lex.lex()
     analyzer.input(str(text20))

     while True:
          tok = analyzer.token()
          if not tok: break
          print ("Se encontro un token :", tok)
          
    
def ingresar_texto():
     cajatexto = tkinter.Text(ventana, height=25, width=100)
     cajatexto.pack(expand=True, fill=BOTH)
     boton3 = tkinter.Button(ventana, text = "Enviar", command = lambda: tokens_directo(cajatexto))
     boton3.pack()
    

boton1 = tkinter.Button(ventana, text = "Ingreso directo", command = ingresar_texto)
boton1.pack()   

def abrir_archivo():
     ventana.filename = filedialog.askopenfilename(initialdir="C:/Users/", filetypes =(("Text File", "*.html"),("All Files","*.*")), title = "Choose a file.")

     try:
          fp = codecs.open(ventana.filename, "r", "windows-1252")
          string = fp.read()
     except:
          fp = codecs.open(ventana.filename, "r", "utf-8")
          string = fp.read()

     fp.close()

     analyzer = lex.lex()
     analyzer.input(string)
     

     while True:
          tok = analyzer.token()
          if not tok: break
          print ("Se encontro un token :", tok)
       
boton2 = tkinter.Button(ventana, text = "Abrir archivo", command = abrir_archivo)
boton2.pack()


ventana.mainloop()


#esto se agrega cuando queremos usar el parser, porque estaba en lo que comentamos pero sí o sí necesitamos para que funcione el parser
#comentar cuando se quiera usar lexer, descomentar si se va a usar parser!
#analyzer = lex.lex()


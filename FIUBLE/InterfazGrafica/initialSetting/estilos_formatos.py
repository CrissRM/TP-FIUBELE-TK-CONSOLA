estilos = {
  "BACKGROUND_PRIMARY": "#000000",
  "FOREGROUND_PRIMARY": "#ededed",
  "BACKGROUND_BUTTON_REGISTRO":"#287233",
  "FOREGROUND_BUTTON_REGISTRO":"#ffffff",
  "BACKGROUND_BUTTON_REGISTRO_ACTIVE":"#1e552d",
  "BACKGROUND_BUTTON_INGRESO":"#002f68",
  "FOREGROUND_BUTTON_INGRESO":"#ffffff",
  "BACKGROUND_BUTTON_INGRESO_ACTIVE":"#002653",
  "BACKGROUND_BUTTON_VOLVER": "#d81800",
  "FOREGROUND_BUTTON_VOLVER": "#ffffff",
  "BACKGROUND_BUTTON_ENVIAR": "#0300eb",
  "FOREGROUND_BUTTON_ENVIAR": "#ffffff",
  "FONT_FAMILY":"Raleway",
  "FONT_SIZE_TITLE":20,
  "FONT_SIZE_SUBTITLE":15,
  "FONT_SIZE_TEXT":13,
  "BORDER_GROOVE":"groove"
}

def button_style(style):
  if style == "back":
    estilo = ("#d81800","#ffffff","#881800")
  elif style =="send":
    estilo = ("#0300eb","#ffffff","#03008b")
  elif style == "register":
    estilo = ("#287233","#ffffff","#1e552d")
  elif style == "signin":
    estilo = ("#002f68","#ffffff","#002653")
  return estilo

def style_label(parent,text,padx,pady,font_family,font_size,font_slant,width,anchor,background,foreground,side,mgx,mgy):
  return  {
    "root": parent,
    "text": text,
    "padding_x": padx,
    "padding_y":pady,
    "font_family": font_family,
    "font_size": font_size,
    "font_slant": font_slant,
    "width":width,
    "anchor": anchor,
    "background": background,
    "foreground":foreground,
    "side": side,
    "margin_x": mgx,
    "margin_y": mgy,
  }

def style_button(parent,text,padx,pady,font_family,font_size,font_slant,width,state,button_style,side,mgx,mgy):
  return {
    "root": parent,
    "text": text,
    "padding_x": padx,
    "padding_y":pady,
    "font_family": font_family,
    "font_size": font_size,
    "font_slant": font_slant,
    "width": width,
    "state": state,
    "button_style": button_style,
    "side": side,
    "margin_x": mgx,
    "margin_y": mgy,
  }

def style_entry(parent,padx,pady,font_family,font_size,font_slant,background,foreground,justify,show,width,side,mgx,mgy,is_password):
  return {
    "root": parent,
    "padding_x": padx,
    "padding_y": pady,
    "font_family": font_family,
    "font_size": font_size,
    "font_slant": font_slant,
    "background": background,
    "foreground": foreground,
    "justify": justify,
    "show": show,
    "width": width,
    "side": side,
    "mgx": mgx,
    "mgy": mgy,
    "is_password": is_password
  }



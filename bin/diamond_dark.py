#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Frank.Ding"

style_dict = {'DARKEST_COLOR': 'rgb(55, 55, 55)',
              'GRAY_COLOR': 'rgb(70, 70, 70)',
              'BUTTON_COLOR': 'rgb(100, 100, 100)',
              'BORDER_COLOR': 'rgb(85, 85, 85)',
              'BRIGHT_COLOR': 'rgb(110, 110, 110)',
              'LIGHT_COLOR': 'rgb(150, 150, 150)',
              'FONT_COLOR': 'rgb(200, 200, 200)',
              'BORDER_WIDTH': '0.5px',
              'BORDER_RADIUS': '3px'
              }

style = """
QMainWindow{
    background-color: GRAY_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;   
}

QPixmap{
    background-color: GRAY_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;   
}

QLineEdit{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QComboBox{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: GRAY_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QComboBox::drop-down{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: GRAY_COLOR;
    border-style: solid;
    border-width: 10px;
    border-radius: 0px;
    border-left-style: solid;
    border-color: BORDER_COLOR;
}

QTextEdit{
    color: FONT_COLOR;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QLabel{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    border-radius: BORDER_LARGE_RADIUS;
}

QListWidget{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QListWidget::item{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
}

QMenu{
    color: FONT_COLOR;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QMenu::item:selected{
    color: FONT_COLOR;
    background-color: BORDER_COLOR;
}

QMenuBar{
    color: FONT_COLOR;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QTableView{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: DARKEST_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BORDER_COLOR;
}

QTableView QTableCornerButton:section{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: BUTTON_COLOR;
    border-style: solid;
    border-color: BORDER_COLOR;
}

QHeaderView{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: BUTTON_COLOR;
    border-style: solid;
    border-width: 0;
    border-color: BORDER_COLOR;
}

QHeaderView:section{
    color: FONT_COLOR;
    font: 9pt Microsoft YaHei UI;
    background-color: BUTTON_COLOR;
    border-style: solid;
    border-width: 0;
    border-color: BORDER_COLOR;
}

QPushButton{
    color: DARKEST_COLOR;
    background-color: BUTTON_COLOR;
    border-style: solid;
    border-width: BORDER_WIDTH;
    border-radius: BORDER_RADIUS;
    border-color: BRIGHT_COLOR;
}

QPushButton:hover{
    color: FONT_COLOR;
    background-color: BRIGHT_COLOR;
}

QPushButton:pressed{
    color: FONT_COLOR;
    background-color: BUTTON_COLOR;
}

QScrollBar:horizontal{
    background: GRAY_COLOR;
    margin: 0 20.5px 0 20.5px;
}

QScrollBar::handle:horizontal{
    background: GRAY_COLOR;
    min-width: 20px;
}

QScrollBar::add-line:horizontal{
    background: GRAY_COLOR;
    width: 20px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal{
    background: GRAY_COLOR;
    width: 20px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar:vertical{
    background: GRAY_COLOR;
    margin: 20.5px 0 20.5px 0;
}

QScrollBar::handle:vertical{
    background: GRAY_COLOR;
    min-height: 20px;
}

QScrollBar::add-line:vertical{
    background: GRAY_COLOR;
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical{
    background: GRAY_COLOR;
    height: 20px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow, QScrollBar::down-arrow, QScrollBar::left-arrow, QScrollBar::right-arrow{
    width: 0px;
    height: 0px;
    background: BRIGHT_COLOR;
}

QScrollBar::add-page, QScrollBar::sub-page{
    background: BORDER_COLOR;
}

QScrollBar::handle:hover, QScrollBar::add-line:hover, QScrollBar::sub-line:hover{
    background: BRIGHT_COLOR;
}

QScrollBar::handle:pressed, QScrollBar::add-line:pressed, QScrollBar::sub-line:pressed{
    background: GRAY_COLOR;
}

"""

def get_stylesheet(text=style):
    for key in style_dict:
        text = text.replace(key, style_dict.get(key))
    return text

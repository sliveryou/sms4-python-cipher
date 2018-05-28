# -*- coding: UTF-8 -*-
__author__ = 'Sliver'

from tkinter import *
import tkinter.messagebox as mbox
from sms4 import SMS4, File


class Cipher(Frame):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.var1 = Variable()
        self.var2 = Variable()
        self.var3 = Variable()
        self.var4 = Variable()

        self.lab1 = Label(frame, text="明文：")
        self.lab1.grid(row=0, column=0, sticky=W)

        self.ent1 = Entry(frame)
        self.ent1.grid(row=0, column=1, sticky=W)

        self.lab2 = Label(frame, text="密钥：")
        self.lab2.grid(row=1, column=0, sticky=W)

        self.ent2 = Entry(frame)
        self.ent2.grid(row=1, column=1, sticky=W)

        self.lab3 = Label(frame, text="结果：")
        self.lab3.grid(row=2, column=0, sticky=W)

        self.ent3 = Entry(frame, textvariable=self.var1)
        self.ent3.grid(row=2, column=1, sticky=W)

        self.button1 = Button(frame, text="加密", command=self.encrypt, fg='orange')
        self.button1.grid(row=3, column=1)

        self.lab4 = Label(frame, text="密文：")
        self.lab4.grid(row=4, column=0, sticky=W)

        self.ent4 = Entry(frame, textvariable=self.var3)
        self.ent4.grid(row=4, column=1, sticky=W)

        self.lab5 = Label(frame, text="密钥：")
        self.lab5.grid(row=5, column=0, sticky=W)

        self.ent5 = Entry(frame, textvariable=self.var4)
        self.ent5.grid(row=5, column=1, sticky=W)

        self.lab6 = Label(frame, text="结果：")
        self.lab6.grid(row=6, column=0, sticky=W)

        self.ent6 = Entry(frame, textvariable=self.var2)
        self.ent6.grid(row=6, column=1, sticky=W)

        self.button2 = Button(frame, text="解密", command=self.decrypt, fg='orange')
        self.button2.grid(row=7, column=1)

        self.lab = Label(frame, text="")
        self.lab.grid(row=8, column=0, sticky=W)

        self.lab7 = Label(frame, text="文件：")
        self.lab7.grid(row=9, column=0, sticky=W)

        self.ent7 = Entry(frame)
        self.ent7.grid(row=9, column=1, sticky=W)

        self.lab8 = Label(frame, text="密钥：")
        self.lab8.grid(row=10, column=0, sticky=W)

        self.ent8 = Entry(frame)
        self.ent8.grid(row=10, column=1, sticky=W)

        self.button3 = Button(frame, text="加密", command=self.file_encrypt, fg='red')
        self.button3.grid(row=9, column=2)

        self.button4 = Button(frame, text="解密", command=self.file_decrypt, fg='red')
        self.button4.grid(row=10, column=2)

    def encrypt(self):
        message = self.ent1.get()
        key = self.ent2.get()
        if len(key) != 16:
            mbox.showwarning('错误','密钥须为16字节字符！')
            return
        result = SMS4(message, key)
        self.var1.set(result.ciphertext)

        self.var3.set(result.ciphertext)
        self.var4.set(key)

    def decrypt(self):
        message = self.ent4.get()
        key = self.ent5.get()
        if len(key) != 16:
            mbox.showwarning('错误','密钥须为16字节字符！')
            return
        result = SMS4(message, key)
        if result.plaintext:
            self.var2.set(result.plaintext)
        else:
            mbox.showwarning('错误', '密文缺失信息，无法解密！')

    def file_encrypt(self):
        filename = self.ent7.get()
        key = self.ent8.get()
        if len(key) != 16:
            mbox.showwarning('错误','密钥须为16字节字符！')
            return
        result = File(key)
        result.encrypt(filename)

    def file_decrypt(self):
        filename = self.ent7.get()
        key = self.ent8.get()
        if len(key) != 16:
            mbox.showwarning('错误','密钥须为16字节字符！')
            return
        result = File(key)
        result.decrypt(filename)
        

root = Tk()
root.title('SMS4')
root.geometry('400x310')
app = Cipher(root)
root.mainloop()
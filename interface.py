from tkinter import *
from tkinter import ttk


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("URL Shortener")
        self.mainframe = ttk.Frame(self.root, padding="6 6 24 24")
        self.mainframe.grid(column=0, row=0, sticky="N, W, E, S")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.url_label = ttk.Label(self.mainframe, text="Your URL: ")
        self.url_label.grid(column=0, row=0, sticky="W, E")

        self.url_entry = ttk.Entry(self.mainframe)
        self.url_entry.grid(column=1, row=0, sticky="W")

        self.convert_button = ttk.Button(self.mainframe, text="Cut!", command=self.get_url)
        self.convert_button.grid(column=2, row=0, sticky="W")

        self.output_label = ttk.Label(self.mainframe, text="Shortened URL: ")
        self.output_label.grid(column=0, row=1, sticky="EW")

        self.output_entry = ttk.Entry(self.mainframe)
        self.output_entry.grid(column=1, row=1, sticky="W")

        self.copy_button = ttk.Button(self.mainframe, text="Copy", command=self.copy_url)
        self.copy_button.grid(column=2, row=1, sticky="W")

        self.clear_button = ttk.Button(self.mainframe, text="Clear", command=self.clear, width=32)
        self.clear_button.grid(column=1, row=2, columnspan=2)

        self.root.mainloop()

    @staticmethod
    def shorten_url(url):
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url

    def get_url(self):
        url = self.url_entry.get()
        shortened_url = self.shorten_url(url)
        self.output_entry.insert(0, shortened_url)

    def copy_url(self):
        url = self.output_entry.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(url)
        self.root.update()
        self.copy_button = ttk.Button(self.mainframe, text="Copy", command=self.copy_url)

    def clear(self):
        self.output_entry.delete(0, "end")
        self.url_entry.delete(0, "end")

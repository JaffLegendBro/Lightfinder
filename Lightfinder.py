

from tkinter import Tk, simpledialog, messagebox


def read_from_file():
    with open('data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

print('Opensource, HJ - Lightfinder')
root = Tk()
root.withdraw()
the_world = {}
read_from_file()

while True:
    query_country = simpledialog.askstring('Lightfinder', 'Type your word')
    query_country = query_country.capitalize()
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Lightfinder',
                             result )
    else:
        messagebox.showinfo('Lightfinder',
                            'Sorry that word was not found, is the word spelled correctly? If not, try updating with UPDATE.bat, or if still not please write and fill in the \'New Word form\'')
         
        root.mainloop()


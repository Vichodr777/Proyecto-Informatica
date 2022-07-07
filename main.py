from kivymd.app import MDApp


lista = open("lista.txt","w")


class Myapp(MDApp):
    def build(self):
        return
    def get_data(self):
        print("Nombre: ",self.root.ids.data.text)
        lista.write(self.root.ids.data.text)

        lista.write("\n")





Myapp().run()
lista.close()
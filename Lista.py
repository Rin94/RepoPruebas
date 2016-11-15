class Lista:

    lista=[]

    def __init__(self, arreglo):
        self.lista=arreglo


    def sumarDosNumeros(self, num1,num2):
        return num1+num2

    def encontrarEnLista(self,num1):
        return 'Yes' if self.lista.count(num1)>=1 else 'No'




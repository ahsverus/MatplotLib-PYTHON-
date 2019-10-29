from datetime import datetime

from flask import Flask,render_template,request
from grafico import plotar_grafico
import csv

app = Flask(__name__)



@app.route('/plotagem', methods=["POST"])
def cadastro():
    cidade = request.form['valorx']
    combustivel = request.form['valory']
    precos_belem = []
    data_belem = []
    i = 0
    values = []
    next = ''
    y = []
    yy = []
    with open('2018-1_CA.csv', encoding='iso-8859-1') as file:
        lista = csv.reader(file, delimiter='\t')
        #next(lista)
        for linha in lista:
            li = linha[0].split("  ")
            if (li[2] == cidade):
                # print(linha)
                for coluna in range(len(li)):
                    if li[coluna] == combustivel:
                        #precos_belem.append(li[8])
                        current_data = datetime.strptime(li[6], "%d/%m/%Y")
                        print(current_data)
                        if next== "":
                            string = li[6]
                            data_belem.append(string[:5])
                            values.append(li[8])
                            next = li[6]
                            print('primiera vez')
                        elif(next==li[6]):
                            values.append(li[8])
                            print('nao é a primeira vez')
                        else:
                            print(values)
                            for number in values:
                                number = number[:1] + '.' + number[2:]
                                precos_belem.append(number)
                            print(precos_belem)
                            y = [float(i) for i in precos_belem]
                            print('eae patrao')
                            yy.append(sum(y)/len(y))
                            values.clear()
                            next = ''




    #for number in precos_belem:
     #   number = number[:1] + '.' + number[2:]
      #  yy.append(number)
    print(yy)
    #y = [float(i) for i in precos_belem]
    #x = list(dict.fromkeys(data_belem))
    print(y)
    print(data_belem)
    yy.append(4.12)
    caminho = plotar_grafico(data_belem,yy,"Evolução das vendas","Meses","Total de venda por mês")
    return render_template('resultado.html', url = caminho)


@app.route('/novo')
def novo():
    return render_template('novo.html')

app.run()

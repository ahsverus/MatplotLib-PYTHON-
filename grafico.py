import matplotlib.pyplot as plt
import io
import base64

#Método para plotar grafico
#Valoresx: lista de valores do eixo X
#Valoresy: lista de valores do eixo y
#labelplotagem: Texto do rótulo da plotagem
#labelx: Texto do rótulo do eixo X
#labely: Texto do rótulo do eixo y

def plotar_grafico(x, y, labelplotagem, labelx, labely):
    img = io.BytesIO()
    plt.plot(x, y, label=labelplotagem)
    plt.xticks(x, rotation='vertical')
    plt.subplots_adjust(bottom=0.15)
    plt.savefig(img, format='png')
    grafico_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(grafico_url)




#importação
import requests
import sys
from PyQt5.QtWidgets import QApplication , QWidget,QLabel,QPushButton,QLineEdit,QMessageBox



#limpa campos 
def limpaCampos():
    #funçao para limpar campos e posicionar o cursor no campo cpf
    caixaTextoCep.clear()
    caixaTextoLogradouro.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUf.clear()
    caixaTextoCep.setFocus()

#funçao para validar o campo cep
def validaCampos():
    
    #variavelq guarda o cep informado
    codigoCep = caixaTextoCep.text()

    if codigoCep == "":
         QMessageBox.critical(janela, "Atenção" , "Cep invalido")
    else:
         #chama outra finçao pra verificar o cep
         tratarCep(codigoCep)

def tratarCep (codigoCep):
    url = f"https://viacep.com.br/ws/{codigoCep}/json/"

    try:
        response = requests.get(url)
        
        #verifica o resultado          
        if response.status_code == 200:
            dados = response.json()

             #verifica se a chave "erro" existe e se o valor e true
            if dados.get("erro") == "true":
                    QMessageBox.critical(janela, "Atenção" , "lcep nao encontrado ")
            else:
                caixaTextoLogradouro.setText(dados.get('logradouro', ''))
                caixaTextoBairro.setText(dados.get('bairro',''))
                caixaTextoCidade.setText(dados.get('localidade',''))
                caixaTextoUf.setText(dados.get('uf','')) 
                
                QMessageBox.information(janela , "consulta de cep", "endereço encontrado")

        else:
             QMessageBox.critical(janela, "erro" , f"erro na requisiçao codigo de estatos {response.status_code}")        

    except:
           QMessageBox.critical(janela, "erro" , f"ocorreu uma exceção: {str(e)}")


#criando a aplicaçao
app = QApplication(sys.argv)
# criação da tela
janela = QWidget()
janela.setWindowTitle("Verificação de CEP")
janela.setGeometry(725, 300, 560, 420)  # largura/altura ajustadas

#    Labels 
# CEP
textoRotuloCep = QLabel("CEP", janela)
textoRotuloCep.move(40, 100)

# Logradouro
textoRotuloLogradouro = QLabel("Logradouro", janela)
textoRotuloLogradouro.move(40, 140)

# Número
textoRotuloNumero = QLabel("Número", janela)
textoRotuloNumero.move(40, 180)

# Bairro
textoRotuloBairro = QLabel("Bairro", janela)
textoRotuloBairro.move(40, 220)

# Cidade
textoRotuloCidade = QLabel("Cidade", janela)
textoRotuloCidade.move(40, 260)

# UF
textoRotuloUf = QLabel("UF", janela)
textoRotuloUf.move(40, 300)

#   Campos de texto 
# CEP
caixaTextoCep = QLineEdit(janela)
caixaTextoCep.move(160, 100)
caixaTextoCep.resize(300, 25)
caixaTextoCep.setInputMask("00000-000")

# Logradouro
caixaTextoLogradouro = QLineEdit(janela)
caixaTextoLogradouro.move(160, 140)
caixaTextoLogradouro.resize(300, 25)
caixaTextoLogradouro.setEnabled(False)

# Número
caixaTextoNumero = QLineEdit(janela)
caixaTextoNumero.move(160, 180)
caixaTextoNumero.resize(100, 25)
caixaTextoNumero.setEnabled(False)

# Bairro
caixaTextoBairro = QLineEdit(janela)
caixaTextoBairro.move(160, 220)
caixaTextoBairro.resize(300, 25)
caixaTextoBairro.setEnabled(False)

# Cidade
caixaTextoCidade = QLineEdit(janela)
caixaTextoCidade.move(160, 260)
caixaTextoCidade.resize(300, 25)
caixaTextoCidade.setEnabled(False)

# UF
caixaTextoUf = QLineEdit(janela)
caixaTextoUf.move(160, 300)
caixaTextoUf.resize(50, 25)
caixaTextoUf.setEnabled(False)


btnLimpar = QPushButton("Limpar", janela)
btnLimpar.move(160, 350)
btnLimpar.resize(100, 30)
btnLimpar.clicked.connect(limpaCampos)

btncep = QPushButton("Buscar CEP", janela)
btncep.move(280, 350)
btncep.resize(120, 30)
btncep.clicked.connect(validaCampos)

# exibindo a janela 
janela.show()

# iniciando o loop de eventos 
sys.exit(app.exec_())
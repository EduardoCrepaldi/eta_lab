from src.phonebook import Phonebook

book = Phonebook()

book.add("Polícia Civíl", "321")
book.add("Antonio", "193")
book.add("Mãe", "1588899990")
book.add("Bombeiro", "193")

if book.entries.get('eeee'):
    print("SUCESSO")

print(book.entries.get('eeee'))

# LINHA DE COMNADO ==>
# pytest. --cov. --cov-report html

# Criar arquivo na raiz de .coveragerc
"""
[report]
fail_under=70

Qual a quantidade de linhas do projeto que estão cobertos no nossos testes unitarios Statements
"""

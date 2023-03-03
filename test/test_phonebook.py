import pytest as pytest

from src.phonebook import Phonebook


class TestPhonebook:

    def setup_method(self):
        self.book = Phonebook()

    def teardown_method(self):
        self.book = None

    def test_add_nome_invalido(self):
        """
        Tentativa de adicionar um nome com caractere especial # @ ! $ %
        :return: "Nome invalido"
        """
        # Setup
        name_invalid = "Eduardo@"
        number_valid = "1234567654"
        expected = "Nome inválido"

        # Chamada
        result = self.book.add(name_invalid, number_valid)

        # Avaliação
        assert result == expected
        assert len(self.book.entries) == 1

    @pytest.mark.parametrize('number_invalid', ["", "1", "12", "123456789012345", 233, 34.44])
    def test_add_validate_number_invalid(self, number_invalid):
        """
        Tentativa de adicionar número estourando o limite inferior do tamanho (domínio permitido: 3 < número < 14)
        :return: "Numero invalido"
        """
        # Setup
        name_valid = "Eduardo"
        expected = "Número inválido"
        # Chamada
        result = self.book.add(name_valid, number_invalid)

        # Avaliação
        assert result == expected
        assert len(self.book.entries) == 1

    def test_add_success(self):
        """
        Tentativa de adicionar com nome e número válidos
        :return: "Numero adicionado"
        """
        # Setup
        name_valid = "Bombeiro"
        number_valid = "193"
        expected = "Número adicionado"

        # Chamada
        result = self.book.add(name_valid, number_valid)

        # Avaliação
        assert expected == result
        assert self.book.entries.get(name_valid) == number_valid

    def test_add_name_duplicate_name(self):
        """
        Tentativa de adicionar mesmo nome duas vezes
        :return: "Número já cadastrado"
        """
        # Setup
        duplicate_name = "POLICIA"
        number_valid = "159"
        expected = "Usuário já cadastrado"

        # Chamada
        result = self.book.add(duplicate_name, number_valid)

        # Avaliação
        assert result == expected
        assert self.book.entries['POLICIA'] == '190'

    def test_lookup_success(self):
        """
        Validando retorno de contato com sucesso, para isso iremos adicionar 3 contatos a mais
        No qual iremos buscar por Bombeiro
        :return: "{'Bombeiro':'193'}"
        """
        # Setup
        self.book.add("Polícia Civil", "197")
        self.book.add("Bombeiro", "193")
        self.book.add("Procon", "151")
        expected = {'Bombeiro': '193'}

        # Chamada
        result = self.book.lookup("Bombeiro")

        # Avaliação
        assert result == expected

    def test_lookup_special_character(self):
        """
        Tentativa de retonar um nome vázio caractere especial # @ ! $ %
        Só vai ser validado com o caracter @ pois temos um outro teste para o método validate_name que valida todos os caracteres especiais passado na parametrização
        :return: "Nome inválido"
        """
        # Setup
        name_invalid = "eduardo@crepaldi.com"
        expected = "Nome inválido"

        # Chamada
        result = self.book.lookup(name_invalid)

        # Avaliação
        assert result == expected

    def test_lookup_name_not_exist(self):
        """
        Validando retorno de contato inexistente
        :return: "Nome não existe"
        """
        # Setup
        name_not_exist = "nao"
        expected = "Nome não existe"

        # Chamada
        result = self.book.lookup(name_not_exist)

        # Avaliação
        assert result == expected

    def test_get_names(self):
        """
        Validando retorno de lista de nomes cadastrado
        :return: "Nome inválido"
        """
        # Setup
        name = "Eduardo"
        number = "123"
        name2 = "Hugo"
        number2 = "321"
        self.book.add(name, number)
        self.book.add(name2, number2)
        expected = ['POLICIA', name, name2]

        # Chamada
        result = self.book.get_names()
        # Avaliação
        assert result == expected

    def test_get_numbers(self):
        """
        Validando retorno de lista dos numeros cadastrado
        :return: "Nome inválido"
        """
        # Setup
        name = "Eduardo"
        number = "123"
        name2 = "Hugo"
        number2 = "321"
        self.book.add(name, number)
        self.book.add(name2, number2)
        expected = ['190', number, number2]

        # Chamada
        result = self.book.get_numbers()
        # Avaliação
        assert result == expected

    def test_clear(self):
        """
        Validando se método clear está limpando o dicionario entries
        :return: "phonebook limpado"
        """
        # Setup
        expected = "phonebook limpado"

        # Chamada
        result = self.book.clear()

        # Avaliacao
        assert result == expected
        assert self.book.entries == {}

    def test_search_success(self):
        """
        Validando se o método search estará retornando os dados certo e listagem
        Neste teste estou validando se está trazendo todos os valores de Polícia, perceba que tem um acento
        :return: {"Polícia Civíl": "321", "Polícia Militar": "333"}"""
        # Setup
        name_search = "Polícia"
        self.book.add("Polícia Civíl", "321")
        self.book.add("Bombeiro", "193")
        self.book.add("Polícia Militar", "333")
        self.book.add("Policia Teste", "111")
        expected = {"Polícia Civíl": "321", "Polícia Militar": "333"}

        # Chamada
        result = self.book.search(name_search)

        # Avaliação
        assert result == expected

    def test_search_name_not_exist(self):
        """
        Validando se o método search está um nome inexistente na lista
        :return: "Nome não existe"
        """
        # Setup
        name_invalid = "Bombeiro"
        expected = "Nome não existe"

        # Chamada
        result = self.book.search(name_invalid)

        # Avaliação
        assert result == expected
    def test_search_name_invalid(self):
        """
        Validando se o método search está validando o nome quando passado inválido
        :return: "Nome inválido"
        """
        # Setup
        name_invalid = "#edu"
        expected = "Nome inválido"

        # Chamada
        result = self.book.search(name_invalid)

        # Avaliação
        assert result == expected

    def test_get_phonebook_sorted(self):
        """
        Validando se o método get_phonebook_sorted está trazendo ordenado a partir do nome
        para esse teste o retorno valido seria
        :return: {'Antonio': '193', 'Bombeiro': '193', 'Mãe': '1588899990', 'POLICIA': '190', 'Polícia Civíl': '321'}
        """
        #Setup
        expected = {'Antonio': '193', 'Bombeiro': '193', 'Mãe': '1588899990', 'POLICIA': '190', 'Polícia Civíl': '321'}
        list_keys = list(expected.keys())
        list_values = list(expected.values())
        self.book.add("Polícia Civíl", "321")
        self.book.add("Antonio", "193")
        self.book.add("Mãe", "1588899990")
        self.book.add("Bombeiro", "193")

        #Chamada
        result = self.book.get_phonebook_sorted()

        #Validação
        assert result == expected
        assert list(result.keys()) == list_keys
        assert list(result.values()) == list_values

    def test_get_phonebook_sorted_empty(self):
        """
        Validando se o método get_phonebook_sorted está trazendo vazio quando não há nenhum nome na lista
        para esse teste o retorno valido seria
        :return: {}
        """
        #Setup
        expected = {}
        self.book.clear()

        #Chamada
        result = self.book.get_phonebook_sorted()

        #Validação
        assert result == expected


    def test_get_phonebook_reverse(self):
        """
        Validando se o método get_phonebook_reverse está trazendo a ordenação reversa a partir do nome
        para esse teste o retorno valido seria
        :return: {'Polícia Civíl': '321', 'POLICIA': '190', 'Mãe': '1588899990', 'Bombeiro': '193', 'Antonio': '193'}
        """
        # Setup
        expected = {'Polícia Civíl': '321', 'POLICIA': '190', 'Mãe': '1588899990', 'Bombeiro': '193', 'Antonio': '193'}
        list_keys = list(expected.keys())
        list_values = list(expected.values())
        self.book.add("Polícia Civíl", "321")
        self.book.add("Antonio", "193")
        self.book.add("Mãe", "1588899990")
        self.book.add("Bombeiro", "193")

        # Chamada
        result = self.book.get_phonebook_reverse()

        # Validação
        assert result == expected
        assert list(result.keys()) == list_keys
        assert list(result.values()) == list_values

    def test_get_phonebook_reverse_empty(self):
        """
        Validando se o método get_phonebook_reverse está trazendo vazio quando não há nenhum nome na lista
        para esse teste o retorno valido seria
        :return: {}
        """
        # Setup
        expected = {}
        self.book.clear()

        # Chamada
        result = self.book.get_phonebook_sorted()

        # Validação
        assert result == expected

    def test_delete_success(self):
        """
        Validando se o método test_delete se ele está deletando com sucesso
        para esse teste o retorno valido seria
        :return: "Usuario deletado"
        """

        # Setup
        name = "Joao"
        number = "123456"
        message = "Usuario deletado"
        self.book.add(name, number)

        # Chamada
        result = self.book.delete(name)

        # Avaliacao
        assert message == result
        assert len(self.book.entries.keys()) == 1

    def test_delete_name_not_exist(self):
        """
        Validando se o método test_delete se ele retornando mensagem quando usuário pesquisado não existe
        para esse teste o retorno valido seria
        :return: "Usuário inexistente"
        """
        # Setup
        name = "Mike"
        message = "Usuário inexistente"

        # Chamada
        result = self.book.delete(name)

        # Avaliacao
        assert message == result
        assert len(self.book.entries.keys()) == 1


    def test_change_number_sucess(self):
        """
        Validando se o método test_change_number está atualizando o numero corretamente
        :return: "Numero de 'POLICIA' atualizado"
        """

        #Setup
        name = 'POLICIA'
        number = '900'
        expected = f"Número de {name} atualizado"

        #Chamada
        result = self.book.change_number(name, number)
        #Validação
        assert result == expected
        assert self.book.entries[name] == number


    def test_change_number_name_not_exist(self):
        """
        Validando se o método test_change_number está Validando um NOME inexistente
        :return: "Nome não existe"
        """

        # Setup
        name = 'Eduardo'
        number = '900'
        expected = "Nome não existe"

        # Chamada
        result = self.book.change_number(name, number)

        # Validação
        assert result == expected

    def test_change_number_name_invalid(self):
        """
        Validando se o método test_change_number está validando se o nome passado é valido
        :return: "Nome inválido"
        """

        # Setup
        name = 'Ed#'
        number = '900'
        expected = "Nome inválido"

        # Chamada
        result = self.book.change_number(name, number)

        # Validação
        assert result == expected

    def test_change_number_number_invalid(self):
        """
        Validando se o método test_change_number está validando se o NUMERO passado é valido
        :return: "Número inválido"
        """

        # Setup
        name = 'Edu'
        number = '12'
        expected = "Número inválido"

        # Chamada
        result = self.book.change_number(name, number)

        # Validação
        assert result == expected

    def test_get_name_by_number_success(self):
        """
        Validando se o método get_name_by_number está retornando o nome certo ao pesquisar pelo número
        :return: "Policia Civil"
        """
        # Setup
        number = "850"
        name = "Policia Civil"
        self.book.add("Bombeiro", "193")
        self.book.add(name, number)
        self.book.add("Engenheiro", "999")


        # Chamada
        result = self.book.get_name_by_number(number)

        # Avaliação
        assert result == name

    def test_get_name_by_number_invalid(self):
        """
        Validando se o método get_name_by_number está validando o numero
        :return: "Número inválido"
        """
        # Setup
        number = "13"
        expected = "Número inválido"
        # Chamada
        result = self.book.get_name_by_number(number)

        # Avaliação
        assert result == expected

    def test_get_name_by_number_not_exist(self):
        """
        Validando se o método get_name_by_number está validando se o número existe
        :return: "Número não existe"
        """
        # Setup
        number = "155"
        expected = "Número não existe"
        # Chamada
        result = self.book.get_name_by_number(number)

        # Avaliação
        assert result == expected

    @pytest.mark.parametrize('name,expected',
                             [('Edua', True), ('Edu12', True), ('Bomb@', False), ('#comentario', False), ('email@teste', False), ('claro!', False), ('R$10', False), ('porcenta%', False)])
    def test_add_validate_name(self, name, expected):
        """
        Validando as possibilidades de retorno do método validate name por parametrização
        :return: True or False
        """
        # Chamada
        result = self.book.validate_name(name)

        # Avaliação
        assert result == expected

class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if not self.validate_name(
                name):  # Foi criado um método para validar se o nome é valido ou se tem algum caracter inválido
            return 'Nome inválido'

        if self.validate_number(number):  # Número deveria estar entre 3 e 14
            return 'Número inválido'

        if name not in self.entries:
            self.entries[name] = number
            return 'Número adicionado'  # Trazendo o retonor para o IF

        return 'Usuário já cadastrado'  # Caso Exista já retorna usuário existente

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if not self.validate_name(name):
            return 'Nome inválido'

        for key in self.entries:
            if key == name:
                return {key: self.entries.get(key)}

        return "Nome não existe"

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        return list(self.entries.keys())  # Ajustando para retornar uma lista

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())  # Ajustando para retornar uma lista

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        if not self.validate_name(search_name):
            return "Nome inválido"

        result = {}  # Ajuste para ser um dicionario
        for name, number in self.entries.items():
            if search_name.upper() in name.upper():
                result[name] = number  # ajustando para ser inserido no dictionario

        if not result:
            return "Nome não existe"

        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order

        Foi criado um método que faz ordenação e reverso do dicionario conforme o nome
        """
        return self.order_dic(reverse=False)

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        Foi criado um método que faz ordenação e reverso do dicionario conforme o nome
        """
        return self.order_dic(reverse=True)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Usuario deletado'
        """
        if self.entries.get(name):
            self.entries.pop(name)
            return 'Usuario deletado'

        return "Usuário inexistente"

    def change_number(self, name, number):

        if self.validate_number(number):
            return "Número inválido"

        if not self.validate_name(name):
            return "Nome inválido"

        if not self.entries.get(name):
            return "Nome não existe"

        self.entries[name] = number
        return f"Número de {name} atualizado"

    def get_name_by_number(self, number):
        """
        Get name by number
        :param number: String with number
        :return: return Name
        """
        if self.validate_number(number):
            return "Número inválido"

        if number not in self.get_numbers():
            return "Número não existe"

        for key, value in self.entries.items():
            if value == number:
                return key

    def order_dic(self, reverse=False):
        """
        Método que retorna o tipo de ordenação Normal e Reversa
        :param number: reverse = False -> Retorna dados em ordem
        :param number: reverse = TRUE -> Retorna dados em ordem reversa
        :return: return Dictionary
        """
        phonebook_order = {}
        list_name = list(self.entries.keys())  # Transformando nomes em lista
        list_name.sort()  # Ordenando Nomes

        if reverse:
            list_name.reverse()  # Ordenação reversa dos nomes

        for name in list_name:
            phonebook_order[name] = self.entries[name]

        return phonebook_order

    """
    Novo método criado para validar se o nome é valido ou não
    """

    def validate_name(self, name):
        validate = ["#", "@", "!", "$", "%"]
        for n in name:
            if n in validate:
                return False
        return True

    def validate_number(self, number):
        return type(number) is not str or (len(number) < 3 or len(number) > 14)

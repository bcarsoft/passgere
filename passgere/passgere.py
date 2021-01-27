from random import randint, choice


class PassGere:
    """
    This class can generate a new password.
    bcarsoft
    """

    def __init__(self):
        """Builder"""
        self._passw = ''

    def generate_pass(self, size=8, **kwargs):
        """
        This method is responsible for generate it.
        kwargs has the follwing keys:
        :param size: int
        :param kwargs: dict
        it (kwargs) has:
        - upcase
        - lowcase
        - numbers
        - simbolo1
        - simbolo2
        - simbolo3
        :return: str or none
        """
        for _ in range(size):
            data_pass = self._get_true_getters_method(**kwargs)
            if not data_pass:
                return None
            method = self._switch_method(data_pass)
            method = self._switch_element(method)
            self._set_passw(self._get_passw() + method)
        else:
            return self._get_passw()

    def _get_dict(self, **kwargs):
        """
        Explicit Dictionary.
        :param kwargs: dict
        :return: dic
        """
        return {i[0]: i[1] for i in kwargs.items()}

    def _get_upcase(self):
        """
        This method returns a generator of upcase characters.
        :return: generator
        """
        return (chr(lt) for lt in range(65, 91))

    def _get_lowcase(self):
        """
        This method returns a generator of lowcase characters.
        :return: generator
        """
        return (chr(lt) for lt in range(97, 123))

    def _get_numbers(self):
        """
        This methdo returns a generator of numbers characters.
        :return: generator
        """
        return (chr(lt) for lt in range(48, 58))

    def _get_simbolo_1(self):
        """
        This method returns a generator of ascii
        characters from 33 to 47.
        :return: generator
        """
        return (chr(lt) for lt in range(33, 48))

    def _get_simbolo_2(self):
        """
        This method returns a generator of ascii
        characters from 58 to 64.
        :return: generator
        """
        return (chr(lt) for lt in range(58, 65))

    def _get_simbolo_3(self):
        """
        This method returns a generator of ascii
        characters from 91 to 95.
        :return: generator
        """
        return (chr(lt) for lt in range(91, 96))

    def _set_passw(self, passw=''):
        """
        set password.
        :param passw: str
        """
        self._passw = passw

    def _get_passw(self):
        """
        get password
        :return: str
        """
        return self._passw

    def _generate_number(self, min=0, max=1):
        """
        generate number.
        :param min: int
        :param max: int
        :return: int
        """
        return randint(a=min, b=max)

    def _get_true_getters_method(self, **kwargs):
        """
        It returns only data with value true in kwargs.
        :param kwargs: dict
        :return: dict or none
        """
        funcao = {i[0]: i[1] for i in kwargs.items() if i[1]}
        result = {}
        index = 1
        for i in funcao:
            if i == 'upcase':
                result[index] = self._get_upcase()
            elif i == 'lowcase':
                result[index] = self._get_lowcase()
            elif i == 'numbers':
                result[index] = self._get_numbers()
            elif i == 'simbolo1':
                result[index] = self._get_simbolo_1()
            elif i == 'simbolo2':
                result[index] = self._get_simbolo_2()
            elif i == 'simbolo3':
                result[index] = self._get_simbolo_3()
            index += 1
        else:
            return result if result.__len__() > 0 else None

    def _switch_method(self, dic={}):
        """
        This method simulates a switch command.
        :param dic: dict
        :param key: int
        :return: function -> generator
        """
        return dic[self._generate_number(min=1, max=dic.__len__())]

    def _switch_element(self, gen=()):
        """
        This method simulates a switch command.
        :param gen: generator
        :return: str
        """
        data = [dt for dt in gen]
        data = tuple(data)
        return choice(data)

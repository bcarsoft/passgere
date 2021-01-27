from passgere.passgere import PassGere


class Cliface:
    """
    This is a command line interface class.
    bcarsoft
    """

    def __init__(self):
        self._choose = 0
        self._values = {}
        self._gen = PassGere()

    def main(self):
        """
        This is the main method of the
        interface. Should be called first.
        """
        while True:
            if not self._root():
                break

    def _root(self):
        """
        This is the part where the user chooses
        for a new password or log out.
        :return: bool
        """
        print('-------------------')
        print('Password Generator')
        print('1 New Password')
        print('2 Exit from it')
        try:
            self._set_choose(int(input('Your Choose: ')))
            if self._get_choose() == 2:
                print('Log Out...')
                return False
            elif self._get_choose() == 1:
                return self._new_password()
            else:
                return True
        except ValueError:
            print('Invalid Input!')
            return True

    def _new_password(self):
        """
        This method takes information about characters type
        to create a new password.
        :return: bool
        """
        self._set_values()
        print('Choose Valid Characters')
        while True:
            print('\n- Upcase Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='upcase'):
                break
        while True:
            print('\n- Lowcase Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='lowcase'):
                break
        while True:
            print('\n- Numbers Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='numbers'):
                break
        while True:
            print('\n- Symbol 1 Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='simbolo1'):
                break
        while True:
            print('\n- Symbol 2 Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='simbolo2'):
                break
        while True:
            print('\n- Symbol 3 Characters')
            self._set_choose(input('y/n: '))
            if self._insert_value(key='simbolo3'):
                break
        if True not in self._values.values():
            print('Invalid Pass Information!')
            return True
        while True:
            try:
                self._set_choose(int(input('\n- Password Size: ')))
                if self._get_choose() < 1:
                    continue
                else:
                    break
            except ValueError:
                pass
        self._get_gen().reset_passw()
        passw = self._get_gen().generate_pass(
            size=self._get_choose(),
            **self._get_values()
        )
        print('+' * passw.__len__())
        print(passw)
        print('+' * passw.__len__())
        return True

    def _insert_value(self, key=''):
        """
        This method inserts values inside a dictionary
        to send to the class who will create a new password.
        :param key: str
        :return: bool
        """
        if self._get_choose().__eq__('y') or self._get_choose().__eq__('Y'):
            self._get_values()[key] = True
            return True
        elif self._get_choose().__eq__('n') or self._get_choose().__eq__('N'):
            self._get_values()[key] = False
            return True
        else:
            return False

    def _set_choose(self, choose):
        """
        set choose.
        :param choose: object
        """
        self._choose = choose

    def _get_choose(self):
        """
        get choose
        :return: object
        """
        return self._choose

    def _get_gen(self):
        """
        It returns PassGere instance.
        :return: PassGere instance
        """
        return self._gen

    def _set_values(self, values={}):
        """
        It inserts new values to this.
        :param values: dict
        """
        self._values = values

    def _get_values(self):
        """
        It returns str value.
        :return: str
        """
        return self._values

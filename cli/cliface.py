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
        while True:
            if not self._root():
                break

    def _root(self):
        print('-------------------')
        print('Password Generator')
        print('1 New Password')
        print('2 Exit from it')
        try:
            self._choose = int(input('Your Choose: '))
            if self._choose == 2:
                print('Log Out...')
                return False
            elif self._choose == 1:
                return self._new_password()
            else:
                return True
        except ValueError:
            print('Invalid Input!')
            return True

    def _new_password(self):
        self._values = {}
        print('Choose Valid Characters')
        while True:
            print('\n- Upcase Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='upcase'):
                break
        while True:
            print('\n- Lowcase Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='lowcase'):
                break
        while True:
            print('\n- Numbers Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='numbers'):
                break
        while True:
            print('\n- Symbol 1 Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='simbolo1'):
                break
        while True:
            print('\n- Symbol 2 Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='simbolo2'):
                break
        while True:
            print('\n- Symbol 3 Characters')
            self._choose = input('y/n: ')
            if self._insert_value(key='simbolo3'):
                break
        if True not in self._values.values():
            print('Invalid Pass Information!')
            return True
        while True:
            try:
                self._choose = int(input('\n- Password Size: '))
                if self._choose < 1:
                    continue
                else:
                    break
            except ValueError:
                pass
        self._gen.reset_passw()
        passw = self._gen.generate_pass(
            size=self._choose,
            **self._values
        )
        print('+' * passw.__len__())
        print(passw)
        print('+' * passw.__len__())
        return True

    def _insert_value(self, key=''):
        if self._choose.__eq__('y') or self._choose.__eq__('Y'):
            self._values[key] = True
            return True
        elif self._choose.__eq__('n') or self._choose.__eq__('N'):
            self._values[key] = False
            return True
        else:
            return False

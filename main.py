from passgere.passgere import PassGere


if __name__ == '__main__':
    ps = PassGere()
    print(
        ps.generate_pass(
            size=35,
            upcase=True,
            lowcase=True,
            numbers=True,
            simbolo1=False,
            simbolo2=True,
            simbolo3=False,
        )
    )

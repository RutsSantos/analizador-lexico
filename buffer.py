class Buffer:
    def load_buffer(self):
        arq = open('/Users/rutsantos/analizador-lexico/test.c', 'r')
        text = arq.readline()

        buffer = []
        cont = 1

        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                buf = ''.join(buffer)
                cont = 1
                yield buf

                buffer = []

        arq.close()
"""
TiniLang to BF translator
@author ymll
"""


class TiniLangTranslator():
    def __init__(self):
        self.bf_2_tini_dictionary = {
            '+': 'vi',
            '-': 'ni',
            '[': 'vicvic',
            ']': 'tinitini',
            '>': 'victi',
            '<': 'vicni',
            ',': 'vic',
            '.': 'tini'
        }
        self.tini_2_bf_dictionary = {v: k for k, v in self.bf_2_tini_dictionary.items()}

    def tini_2_bf(self, tini_code):
        out = ''
        try:
            for c in tini_code:
                out += self.tini_2_bf_dictionary[c]
        except KeyError as e:
            raise Exception('Not a Victini!') from e
        return out

    def bf_2_tini(self, bf_code):
        out = ''
        for c in bf_code:
            try:
                out += self.bf_2_tini_dictionary[c] + ' '
            except KeyError as e:
                pass
        return out


if __name__ == '__main__':
    bf_code = '+++++++++++++++++++++++++[>++>+++>++++>+++++<<<<-]+++++++++++++++++++++++++>>+++++.>+++++.++.' \
              '----------.++.+++++.>--------..........<<<<++++++++.-----------------------.'
    t = TiniLangTranslator()
    tini_code = t.bf_2_tini(bf_code)
    print(tini_code)

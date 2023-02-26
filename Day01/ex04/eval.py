class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (not isinstance(coefs, list)) or (not isinstance(words, list)) or \
                len(coefs) != len(words):
            return -1
        sum = 0
        for item in zip(words, coefs):
            sum += len(item[0]) * item[1]
        return sum

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (not isinstance(coefs, list)) or (not isinstance(words, list)) or \
                len(coefs) != len(words):
            return -1
        sum = 0
        for coef, word in enumerate(words):
            sum += coefs[coef] * len(word)
        return sum


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print(Evaluator.zip_evaluate(coefs, words))

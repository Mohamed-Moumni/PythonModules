import typing

class Evaluator:
    def zip_evaluate(coefs: list, words: list) -> int:
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(coef, float) for coef in coefs):
            return -1
        if not all(isinstance(word, str) for word in words):
            return -1
        sum = 0
        for item in zip(coefs, words):
            sum += (len(item[1]) * item[0])
        return sum
    def enumerate_evaluate(coefs: list, words: list) -> int:
        if len(coefs) != len(words):
            return -1
        if not all(isinstance(coef, float) for coef in coefs):
            return -1
        if not all(isinstance(word, str) for word in words):
            return -1
        sum = 0
        for item in enumerate(words):
            sum += (len(item[1]) * coefs[item[0]])
        return sum



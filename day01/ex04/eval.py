class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words):
            return -1
        for nbr, w in zip(coefs, words):
            result = result + (len(w) * nbr)
        return result
    @staticmethod
    def enumerate_evaluate(coefs, words):
        result = 0
        if len(coefs) != len(words):
            return -1
        for nbr in enumerate(coefs):
            result = result + (len(words[nbr[0]]) * nbr[1])
        return result
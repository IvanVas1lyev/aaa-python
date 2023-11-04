"""
Implementation of a class that counts the number of words
in a list of sentences
"""


class CountVectorizer:
    """
    Class that counts the number of words in a list of sentences
    """

    def __init__(self) -> None:
        """
        Inits CountVectorizer class
        :return: None
        """
        self.vocab = {}
        self.vectors = []

    def fit_transform(self, sentences: list) -> list:
        """
        Function that counts the number of words in a list of sentences
        :param sentences:
        :return: None
        """
        self.vectors = []
        self.vocab = {}

        index = 0

        for sentence in sentences:
            for word in sentence.lower().split():
                if word not in self.vocab:
                    self.vocab[word] = index
                    index += 1

        for sentence in sentences:
            vector = [0] * len(self.vocab)

            for word in sentence.lower().split():
                vector[self.vocab[word]] += 1

            self.vectors.append(vector)

        return self.vectors

    def get_feature_name(self) -> list:
        """
        Function that print the number of words in a list of sentences
        :return: List of lists with number of words for every sentence
        """
        return list(self.vocab.keys())


if __name__ == '__main__':
    cv = CountVectorizer()
    bunch_of_boring_words = [
        "Hi my name is Vanya",
        "Hi my name is Nikola",
        "Vanya and Nikola are a good team"
    ]

    cv.fit_transform(bunch_of_boring_words)
    print(cv.get_feature_name())

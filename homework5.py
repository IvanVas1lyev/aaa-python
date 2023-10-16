"""
Implementation of a class that counts the number of words
in a list of sentences
"""


class CountVectorizer():
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

    def fit_transform(self, sentences: list) -> None:
        """
        Function that counts the number of words in a list of sentences
        :param sentences:
        :return: None
        """
        index = 0

        for sentence in sentences:
            for word in sentence.split():
                if word not in self.vocab:
                    self.vocab[word] = index
                    index += 1

        for sentence in sentences:
            vector = [0] * len(self.vocab)

            for word in sentence.split():
                if word in self.vocab:
                    vector[self.vocab[word]] += 1

            self.vectors.append(vector)

    def get_feature_name(self) -> list:
        """
        Function that print the number of words in a list of sentences
        :return: List of lists with number of words for every sentence
        """
        return self.vectors


if __name__ == '__main__':
    cv = CountVectorizer()
    bunch_of_boring_words = [
        "Hi my name is Vanya",
        "Hi my name is Nikola",
        "Vanya and Nikola are a good team"
    ]

    cv.fit_transform(bunch_of_boring_words)
    print(cv.get_feature_name())

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
        Init CountVectorizer class
        :return: None
        """
        self.vocab = {}
        self.vectors = []

    def fit_transform(self, sentences: list) -> list:
        """
        Function that counts the number of words in a list of sentences
        :param sentences: Sentences of the corpus
        :return: Vectors list with the count matrix
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

    def get_feature_names(self) -> list:
        """
        Function that print the number of words in a list of sentences
        :return: List of lists with number of words for every sentence
        """
        return list(self.vocab.keys())


if __name__ == '__main__':
    cv = CountVectorizer()
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    count_matrix = cv.fit_transform(corpus)

    print(cv.get_feature_names())
    print(count_matrix)

"""
Implementation of a class tf-idf-vectorizer transformer
"""
from count_vectorizer_class import CountVectorizer
from tf_idf_class import TfIdfTransformer


class TfIdfVectorizer(CountVectorizer):
    """
    Class that computes TF-IDF-Vectorizer transformation
    """
    def __init__(self) -> None:
        """
        Init TfIdfVectorizer class
        """
        super().__init__()
        self.tf_idf = []
        self.tf_idf_transformer = TfIdfTransformer()

    def fit_transform(self, sentences: list) -> list:
        """
        Function that counts the number of words in a list of sentences
        and computes the TF-IDF transformation on the count matrix
        :param sentences: Sentences of the corpus
        :return: TF-IDF matrix
        """
        count_matrix = super().fit_transform(sentences)
        self.tf_idf = self.tf_idf_transformer.fit_transform(count_matrix)

        return self.tf_idf


if __name__ == '__main__':
    # take matrix from task:
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    tiv = TfIdfVectorizer()
    tfidf_matrix = tiv.fit_transform(corpus)

    print(tiv.get_feature_names())
    print(tfidf_matrix)

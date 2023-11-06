"""
Implementation of a class tf-idf transformer
"""
from tf import tf_transform
from idf import idf_transform


class TfIdfTransformer:
    """
    Class that computes TF-IDF transformation
    """
    def __init__(self) -> None:
        """
        Init TfIdfTransformer class
        :return: None
        """
        self.tf = []
        self.idf = []
        self.tf_idf = []

    def fit_transform(self, count_matrix: list) -> list:
        """
        Function that computes the TF-IDF transformation on the count matrix
        :param count_matrix: Matrix with document-term frequencies
        :return: TF-IDF matrix
        """
        count_matrix_docs_num = len(count_matrix)
        count_matrix_doc_words_num = len(count_matrix[0])

        self.tf = tf_transform(count_matrix)
        self.idf = idf_transform(count_matrix)
        self.tf_idf = []

        for i in range(count_matrix_docs_num):
            self.tf_idf.append([0] * count_matrix_doc_words_num)

            for j in range(count_matrix_doc_words_num):
                self.tf_idf[i][j] = round(self.idf[j] * self.tf[i][j], 3)

        return self.tf_idf


if __name__ == '__main__':
    # take matrix from task:
    cm = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    transformer = TfIdfTransformer()
    tfidf_matrix = transformer.fit_transform(cm)

    print(tfidf_matrix)

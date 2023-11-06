"""
Implementation of the idf transform function
"""
import math


def idf_transform(count_matrix: list) -> list:
    """
    Function that computes IDF transformation on the count matrix
    :param count_matrix: Matrix with document-term frequencies
    :return: IDF vector
    """
    count_matrix_docs_num = len(count_matrix)
    count_matrix_doc_words_num = len(count_matrix[0])
    idf_transform_result = [0 for i in range(count_matrix_doc_words_num)]

    for doc in count_matrix:
        for i in range(count_matrix_doc_words_num):
            idf_transform_result[i] += 1 if doc[i] > 0 else 0

    for i, word_freq in enumerate(idf_transform_result):
        idf_transform_result[i] = round(math.log((count_matrix_docs_num + 1)
                                                 / (word_freq + 1)) + 1, 3)

    return idf_transform_result


if __name__ == '__main__':
    # take matrix from task:
    cm = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    idf_count_matrix_result = idf_transform(cm)

    print(idf_count_matrix_result)

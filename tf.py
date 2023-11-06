"""
Implementation of the tf transform function
"""


def tf_transform(count_matrix: list) -> list:
    """
    Function that computes TF transformation of the count matrix
    :param count_matrix: Matrix with document-term frequencies
    :return: TF matrix
    """
    tf_matrix = []

    for nums_vec in count_matrix:
        tf_matrix.append([round(num / sum(nums_vec), 3) for num in nums_vec])

    return tf_matrix


if __name__ == '__main__':
    # take matrix from task:
    cm = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tf_count_matrix_result = tf_transform(cm)

    print(tf_count_matrix_result)

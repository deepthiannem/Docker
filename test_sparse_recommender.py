import pytest
from sparse_recommender import SparseMatrix

# Test case for setting and getting values in the SparseMatrix
def test_set_and_get():
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    assert matrix.get(0, 0) == 5

# Test case for setting multiple values in the SparseMatrix
def test_set_multiple_values():
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    matrix.set(1, 2, 3)
    assert matrix.get(0, 0) == 5
    assert matrix.get(1, 2) == 3

# Test case for setting invalid values in the SparseMatrix
def test_set_invalid_values():
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    matrix.set(1, 2, 3)
    assert matrix.get(2, 2) is None  

# Test case for recommending items based on a vector
def test_recommend():
    matrix = SparseMatrix()
    matrix.set(0, 0, 7)
    matrix.set(1, 1, 3)
    vector = [1, 0]
    recommendations = matrix.recommend(vector)
    assert recommendations == [7, 0]

# Test case for adding a movie to the SparseMatrix
def test_add_movie():
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 9)
    matrix2 = SparseMatrix()
    matrix2.set(0, 0, 7)
    matrix1.add_movie(matrix2)
    assert matrix1.get(0, 0) == 16
    assert matrix1.get(0, 1) is None 
    
# Test case for converting the SparseMatrix to a dense matrix
def test_to_dense():
    matrix = SparseMatrix()
    matrix.set(0, 0, 7)
    matrix.set(1, 1, 9)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[7, 0], [0, 9]]

# Test case for setting negative row and column indices
def test_set_negative_row_col():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(-1, 0, 5)
    with pytest.raises(ValueError):
        matrix.set(0, -1, 5)

# Test case for setting an invalid value in the SparseMatrix
def test_set_invalid_value():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(0, 0, 'abc')

# Test case for recommending items with an invalid vector length
def test_recommend_invalid_vector_length():
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    matrix.set(1, 1, 3)
    vector = [1, 0, 1]  
    with pytest.raises(ValueError):
        recommendations = matrix.recommend(vector)

# Test case for adding a movie with negative indices to the SparseMatrix
def test_add_movie_negative_indices():
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 9)
    matrix2 = SparseMatrix()
    with pytest.raises(ValueError):
        matrix2.set(-1, 0, 7)
    matrix1.add_movie(matrix2)  
    assert matrix1.get(0, 0) == 9


# Test case for converting an empty SparseMatrix to a dense matrix
def test_to_dense_empty_matrix():
    matrix = SparseMatrix()
    dense_matrix = matrix.to_dense()
    assert dense_matrix == []







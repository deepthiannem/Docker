class SparseMatrix:
    def __init__(self):
        self.data = {}  # Initialize the data dictionary to store sparse matrix values

    def set(self, row, col, value):
        # Set a value in the sparse matrix at the specified row and column
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative.")
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or a float.")
        self.data[(row, col)] = value

    def get(self, row, col):
        # Get a value from the sparse matrix at the specified row and column
        return self.data.get((row, col))

    def recommend(self, vector):
        num_columns = max(col for _, col in self.data.keys()) + 1
        if len(vector) != num_columns:
            raise ValueError("Vector length must match the number of columns in the matrix.")
    
        recommendations = []
        for row in range(len(vector)):
            recommendation = 0
            for (r, c), value in self.data.items():
                if r == row:
                    recommendation += value * vector[c]
            recommendations.append(recommendation)
        return recommendations

    def add_movie(self, matrix):
        for (row, col), value in matrix.data.items():
            if row < 0 or col < 0:
                raise ValueError("Row and column indices must be non-negative.")
            if not isinstance(value, (int, float)):
                raise ValueError("Value must be an integer or a float.")
            existing_value = self.data.get((row, col), 0)
            new_value = existing_value + value
            self.set(row, col, new_value)


    def to_dense(self):
        # Convert the sparse matrix to a dense matrix
        if not self.data:
            return []  # Return an empty matrix if there is no data
        rows = max(row for row, _ in self.data.keys()) + 1
        cols = max(col for _, col in self.data.keys()) + 1
        dense_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        return dense_matrix

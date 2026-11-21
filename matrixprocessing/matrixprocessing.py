import sys


def read_matrix():
  try:
    rows, cols = map(int, input("Enter matrix size: > ").split())
    print("Enter matrix:")
    matrix = []
    for _ in range(rows):
      row = list(map(float, input("> ").split()))
      if len(row) != cols:
        return None
      matrix.append(row)
    return matrix
  except Exception:
    return None


def print_matrix(matrix):
  for row in matrix:
    formatted_row = [
        str(int(val)) if val.is_integer() else str(val) for val in row
    ]
    print(" ".join(formatted_row))


def add_matrices():
  print("Enter size of first matrix: ", end="")
  m1 = read_matrix()
  if m1 is None:
    print("ERROR")
    return

  print("Enter size of second matrix: ", end="")
  m2 = read_matrix()
  if m2 is None:
    print("ERROR")
    return

  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    print("The operation cannot be performed.")
    return

  result = [
      [m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
  ]
  print("The result is:")
  print_matrix(result)


def multiply_by_constant():
  m = read_matrix()
  if m is None:
    print("ERROR")
    return
  const = float(input("Enter constant: > "))
  result = [[val * const for val in row] for row in m]
  print("The result is:")
  print_matrix(result)


def multiply_matrices():
  print("Enter size of first matrix: ", end="")
  m1 = read_matrix()
  if m1 is None:
    print("ERROR")
    return

  print("Enter size of second matrix: ", end="")
  m2 = read_matrix()
  if m2 is None:
    print("ERROR")
    return

  if len(m1[0]) != len(m2):
    print("The operation cannot be performed.")
    return

  result = [
      [
          sum(m1[i][k] * m2[k][j] for k in range(len(m2)))
          for j in range(len(m2[0]))
      ]
      for i in range(len(m1))
  ]
  print("The result is:")
  print_matrix(result)


def transpose_matrix():
  print("1. Main diagonal")
  print("2. Side diagonal")
  print("3. Vertical line")
  print("4. Horizontal line")
  choice = int(input("Your choice: > "))

  m = read_matrix()
  if m is None:
    print("ERROR")
    return

  rows = len(m)
  cols = len(m[0])
  result = []

  if choice == 1:  # Main diagonal
    result = [[m[j][i] for j in range(rows)] for i in range(cols)]
  elif choice == 2:  # Side diagonal
    result = [
        [m[rows - 1 - j][cols - 1 - i] for j in range(rows)]
        for i in range(cols)
    ]
  elif choice == 3:  # Vertical line
    result = [[m[i][cols - 1 - j] for j in range(cols)] for i in range(rows)]
  elif choice == 4:  # Horizontal line
    result = [[m[rows - 1 - i][j] for j in range(cols)] for i in range(rows)]

  print("The result is:")
  print_matrix(result)


def get_matrix_minor(m, i, j):
  return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]


def get_matrix_determinant(m):
  if len(m) == 1:
    return m[0][0]
  if len(m) == 2:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

  det = 0
  for current_column in range(len(m)):
    minor = get_matrix_minor(m, 0, current_column)
    det += (
        (-1) ** current_column
        * m[0][current_column]
        * get_matrix_determinant(minor)
    )
  return det


def calculate_determinant():
  m = read_matrix()
  if m is None or len(m) != len(m[0]):
    print("The operation cannot be performed.")
    return
  det = get_matrix_determinant(m)
  print("The result is:")
  if det.is_integer():
    print(int(det))
  else:
    print(round(det, 4))


def inverse_matrix():
  m = read_matrix()
  if m is None or len(m) != len(m[0]):
    print("This matrix doesn't have an inverse.")
    return

  det = get_matrix_determinant(m)
  if det == 0:
    print("This matrix doesn't have an inverse.")
    return

  n = len(m)
  if n == 1:
    print("The result is:")
    print(f"{1 / m[0][0]:.2f}")
    return

  cofactors = []
  for r in range(n):
    cofactor_row = []
    for c in range(n):
      minor = get_matrix_minor(m, r, c)
      cofactor = (-1) ** (r + c) * get_matrix_determinant(minor)
      cofactor_row.append(cofactor)
    cofactors.append(cofactor_row)

  # Transpose cofactor matrix (adjugate matrix)
  cofactors = [[cofactors[j][i] for j in range(n)] for i in range(n)]

  # Divide by determinant
  result = [[cofactors[i][j] / det for j in range(n)] for i in range(n)]

  print("The result is:")
  for row in result:
    formatted_row = []
    for val in row:
      formatted_row.append(f"{val:.2f}")
    print(" ".join(formatted_row))


def main():
  while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: > ")
    if choice == "1":
      add_matrices()
    elif choice == "2":
      multiply_by_constant()
    elif choice == "3":
      multiply_matrices()
    elif choice == "4":
      transpose_matrix()
    elif choice == "5":
      calculate_determinant()
    elif choice == "6":
      inverse_matrix()
    elif choice == "0":
      break


if __name__ == "__main__":
  main()
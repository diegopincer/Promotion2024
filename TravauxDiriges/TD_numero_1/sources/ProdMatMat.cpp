#include <algorithm>
#include <cassert>
#include <iostream>
#include <thread>
#if defined(_OPENMP)
#include <omp.h>
#endif
#include "ProdMatMat.hpp"

namespace {
void prodSubBlocks(int iRowBlkA, int iColBlkB, int iColBlkA, int szBlock,
                   const Matrix& A, const Matrix& B, Matrix& C) {

  #pragma omp parallel for collapse(2)
  for (int j = iRowBlkA; j < std::min(A.nbRows, iRowBlkA + szBlock); ++j)
    for (int k = iColBlkB; k < std::min(B.nbCols, iColBlkB + szBlock); k++)
      for (int i = iColBlkA; i < std::min(A.nbCols, iColBlkA + szBlock); i++)
        C(i, j) += A(i, k) * B(k, j);
}
const int szBlock = 32;
}  // namespace


Matrix operator*(const Matrix& A, const Matrix& B) {
  Matrix C(A.nbRows, B.nbCols, 0.0);
  //prodSubBlocks(0, 0, 0, std::max({A.nbRows, B.nbCols, A.nbCols}), A, B, C);
   for (int iRowBlkA = 0; iRowBlkA < A.nbRows; iRowBlkA += szBlock) {
    for (int iColBlkB = 0; iColBlkB < B.nbCols; iColBlkB += szBlock) {
      for (int iColBlkA = 0; iColBlkA < A.nbCols; iColBlkA += szBlock) {
        prodSubBlocks(iRowBlkA, iColBlkB, iColBlkA, szBlock, A, B, C);
      }
    }
  }
  return C;
}

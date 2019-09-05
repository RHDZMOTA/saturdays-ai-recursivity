import fire
import logging

from util import TriangleBuilder, caching, timeit


logger = logging.getLogger(__name__)


class Main(object):
    builder = TriangleBuilder()

    @caching
    def get_element_recursively(self, i, j):
        return 1 if (j >= i or j == 0) else \
            self.get_element_recursively(i=i-1, j=j-1) + self.get_element_recursively(i=i-1, j=j)

    def pascal_triangle_a(self, level, index=0):
        if index < level:
            row = [str(self.get_element_recursively(i=index, j=j)) for j in range(index+1)]
            print(" ".join(row))
            self.pascal_triangle_a(level=level, index=index+1)

    def pascal_triangle_b(self, level, index=0):
        if index < level:
            row = self.builder.get_row(index=index)
            print(" ".join(row))
            self.pascal_triangle_b(level, index+1)

    @timeit(logger)
    def pascal_triangle(self, level, option):
        if "a" == option.lower():
            self.pascal_triangle_a(level=level, index=0)
        if "b" == option.lower():
            self.pascal_triangle_b(level=level, index=0)

    @caching
    def fibonacci(self, i):
        if i <= 1:
            return 1
        return self.fibonacci(i=i-2) + self.fibonacci(i=i-1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)

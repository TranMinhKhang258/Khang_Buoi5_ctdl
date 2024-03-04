def tuple_elementwise_sum(tuple1, tuple2):
    output_tuple = tuple(x + y for x, y in zip(tuple1, tuple2))
    return output_tuple

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

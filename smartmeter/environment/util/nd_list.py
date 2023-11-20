def create_nd_list(dimensions, value=0):
    if not dimensions:
        return value
    return [create_nd_list(dimensions[1:], value) for _ in range(dimensions[0])]
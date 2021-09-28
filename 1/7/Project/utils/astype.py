def astype(records, data_type):
    """A Pandas astype-like function.

    Args:
        records (list): A 1-D list.
        data_type (data type): The target data type.

    Returns:
        list: The converted records.

    Examples:
        >>> l = ['1', '2', '3']
        >>> astype(l, int)
    """
    return [data_type(record) for record in records]
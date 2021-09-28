def iloc(records, rows, cols=None) -> list:
    """A Pandas .iloc-like function.
    
    Args:
        records (list): A 2-D list.
        rows (str or int): The indices of rows.
        cols (str or int): The indices of columns. Default is None.

    Returns:
        list: The sliced records.

    Examples:
        >>> l = [[1, 2], [1, 3], [2, 3]]
        >>> iloc(l,  rows=':')
        [[1, 2], [1, 3], [2, 3]]
        >>> iloc(l,  rows=0)
        [[1, 2]]
        >>> iloc(l,  rows='1:')
        [[1, 3], [2, 3]]
        >>> iloc(l,  rows=':2')
        [[1, 2], [1, 3]]
        >>> iloc(l,  rows=':', cols=':')
        [[1, 2], [1, 3], [2, 3]]
        >>> iloc(l,  rows=':', cols='1:')
        [[2], [3], [3]]
        >>> iloc(l,  rows=':', cols=0)
        [1, 1, 2]
    """
    assert isinstance(records[0], list), 'records must be a 2-D list!'
    def _parseColon(s: str) -> int:
        """Parse colon in rows or cols.

        Args:
            s (str): rows or cols
        
        Returns:
            int: Then start or/and end of the rows or cols.
        """
        s = str(s)
        if ':' not in s:
            return int(s), int(s)+1
        else:
            start = s.split(':')[0]
            end = s.split(':')[1]
        if start == '':
            start = 0
        else:
            start = int(start)
        if end == '':
            end = None
        else:
            end = int(end)
        return start, end
    # Get row_start, row_end
    row_start, row_end = _parseColon(rows)
    if cols is None:
        cols = ':'
    # Get col_start, col_end
    col_start, col_end = _parseColon(cols)
    # Slice rows
    records = records[row_start:row_end]
    # Slice columns
    if col_end is None:
        records = [record[col_start:col_end] for record in records]
    else:
        records = [record[col_start] for record in records]

    return records
def iloc(records, rows=':', cols=':') -> list:
    """A Pandas .iloc-like function.

    Args:
        records (list): A 2-D list.
        rows (str or int): The indices of rows. Default is ':'.
        cols (str or int): The indices of columns. Default is ':'.

    Returns:
        list: The sliced records.

    Examples:
        >>> l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> iloc(l)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> iloc(l,  rows=0)
        [[1, 2, 3]]
        >>> iloc(l,  rows=0, cols=0)
        [1]
        >>> iloc(l,  rows='0:1')
        [[1, 2, 3]]
        >>> iloc(l,  rows='1:')
        [[4, 5, 6], [7, 8, 9]]
        >>> iloc(l,  rows=':2')
        [[1, 2, 3], [4, 5, 6]]
        >>> iloc(l,  rows=':', cols='1:')
        [[2, 3], [5, 6], [8, 9]]
        >>> iloc(l,  rows=':', cols=0)
        [1, 4, 7]
        >>> iloc(l,  rows=':', cols='0:1')
        [1, 4, 7]
        >>> iloc(l,  rows=':', cols='0:2')
        [[1, 2], [4, 5], [7, 8]]
    """
    assert isinstance(records[0], list), 'records must be a 2-D list!'

    def _parseColon(ind: str) -> int:
        """Parse colon in rows or cols.

        Args:
            ind (str): rows or cols

        Returns:
            int: Then start or/and end of the rows or cols.

        Examples:
            # ':'.split(':') ---- ['', '']
            >>> _parseColon(':')
            (0, None)

            # '0'.split(':') ---- ['0]
            >>> _parseColon(0)
            (0, 1)

            # '1:'.split(':') ---- ['1', '']
            >>> _parseColon('1:')
            (1, None)

            # ':2'.split(':') ---- ['', '2']
            >>> _parseColon(':2')
            (0, 2)

            # '1:2'.split(':') ---- ['1', '2']
            >>> _parseColon('1:2')
            (1, 2)
        """
        ind = str(ind)
        ind = ind.split(':', maxsplit=1)
        start = ind[0]
        start = int(start) if start != '' else 0
        # if no ind[0], end = start+1
        end = ind[1] if len(ind) == 2 else start+1
        end = int(end) if end != '' else None

        return start, end

    # Get row_start, row_end
    row_start, row_end = _parseColon(rows)
    # Get col_start, col_end
    col_start, col_end = _parseColon(cols)
    # Slice rows
    records = records[row_start:row_end]
    # Slice columns
    if col_end is None:
        records = [record[col_start:col_end] for record in records]
    elif col_end - col_start != 1:
        records = [record[col_start:col_end] for record in records]
    else:
        records = [record[col_start] for record in records]

    return records

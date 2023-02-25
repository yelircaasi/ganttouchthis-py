def expand_tasks(task_abbr: str) -> list:
    def expand_block(block):
        error = ValueError(
            r"Tasks string not of a suitable form. Acceptable: \d{1, 3}(-\d{1, 3})?([A-Z]\d{0, 2}(-[A-Z]\d{0, 2})?)?"
        )
        if block.isalpha():
            return [block]
        if block.isnumeric():
            return list(map(str, range(1, int(block) + 1)))
        elif "-" in block:
            start, end = block.split("-")
            if start.isnumeric() and end.isnumeric():
                return list(map(str, range(int(start), int(end) + 1)))
            elif start.isalpha() and end.isalpha():
                return list(map(chr, range(ord(start), ord(end) + 1)))
            elif start.isalnum() and end.isalnum():
                try:
                    start_letter = start[0]
                    start_number = int(start[1:])
                    end_isalpha = (end_letter := end[0]).isalpha()
                    if end_isalpha and (start_letter != end_letter):
                        raise error
                    end_number = int(end[1:]) if end_isalpha else int(end)
                    print(start_letter, end_letter, start_number, end_number)

                    return list(map(lambda num: start_letter + str(num), range(start_number, end_number + 1)))
                except:
                    raise error
            else:
                raise error
        elif block.isalnum():
            letter, num = block[0], block[1:]
            if not letter.isalpha() and num.isnumeric():
                raise error
            return list(map(lambda x: letter + str(x), range(1, int(num) + 1)))
        else:
            raise error

    tasks = []
    blocks = task_abbr.split(",")
    for block in blocks:
        tasks.extend(expand_block(block))
    return tasks

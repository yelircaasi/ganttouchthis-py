from typing import Iterable, List, Union


def box(string_: str) -> str:
    n = len(string_)
    return f"┏━{n * '━'}━┓\n┃ {string_} ┃\n┗━{n * '━'}━┛"


def multibox(strings: Iterable[str]) -> str:
    lens = tuple(map(len, strings))
    top = "┏━{}━┓".format("━┳━".join(map(lambda i: i * "━", lens)))
    middle = "┃ {} ┃".format(" ┃ ".join(strings))
    bottom = "┗━{}━┛".format("━┻━".join(map(lambda i: i * "━", lens)))
    return "\n".join((top, middle, bottom))


def table(array2d_: List[List[Union[str, int]]], head=True) -> str:
    ...
    "─│┌ ┐"
    array2d: List[List[str]] = list(map(lambda row: list(map(str, row)), array2d_))
    print(array2d)
    assert len(set(map(len, array2d))) == 1  # all rows should have the same number of values
    nc = max(map(len, array2d))
    nr = len(array2d)
    widths = []
    for col in range(nc):
        widths.append(max(map(lambda i: len(array2d[i][col]), range(nr))))
    line = "\n├─{}─┤\n".format("─┼─".join(map(lambda i: i * "─", widths)))
    bottom = "└─{}─┘".format("─┴─".join(map(lambda i: i * "─", widths)))

    def textline(row, thick=False):
        sep = "┃" if thick else "│"
        row = map(lambda sw: f"{sw[0]: <{sw[1]}}", zip(row, widths))
        joiner = f" {sep} "
        return f"{sep} {joiner.join(row)} {sep}"

    if head:
        top = "┏━{}━┓".format("━┳━".join(map(lambda i: i * "━", widths)))
        middle = textline(array2d[0], thick=True)  # "┃ {} ┃".format(" ┃ ".join(array2d[0]))
        joiner = "┡━{}━┩".format("━╇━".join(map(lambda i: i * "━", widths)))

        return "\n".join(("", top, middle, joiner, line.join(map(textline, array2d[1:])), bottom))
    else:
        top = "┌─{}─┐".format("─┬─".join(map(lambda i: i * "─", widths)))
        return "\n".join(("", top, line.join(map(textline, array2d)), bottom))

    # https://graphemica.com/blocks/box-drawing

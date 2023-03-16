from typing import Any, Callable, Iterable, List

from .date import Date, date_range


def date_input(prompt_start: str = "Date", prompt_body: str = "") -> Date:
    if not prompt_body:
        prompt_body = "please enter date as yyyy-mm-dd or integer offset from today (empty -> 0)"
    prompt = f"{prompt_start}: {prompt_body}:\n "
    date_string = input(prompt) or "0"
    if date_string.isdigit():
        d = Date.today() + int(date_string)
    else:
        d = Date.fromisoformat(date_string)
    if not d:
        raise ValueError("Expect a date string (yyyy-mm-dd) or an integer.")
    return d

def option_input(options: Iterable[str], box: bool = True) -> str:
    func = option_input_with_box if box else option_input_without_box
    return func(options)


def parse_input(options_list):
    try:
        option_num = int(input("\n ").strip() or "1") - 1
        option = options_list[option_num]
        print()
        return option
    except:
        print("Invalid input; please enter a number corresponding to one of the options.")
        parse_input(options_list)


def option_input_with_box(options: Iterable[str]) -> str:
    options = list(options)
    print_options = options[:]
    print_options[0] += " (default)"
    width = max(26, max(map(len, print_options)) + 7)
    line = width * '─'
    print(f"┌{line}┐")
    print(f"│ {'Please select an option:': <{width-2}} │")
    print(f"├{line}┤")
    for i, option in enumerate(options, start=1):
        print(f"│{i: >3}) {option: <{width-6}} │")
    print(f"└{line}┘")
    
    return parse_input(options)
    

def option_input_without_box(options: Iterable[str]) -> str:
    options = list(options)
    print("Please select an option:")
    for i, option in enumerate(options, start=1):
        if i == 1:
            print(f"  {i}) {option} (default)")
        else:
            print(f"  {i}) {option}")
    return parse_input(options)


def validated_input(prompt: str, convertor: Callable = str, default: Any = None) -> Any:
    try:
        input_ = input(f"{prompt}: \n ")
        if not input_:
            return default
        output = convertor(input_)
        return output
    except:
        print(f"Please enter an input convertible by '{str(convertor)}'.")
        return validated_input(prompt, convertor)

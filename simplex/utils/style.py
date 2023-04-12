from utils.path import get_path


def get_adjusted_style(window_height: float) -> str:
    """The get_adjusted_style function takes a window_height argument, which is a float representing the height of a window. 
    The function adjusts a style sheet by replacing certain values with values calculated based on the window_height argument. 
    The adjusted style sheet is returned as a string.

    Args:
        window_height (float): A float representing the height of a window.

    Returns:
        str: The adjusted style sheet as a string.
    """

    replacement = {
        '@padding': f'{round(window_height / 200)}px',
        '@font-size': f'{round(window_height / 38.5)}px',
        '@button-height': f'{round(window_height / 38.5 + 7)}px',
        '@button-border-radius': f'{round(window_height / 38.5 + 7) // 2}px',
        '@tab-height': f'{round(window_height / 26)}px',
        '@tab-border-radius': f'{round(window_height / 52 + 5)}px',
        '@header-height': f'{round(window_height / 38.5 + 22)}px',
        '@header-width': f'{round(window_height / 38.5 + 12)}px',
        '@checkbox-size': f'{round(window_height / 52)}px',
        '@checkbox-border-radius': f'{round(window_height / 52) // 2 + 2}px',
        '@tableitem-border-radius': f'{round(window_height / 38.5 + 7)}px',
    }

    with open(get_path('assets/style.qss'), 'r') as file:
        style = file.read()

    for key in replacement:
        style = style.replace(key, replacement[key])

    return style

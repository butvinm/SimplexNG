from utils.path import get_path


def get_adjusted_style(window_height: float) -> str:
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

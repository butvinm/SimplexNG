class Style:
    def __init__(self, height: float):
        replacement = {
            '@padding': f'{round(height/200)}px',
            '@font-size': f'{round(height/38.5)}px',
            '@button-height': f'{round(height/38.5+7)}px',
            '@button-border-radius': f'{round(height/38.5+7)//2}px',
            '@tab-height': f'{round(height/26)}px',
            '@tab-border-radius': f'{round(height/52+5)}px',
            '@header-height': f'{round(height/38.5+22)}px',
            '@header-width': f'{round(height/38.5+12)}px',
            '@checkbox-size': f'{round(height/52)}px',
            '@checkbox-border-radius': f'{round(height/52)//2+2}px',
            '@tableitem-border-radius': f'{round(height/50)}px',
        }

        self.style = """
                * {font-family: "Arial", "Helvetica", "sans-serif";   font-size: @font-size;}
                QMainWindow { background: #808080;}
                QMenuBar { background: #fefefe; border: 3px solid #808080; border-radius: 10px; margin: 5px 5px 0; }
                QMenuBar::item { margin: 3px 15px 0; padding: 1px 4px; background: transparent; border-radius: 4px;}
                QMenuBar::item:selected { background: #e5e5e5;}
                QMenuBar::item:pressed { background: #808080; color: #ffffff;}
                QMenu { background-color: #fefefe; border: 3px solid #808080; border-radius: 10px;}
                QMenu::item { background-color: transparent; border-radius: 10px; margin: 6px;}
                QMenu::item:selected { background-color: #e5e5e5; color: #000000;}
                QPushButton { min-height: @button-height; background: #fefefe; border: 2px solid #fefefe; border-radius: @button-border-radius;}
                QPushButton:hover { border: 3px solid #808080;}
                QPushButton:pressed { background: #808080; border: 3px solid #808080; color: #ffffff;}
                QTabWidget::pane { background: #e5e5e5; border: none;}
                QTabBar::tab { height: @tab-height;  min-width: 237px; border-top-left-radius: @tab-border-radius; border-top-right-radius: @tab-border-radius;}
                QTabBar::tab:selected { background: #e5e5e5;}QTabBar::tab:!selected { background: #fefefe;}
                QTableWidget QTableCornerButton::section { background: rgba(0, 0, 0, 0); border: none;}
                QTableWidget { background: #fefefe; border-radius: 20px; gridline-color: #fefefe; selection-background-color: rgba(0, 0, 0, 0); selection-color: black;}
                QTableWidget::item { background: #ffffff; border: 1px solid #808080; border-radius: @tableitem-border-radius; margin: 5px; padding: @padding;}
                QTableWidget::item:selected { background: rgba(0, 0, 0, 0); border: 3px solid #808080; border-radius: @tableitem-border-radius;}
                QLineEdit { background: #ffffff; border: 3px solid #ffffff; border-radius: @tableitem-border-radius;}
                QHeaderView { border: none; background: rgba(0, 0, 0, 0);}
                QHeaderView::section { background: rgba(0, 0, 0, 0); border: none;}
                QHeaderView::section:horizontal { height: @header-height;}
                QHeaderView::section:vertical { width: @header-width; padding-left: 14px;}
                QSlider::groove:vertical { background: red; position: absolute; left: 4px; right: 4px;}
                QSlider::handle:vertical { height: 18px; background: #fefefe; border: 2px solid #808080; border-radius: 10px; margin: 0 -4px;}
                QSlider::add-page:vertical { background: #808080;}
                QSlider::sub-page:vertical { background: #fefefe;}
                QCheckBox { margin-left: 40px; spacing: 20px;}
                QCheckBox::indicator  { height: @checkbox-size;  width: @checkbox-size;   border-radius: @checkbox-border-radius;}
                QCheckBox::indicator:checked { border: 3px solid #808080; background: #808080;}
                QCheckBox::indicator:unchecked { border: 3px solid #808080; background: #fefefe;}
                """

        for key in replacement:
            self.style = self.style.replace(key, replacement[key])

import sys

if sys.platform == "win32":
    from .windows import AcrylicWindow
    from .windows import WindowsFramelessWindow as FramelessWindow
    from .windows import WindowsWindowEffect as WindowEffect
else:
    from .unix import UnixFramelessWindow as FramelessWindow
    from .unix import UnixWindowEffect as WindowEffect

    AcrylicWindow = FramelessWindow

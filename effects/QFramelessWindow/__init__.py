import sys

if sys.platform == "win32":
    from .windows import AcrylicWindow
    from .windows import WindowsFramelessWindow as FramelessWindow
    from .windows import WindowsWindowEffect as WindowEffect
    from .windows import NoIconWindowsFramelessWindow as NoIconFramelessWindow
else:
    raise SystemError("This System can not support uclock")

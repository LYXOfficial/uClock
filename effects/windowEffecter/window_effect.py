# coding:utf-8
import sys
from ctypes import *
from ctypes.wintypes import *

from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWinExtras import QtWin

from win32 import win32api, win32gui
from win32.lib import win32con

from .c_structures import *


class WindowEffect():
    """ 调用windows api实现窗口效果 """
    dwmapi = WinDLL("dwmapi")
    DwmExtendFrameIntoClientArea = dwmapi.DwmExtendFrameIntoClientArea
    DwmSetWindowAttribute = dwmapi.DwmSetWindowAttribute
    DwmExtendFrameIntoClientArea.restype = LONG
    DwmSetWindowAttribute.restype = LONG
    DwmSetWindowAttribute.argtypes = [c_int, DWORD, LPCVOID, DWORD]
    DwmExtendFrameIntoClientArea.argtypes = [c_int, POINTER(MARGINS)]

    def __init__(self):
        # 调用api
        self.SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
        self.SetWindowCompositionAttribute.restype = c_bool
        self.SetWindowCompositionAttribute.argtypes = [
            c_int, POINTER(WINDOWCOMPOSITIONATTRIBDATA)]
        # 初始化结构体
        self.accentPolicy = ACCENT_POLICY()
        self.winCompAttrData = WINDOWCOMPOSITIONATTRIBDATA()
        self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value[0]
        self.winCompAttrData.SizeOfData = sizeof(self.accentPolicy)
        self.winCompAttrData.Data = pointer(self.accentPolicy)
    def setAcrylicEffect(self, hWnd: int, gradientColor: str = 'F2F2F230', isEnableShadow: bool = True, animationId: int = 0):
        """ 给窗口开启Win10的亚克力效果 F2F2F230

        Parameters
        ----------
        hWnd : 窗口句柄\n
        gradientColor : 十六进制亚克力混合色，对应rgba四个分量\n
        isEnableShadow : 控制是否启用窗口阴影\n
        animationId : 控制磨砂动画
        """
        # 亚克力混合色
        gradientColor = gradientColor[6:] + gradientColor[4:6] + \
            gradientColor[2:4] + gradientColor[:2]
        gradientColor = DWORD(int(gradientColor, base=16))
        # 磨砂动画
        animationId = DWORD(animationId)
        # 窗口阴影
        accentFlags = DWORD(0x20 | 0x40 | 0x80 |
                            0x100) if isEnableShadow else DWORD(0)
        self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_ACRYLICBLURBEHIND.value[0]
        self.accentPolicy.GradientColor = gradientColor
        self.accentPolicy.AccentFlags = accentFlags
        self.accentPolicy.AnimationId = animationId 
        # 开启亚克力
        self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))


    def setAeroEffect(self, hWnd: int):
        """ 给窗口开启Aero效果
        Parameter
        ----------
        hWnd : 窗口句柄
        """
        self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value[0]
        # 开启Aero
        self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))

    def setShadowEffect(self, hWnd):
        hWnd = int(hWnd)
        self.DwmSetWindowAttribute(
            hWnd,
            DWMWINDOWATTRIBUTE.DWMWA_NCRENDERING_POLICY.value,
            byref(c_int(DWMNCRENDERINGPOLICY.DWMNCRP_ENABLED.value)),
            4,
        )
        margins = MARGINS(-1, -1, -1, -1)
        self.DwmExtendFrameIntoClientArea(hWnd, byref(margins))

        
    def moveWindow(self, hWnd: int):
        """ 移动窗口
        Parameter
        ----------
        hWnd : 窗口句柄
        """
        win32gui.ReleaseCapture()
        win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
                    win32con.SC_MOVE + win32con.HTCAPTION, 0)
    def addWindowAnimation(self, hWnd):
        """ 还原窗口动画效果

        Parameters
        ----------
        hWnd : int or `sip.voidptr`
            窗口句柄
        """
        hWnd = int(hWnd)
        style = win32gui.GetWindowLong(hWnd, win32con.GWL_STYLE)
        win32gui.SetWindowLong(
            hWnd,
            win32con.GWL_STYLE,
            style
            | win32con.WS_MAXIMIZEBOX
            | win32con.WS_CAPTION
            | win32con.CS_DBLCLKS
            | win32con.WS_THICKFRAME,
        )
            

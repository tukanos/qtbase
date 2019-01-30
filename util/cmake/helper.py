#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the plugins of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import re


def featureName(input: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_]', '_', input)


def map_qt_base_library(lib: str) -> str:
    library_map = {
        'global': 'Qt::Core',  # manually added special case
        'accessibility_support': 'Qt::AccessibilitySupport',
        'androidextras': 'Qt::AndroidExtras',
        'animation': 'Qt::3DAnimation',
        'application-lib': 'Qt::AppManApplication',
        'bluetooth': 'Qt::Bluetooth',
        'bootstrap-dbus': 'Qt::BootstrapDBus',
        'bootstrap': 'Qt::Bootstrap',
        'client': 'Qt::WaylandClient',
        'clipboard_support': 'Qt::ClipboardSupport',
        'common-lib': 'Qt::AppManCommon',
        'compositor': 'Qt::WaylandCompositor',
        'concurrent': 'Qt::Concurrent',
        'container': 'Qt::AxContainer',
        'control': 'Qt::AxServer',
        'core_headers': 'Qt::WebEngineCore',
        'core': 'Qt::Core',
        'coretest': 'Qt::3DCoreTest',
        'crypto-lib': 'Qt::AppManCrypto',
        'dbus': 'Qt::DBus',
        'devicediscovery': 'Qt::DeviceDiscoverySupport',
        'edid': 'Qt::EdidSupport',
        'eglconvenience': 'Qt::EglSupport',
        'eglfsdeviceintegration': 'Qt::EglFSDeviceIntegration',
        'eglfs_kms_support': 'Qt::EglFsKmsSupport',
        'enginio_client': 'Enginio',
        'eventdispatchers': 'Qt::EventDispatcherSupport',
        'extras': 'Qt::3DExtras',
        'fbconvenience': 'Qt::FbSupport',
        'fontdatabase_support': 'Qt::FontDatabaseSupport',
        'gamepad': 'Qt::Gamepad',
        'glxconvenience': 'Qt::GlxSupport',
        'graphics_support': 'Qt::GraphicsSupport',
        'gsttools': 'Qt::MultimediaGstTools',
        'gui': 'Qt::Gui',
        'help': 'Qt::Help',
        'hunspellinputmethod': 'Qt::HunspellInputMethod',
        'input': 'Qt::InputSupport',
        'installer-lib': 'Qt::AppManInstaller',
        'kmsconvenience': 'Qt::KmsSupport',
        'launcher-lib': 'Qt::AppManLauncher',
        'lib': 'Qt::Designer',
        'linuxaccessibility': 'Qt::LinuxAccessibilitySupport',
        'location': 'Qt::Location',
        'logic': 'Qt::3DLogic',
        'macextras': 'Qt::MacExtras',
        'main-lib': 'Qt::AppManMain',
        'manager-lib': 'Qt::AppManManager',
        'monitor-lib': 'Qt::AppManMonitor',
        'multimedia': 'Qt::Multimedia',
        'multimediawidgets': 'Qt::MultimediaWidgets',
        'network': 'Qt::Network',
        'nfc': 'Qt::Nfc',
        'oauth': 'Qt::NetworkAuth',
        'openglextensions': 'Qt::OpenGLExtensions',
        'opengl': 'Qt::OpenGL',
        'package-lib': 'Qt::AppManPackage',
        'packetprotocol': 'Qt::PacketProtocol',
        'particles': 'Qt::QuickParticles',
        'platformcompositor': 'Qt::PlatformCompositorSupport',
        'plugin-interfaces': 'Qt::AppManPluginInterfaces',
        'positioning': 'Qt::Positioning',
        'positioningquick': 'Qt::PositioningQuick',
        'printsupport': 'Qt::PrintSupport',
        'purchasing': 'Qt::Purchasing',
        'qmldebug': 'Qt::QmlDebug',
        'qmldevtools': 'Qt::QmlDevTools',
        'qml': 'Qt::Qml',
        'qmltest': 'Qt::QuickTest',
        'qtmultimediaquicktools': 'Qt::MultimediaQuick',
        'qtzlib': 'Qt::Zlib',
        'quick3danimation': 'Qt::3DQuickAnimation',
        'quick3dextras': 'Qt::3DQuickExtras',
        'quick3dinput': 'Qt::3DQuickInput',
        'quick3d': 'Qt::3DQuick',
        'quick3drender': 'Qt::3DQuickRender',
        'quick3dscene2d': 'Qt::3DQuickScene2D',
        'quickcontrols2': 'Qt::QuickControls2',
        'quick': 'Qt::Quick',
        'quickshapes': 'Qt::QuickShapes',
        'quicktemplates2': 'Qt::QuickTemplates2',
        'quickwidgets': 'Qt::QuickWidgets',
        'render': 'Qt::3DRender',
        'script': 'Qt::Script',
        'scripttools': 'Qt::ScriptTools',
        'sensors': 'Qt::Sensors',
        'serialport': 'Qt::SerialPort',
        'services': 'Qt::ServiceSupport',
        'sql': 'Qt::Sql',
        'svg': 'Qt::Svg',
        'testlib': 'Qt::Test',
        'theme_support': 'Qt::ThemeSupport',
        'service_support': 'Qt::ServiceSupport',
        'eventdispatcher_support': 'Qt::EventDispatcherSupport',
        'edid_support': 'Qt::EdidSupport',
        'tts': 'Qt::TextToSpeech',
        'uiplugin': 'Qt::UiPlugin',
        'uitools': 'Qt::UiTools',
        'virtualkeyboard': 'Qt::VirtualKeyboard',
        'vkconvenience': 'Qt::VulkanSupport',
        'webchannel': 'Qt::WebChannel',
        'webengine': 'Qt::WebEngine',
        'webenginewidgets': 'Qt::WebEngineWidgets',
        'websockets': 'Qt::WebSockets',
        'webview': 'Qt::WebView',
        'widgets': 'Qt::Widgets',
        'window-lib': 'Qt::AppManWindow',
        'windowsuiautomation': 'Qt::WindowsUIAutomationSupport',
        'winextras': 'Qt::WinExtras',
        'x11extras': 'Qt::X11Extras',
        'xcb_qpa_lib': 'Qt::XcbQpa',
        'xmlpatterns': 'Qt::XmlPatterns',
        'xml': 'Qt::Xml',
    }
    return library_map.get(lib, lib)


def map_qt_library(lib: str) -> str:
    private = False
    if lib.endswith('-private'):
        private = True
        lib = lib[:-8]
    mapped = map_qt_base_library(lib)
    if private:
        mapped += 'Private'
    return mapped


platform_mapping = {
    'win32': 'WIN32',
    'unix': 'UNIX',
    'darwin': 'APPLE',
    'linux': 'LINUX',
    'integrity': 'INTEGRITY',
    'qnx': 'QNX',
    'vxworks': 'VXWORKS',
    'hpux': 'HPUX',
    'nacl': 'NACL',
    'android': 'ANDROID',
    'android-embedded': 'ANDROID_EMBEDDED',
    'uikit': 'APPLE_UIKIT',
    'tvos': 'APPLE_TVOS',
    'watchos': 'APPLE_WATCHOS',
    'winrt': 'WINRT',
    'wasm': 'WASM',
    'msvc': 'MSVC',
    'clang': 'CLANG',
    'gcc': 'GCC',
    'icc': 'ICC',
    'intel_icc': 'ICC',
    'osx': 'APPLE_OSX',
    'ios': 'APPLE_IOS',
    'freebsd': 'FREEBSD',
    'openbsd': 'OPENBSD',
    'netbsd': 'NETBSD',
    'haiku': 'HAIKU',
    'netbsd': 'NETBSD',
    'mac': 'APPLE_OSX',
    'macx': 'APPLE_OSX',
    'macos': 'APPLE_OSX',
    'macx-icc': '(APPLE_OSX AND ICC)',
}


def substitute_platform(platform: str) -> str:
    """ Return the qmake platform as cmake platform or the unchanged string. """
    return platform_mapping.get(platform, platform)


libray_mapping = {
    'libdl': '${CMAKE_DL_LIBS}',
    'doubleconversion': 'double-conversion',
    'glib': 'GLIB2::GLIB2',
    'icu': 'ICU::i18n ICU::uc ICU::data',
    'libatomic': 'Atomic',
    'libproxy': 'LibProxy::LibProxy',
    'pcre2': 'PCRE2',
    'librt': 'WrapRt',
    'zlib': 'ZLIB::ZLIB',
    'zstd': 'ZSTD::ZSTD',
}


def substitute_libs(lib: str) -> str:
    return libray_mapping.get(lib, lib)

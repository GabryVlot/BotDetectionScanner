###############################################################################################################
## ManuallyFoundLiterals.py
## Contains repeating detection patterns across different sites
##
## License 2018 Open Source License
## Written By: Gabry Vlot (https://github.com/GabryVlot)
## Project: Detecting Web bot Detecting | BotDetectionScanner (https://github.com/GabryVlot/BotDetectionScanner)
###############################################################################################################

import re

class ManuallyFoundLiterals:

  def __init__(self):
        self.patterns = [
            ('Distil', ['Internet Explorer", "Firefox", "Chrome", "Chromium", "Safari", "MacIntel", "Win32", "Win64", "Windows", "WinNT", "OSX", "Linux", "eval", "O", "Snow Leopard", "Lion/Mountain Lion", "Yosemite", "Mavericks", "d", "XMLHttpRequest", "undefined", "Msxml2.XMLHTTP.6.0", "Msxml2.XMLHTTP.3.0", "Microsoft.XMLHTTP", "length", "substring", "slice", "n", "substr", "", "navigator", "toLowerCase", "a", "h", "replace", "t", "\$2\$1", "platform", "script", "object", "screen", "fonts", "cpu", "addEventListener", "__", "_", "uate", "__web", "__s", "__fx", "_unwrapped", "_script_", "tion", "_fn", "_S", "_IDE", "_Recorder", "_p", "_s", "P", "S", "e", "document", "match", "cache_", "300", "external", "Sequentum", "indexOf", "400", "s", "getAttribute", "documentElement", "500", "web", "600", "700", "POST", "open", "=", "send", "hostname", "location", "___dTL", "getElementById", "nodeName", "INPUT", "value", "audio", "progress", "video", "window", "media", "readystate", "loading", "load", "-", "attachEvent", "onload"']),
            ('Distil_FP', [re.escape('/dist/preview_data.js?token=__TOKEN__&preview_layer_ids'), '"phantomjs", "moatbot", "facebookexternalhit"']),
            ('AsyncDistil', ['\$cdc_asdjflasutopfhvcZLmcfl_", "0", "{"sensor_data":"", "touchmove", "doadma_en", "readyState", ', '_ac = \[', '"Chrome Remote Desktop Viewer", "fonts", "callPhantom", "RTCPeerConnection", "attachEvent", "timezoneOffsetKey", "lang"']),
            ('Distil_AreYouHuman', [re.escape('distil.areyouahuman')]),
            ('Google_ima3', ['ima.bridge.getVideoMetadata', 'webdriver-evaluate', 'webdriver-evaluate-response']),
            ('ShieldSquare', [re.escape('typeof a.__webdriver_script_fn '), re.escape('","j34":"'), re.escape('"undefined" !== typeof a._Selenium_IDE_Recorder')]),
            ('OneSignal', ['OneSignal', '/phantom/i.test\(', 'SlimerJS', 'Bowser', 'squarespace', 'PhantomJS']),
            ('liveintent', ['name: "phantomjs",', '"./internal/default_filter"', '"./processors/stack": 10', 'o = r.appId || "mint-production-appId"']),
            ('webfont_googleAPI', ['a.a.indexOf\("PhantomJS"\)', 'a.a.indexOf\("PlayStation"\)', 'a.a.indexOf\("AdobeAIR"\)', 'WebFont']),
            ('fox_browser', ['function getWindowsVersion\(s\)','/phantom/i.test\(ua\)', '/slimerjs/i.test\(ua\)', 'function detect\(ua\)']),
            ('akamaicdc', ['in document || navigator.webdriver', '\$cdc_asdjflasutopfhvcZLmcfl_', '"callPhantom" in e || /PhantomJS/i.test']),
            ('unknown_obf', [re.escape('var _ = ["opera", "Candara", "", "btoa", "HTMLMenuItemElement", "Vani", "timing", "Malgun Gothic", "navigator", "Calibri", "Opera", "screenX", "Shonar Bangla", "bt", "charCodeAt", "save", "[object SafariRemoteNotification]", "charAt", "1.0", "<div>", "textBaseline", "XMLHttpRequest", "7", "MS PGothic", "Noteworthy", "5.0", "getElementsByClassName", "src", "port", "compute", "Apple SD Gothic Neo", "hostname", "screenY", "Lucida Sans", "product", "AVENIR", "Synchro LET", "getImageData", "Vijaya", "Yu Gothic UI", "outerWidth", "1.4", "Skia", "ieps", "indexedDB", "AcroPDF.PDF.1", "ShockwaveFlash.ShockwaveFlash.7", ".", "number", "toHexStr", "bazadebezolkohpepadr", "Chrome IOS", "/akam/10/pixel_", "object", "exitEarly", "Big Caslon", "18pt Tahoma", "insertBefore", "location", "boolean", "chrome", "}", "Gill Sans", "documentElement", "encodeURIComponent", "screen", "description", "ap", "Safari", "profile", "oscpu", "childNodes", "drawImage", "open", "</div>", "documentMode", "name", "Microsoft.XMLHTTP", "text", "IE", "Monaco", "=", "fonts", "detachEvent", "Mona Lisa Solid ITC TT", "driver", "doNotTrack", "sr", "sessionStorage", "Abadi MT Condensed Light", "2.0", "pageXOffset", "ROTL", "1.9", "now", "ceil", "globalStorage", "urhehlevkedkilrobacf",')]),
            ('CloudFlare', ['window.callPhantom || window._phantom', 'var ambn_cd = document.createElement\("script"\);']),
            ('DoubleClick', [re.escape('b.callPhantom || b._phantom || b.__phantomas || b.Buffer || b.emit || b.spawn || b.webdriver || b.domAutomation')]),
            ('Segmentify_BrowserFP', [re.escape('var r, i = n(/(ipod|iphone|ipad)/i).toLowerCase(),'), re.escape('version: n(/slimerjs\/(\d+(\.\d+)?)/i)')]),
            ('AkamaiBlockBotsUA', [re.escape('/Mozilla\/5\.0\s\(Windows\sNT\s6\.1;\sWOW64;\sTrident\/7\.0;\sSLCC2;\s\.NET\sCLR\s2\.0\.50727;\s\.NET\sCLR\s3\.5\.30729;\s\.NET\sCLR\s3\.0\.30729;\s\.NET4\.0C;\s\.NET4\.0E;\srv:11\.0\)\slike\sGecko/i) || navigator.userAgent.match(/Mozilla\/5\.0\s\(Windows\sNT\s6\.1;\sWOW64;\srv:45\.0\)\sGecko\/20100101\sFirefox\/45\.0/i) || navigator.userAgent.match(/PTST/i)')]),
            ('AkamaiBlockBotsUA2', [re.escape('\sWOW64;'), 'Block bot agents', 'AKM-41']),
            ('akamai?', [re.escape("script[type='text/rocketscript']"),'clnmdecom', '"_selenium","_webdriver","__nightmare","callSelenium"']),
            ('modernizr', ['Modernizr._config.classPrefix', 'Modernizr.addTest', re.escape('Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Min')]),
            ('modernizr(2)', ['Modernizr', re.escape('attachEvent("onbeforeprint"'), 'window.Modernizr']),
            ('Tealium_utag', ['tealium universal tag', 'navigator.plugins.length', 'screen.colorDepth']),
            ('JW Player', ['JW Player','navigator.userAgent', 'navigator.plugins.length']),
            ('SnapABug', ['SnapABug', 'SnapEngage']),
            ('SnapABug2?', ['Please leave us a message. 24/7 support is available for Enterprise and Premium', 'window.ActiveXObject', 'navigator.language']),
            ('fingerprinterjs', ['webglKey', 'hasLiedResolutionKey', 'hasLiedBrowserKey', 'hasLiedOsKey']),
            ('bat.bing.com', ['bat.bing.com', 'addFraudSignals']),
            ('PubAds', ['googletag.impl.pubads', 'window.navigator.plugins', 'ShockwaveFlash.ShockwaveFlash']),
            ('SegmentAnalytics', ['phantomjs-prebuilt', 'karma-phantomjs-launcher']),
            ('WebEngage', ['webengage/ua', re.escape('Google Page Speed Insights", "Site24x7", "PhantomJS"')]),
            ('PixiMedia', ['case"flv":case"f4v":case"mp4":case"ogg":case"ogv":case"webm":case"video":case"dailymotion":return"video"']),
            ('dna', ['HttpConnection.xhrRequest', '__webdriver_evaluate"in document', 'handler.setDNA', 'swfLib.handler.getDNA']),
            ('hotwords', ['hotwords.core.BrowserDetect', '.__phantom']),
            ('uol', [re.escape('PhantomJS-based web perf metrics + monitoring tool'), 'botDetect()']),
            ('metrics', ['document.__webdriver_script_fn', 'WebKitMediaKeyMessageEvent', 'WebGLRenderingContext', 'MozSettingsEvent']),
            ('am15', ['am15.net', 'window._phantom', 'amuid']),
            ('APU', ['_phantom', 'callPhantom', 'zwgsdloasdf', 'apu', 'window.zfgloadedpopup']),
            ('Platform.js', ['Electron', 'PhantomJS', 'cleanupOS', 'Platform.js']),
            ('GoogleAnalytics', [re.escape('www.gstatic.com/attribution/collection/attributiontools'), '.callPhantom', 'window._phantom', 'gtmscript']),
            ('GoogleDoubleClickForPublishers', ['dfpKeyValues', 'isPubDfp', 'webdriver', 'navigator.userAgent', '__phantomas', 'callPhantom', ]),
            ('UnknownBotDetection', ['detectPhantomJs', 'detectSelenium', 'navigator.userAgent', 'callPhantom', 'bots']),
            ('UnknownBotDetection2', ['isPhantomJS', 'isHeadlessChrome', 'navigator.userAgent', 'callPhantom']),
            ('UnknownBotDetection3', ['hasWebdriverAttr', 'webdriver', 'hasPhantom', 'window.callPhantom', 'window._phantom', 'hasDomAutomation', 'window.domAutomation']),
            ('UnknownBotDetection4', [re.escape('version:t(/silk\/(\d+(\.\d+)?)/i)}:/phantom/i.test(e)?n={name:"PhantomJS",phantom:o,version:t(/phantomjs\/(\d+')]),
            ('UnknownBotDetection5', ['webdriver','driver', '5932ec3b29ebe803fd4c2ea4c6466594a8d26e98']),
            ('Wistia', ['Wistia', 'phantomjs']),
            ('Avada', ['avada_lightbox', 'phantomjs', 'wrap_gravity_selects']),
            ('Vendor', [re.escape('chromium|flock|rockmelt|midori|epiphany|silk|skyfire|ovibrowser|bolt|iron|vivaldi|iridium|phantomjs|bowser'), 'headlesschrome', re.escape('navigator.language||navigator.userLanguage||navigator.browserLanguage')]),
            ('CommonUAPattern', [re.escape('chromium|flock|rockmelt|midori|epiphany|silk|skyfire|ovibrowser|bolt|iron|vivaldi|iridium|phantomjs')]),
            ('WistiaHeadlessTampered', ['xhrHasBeenTamperedWith', 'isHeadless', 'phantomjs']),
            ('VAMSOFT', [re.escape('Mozilla/4.0 (Windows NT 6.2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.70 Safari/537.17')]),
            ('MultipleBotPatterns', ['BotPattern', 'PhantomJS', 'DuckDuckBot'])
        ]
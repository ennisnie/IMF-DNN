import PyQt5.QtCore as _mod_PyQt5_QtCore
import PyQt5.QtGui as _mod_PyQt5_QtGui
import PyQt5.QtWidgets as _mod_PyQt5_QtWidgets

class QGraphicsSvgItem(_mod_PyQt5_QtWidgets.QGraphicsObject):
    'QGraphicsSvgItem(parent: QGraphicsItem = None)\nQGraphicsSvgItem(str, parent: QGraphicsItem = None)'
    UserType = 65536
    __class__ = QGraphicsSvgItem
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, parent: QGraphicsItem=None):
        'QGraphicsSvgItem(parent: QGraphicsItem = None)\nQGraphicsSvgItem(str, parent: QGraphicsItem = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtSvg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def acceptDrops(cls, self):
        'acceptDrops(self) -> bool'
        return True
    
    @classmethod
    def acceptHoverEvents(cls, self):
        'acceptHoverEvents(self) -> bool'
        return True
    
    @classmethod
    def acceptTouchEvents(cls, self):
        'acceptTouchEvents(self) -> bool'
        return True
    
    @classmethod
    def acceptedMouseButtons(cls, self):
        'acceptedMouseButtons(self) -> Qt.MouseButtons'
        pass
    
    @classmethod
    def advance(cls, self, int):
        'advance(self, int)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def boundingRect(cls, self):
        'boundingRect(self) -> QRectF'
        pass
    
    @classmethod
    def boundingRegion(cls, self, QTransform):
        'boundingRegion(self, QTransform) -> QRegion'
        pass
    
    @classmethod
    def boundingRegionGranularity(cls, self):
        'boundingRegionGranularity(self) -> float'
        return 1.0
    
    @classmethod
    def cacheMode(cls, self):
        'cacheMode(self) -> QGraphicsItem.CacheMode'
        pass
    
    @classmethod
    def childEvent(cls, self, QChildEvent):
        'childEvent(self, QChildEvent)'
        pass
    
    @classmethod
    def childItems(cls, self):
        'childItems(self) -> List[QGraphicsItem]'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def childrenBoundingRect(cls, self):
        'childrenBoundingRect(self) -> QRectF'
        pass
    
    @classmethod
    def clearFocus(cls, self):
        'clearFocus(self)'
        pass
    
    @classmethod
    def clipPath(cls, self):
        'clipPath(self) -> QPainterPath'
        pass
    
    @classmethod
    def collidesWithItem(cls, self, QGraphicsItem, mode: Qt.ItemSelectionMode=Qt.IntersectsItemShape):
        'collidesWithItem(self, QGraphicsItem, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool'
        return True
    
    @classmethod
    def collidesWithPath(cls, self, QPainterPath, mode: Qt.ItemSelectionMode=Qt.IntersectsItemShape):
        'collidesWithPath(self, QPainterPath, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> bool'
        return True
    
    @classmethod
    def collidingItems(cls, self, mode: Qt.ItemSelectionMode=Qt.IntersectsItemShape):
        'collidingItems(self, mode: Qt.ItemSelectionMode = Qt.IntersectsItemShape) -> object'
        pass
    
    @classmethod
    def commonAncestorItem(cls, self, QGraphicsItem):
        'commonAncestorItem(self, QGraphicsItem) -> QGraphicsItem'
        pass
    
    @classmethod
    def connectNotify(cls, self, QMetaMethod):
        'connectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def contains(cls, self, UnionQPointF=None, QPoint=None):
        'contains(self, Union[QPointF, QPoint]) -> bool'
        return True
    
    @classmethod
    def contextMenuEvent(cls, self, QGraphicsSceneContextMenuEvent):
        'contextMenuEvent(self, QGraphicsSceneContextMenuEvent)'
        pass
    
    @classmethod
    def cursor(cls, self):
        'cursor(self) -> QCursor'
        pass
    
    @classmethod
    def customEvent(cls, self, QEvent):
        'customEvent(self, QEvent)'
        pass
    
    @classmethod
    def data(cls, self, int):
        'data(self, int) -> Any'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def deviceTransform(cls, self, QTransform):
        'deviceTransform(self, QTransform) -> QTransform'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls, self, QMetaMethod):
        'disconnectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def dragEnterEvent(cls, self, QGraphicsSceneDragDropEvent):
        'dragEnterEvent(self, QGraphicsSceneDragDropEvent)'
        pass
    
    @classmethod
    def dragLeaveEvent(cls, self, QGraphicsSceneDragDropEvent):
        'dragLeaveEvent(self, QGraphicsSceneDragDropEvent)'
        pass
    
    @classmethod
    def dragMoveEvent(cls, self, QGraphicsSceneDragDropEvent):
        'dragMoveEvent(self, QGraphicsSceneDragDropEvent)'
        pass
    
    @classmethod
    def dropEvent(cls, self, QGraphicsSceneDragDropEvent):
        'dropEvent(self, QGraphicsSceneDragDropEvent)'
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def effectiveOpacity(cls, self):
        'effectiveOpacity(self) -> float'
        return 1.0
    
    @classmethod
    def elementId(cls, self):
        'elementId(self) -> str'
        return ''
    
    @classmethod
    def ensureVisible(cls, self, float, float_, float_1, float_2, xMargin: int=50, yMargin: int=50):
        'ensureVisible(self, rect: QRectF = QRectF(), xMargin: int = 50, yMargin: int = 50)\nensureVisible(self, float, float, float, float, xMargin: int = 50, yMargin: int = 50)'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def filtersChildEvents(cls, self):
        'filtersChildEvents(self) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self):
        'flags(self) -> QGraphicsItem.GraphicsItemFlags'
        pass
    
    @classmethod
    def focusInEvent(cls, self, QFocusEvent):
        'focusInEvent(self, QFocusEvent)'
        pass
    
    @classmethod
    def focusItem(cls, self):
        'focusItem(self) -> QGraphicsItem'
        pass
    
    @classmethod
    def focusOutEvent(cls, self, QFocusEvent):
        'focusOutEvent(self, QFocusEvent)'
        pass
    
    @classmethod
    def focusProxy(cls, self):
        'focusProxy(self) -> QGraphicsItem'
        pass
    
    @classmethod
    def grabGesture(cls, self, QtGestureType, flags: Union[Qt.GestureFlags,Qt.GestureFlag]=Qt.GestureFlags()):
        'grabGesture(self, Qt.GestureType, flags: Union[Qt.GestureFlags, Qt.GestureFlag] = Qt.GestureFlags())'
        pass
    
    @classmethod
    def grabKeyboard(cls, self):
        'grabKeyboard(self)'
        pass
    
    @classmethod
    def grabMouse(cls, self):
        'grabMouse(self)'
        pass
    
    @classmethod
    def graphicsEffect(cls, self):
        'graphicsEffect(self) -> QGraphicsEffect'
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QGraphicsItemGroup'
        pass
    
    @classmethod
    def hasCursor(cls, self):
        'hasCursor(self) -> bool'
        return True
    
    @classmethod
    def hasFocus(cls, self):
        'hasFocus(self) -> bool'
        return True
    
    @classmethod
    def hide(cls, self):
        'hide(self)'
        pass
    
    @classmethod
    def hoverEnterEvent(cls, self, QGraphicsSceneHoverEvent):
        'hoverEnterEvent(self, QGraphicsSceneHoverEvent)'
        pass
    
    @classmethod
    def hoverLeaveEvent(cls, self, QGraphicsSceneHoverEvent):
        'hoverLeaveEvent(self, QGraphicsSceneHoverEvent)'
        pass
    
    @classmethod
    def hoverMoveEvent(cls, self, QGraphicsSceneHoverEvent):
        'hoverMoveEvent(self, QGraphicsSceneHoverEvent)'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def inputMethodEvent(cls, self, QInputMethodEvent):
        'inputMethodEvent(self, QInputMethodEvent)'
        pass
    
    @classmethod
    def inputMethodHints(cls, self):
        'inputMethodHints(self) -> Qt.InputMethodHints'
        pass
    
    @classmethod
    def inputMethodQuery(cls, self, QtInputMethodQuery):
        'inputMethodQuery(self, Qt.InputMethodQuery) -> Any'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def installSceneEventFilter(cls, self, QGraphicsItem):
        'installSceneEventFilter(self, QGraphicsItem)'
        pass
    
    @classmethod
    def isActive(cls, self):
        'isActive(self) -> bool'
        return True
    
    @classmethod
    def isAncestorOf(cls, self, QGraphicsItem):
        'isAncestorOf(self, QGraphicsItem) -> bool'
        return True
    
    @classmethod
    def isBlockedByModalPanel(cls, self):
        'isBlockedByModalPanel(self) -> Tuple[bool, QGraphicsItem]'
        pass
    
    @classmethod
    def isClipped(cls, self):
        'isClipped(self) -> bool'
        return True
    
    @classmethod
    def isEnabled(cls, self):
        'isEnabled(self) -> bool'
        return True
    
    @classmethod
    def isObscured(cls, self, float, float_, float_1, float_2):
        'isObscured(self, rect: QRectF = QRectF()) -> bool\nisObscured(self, float, float, float, float) -> bool'
        return True
    
    @classmethod
    def isObscuredBy(cls, self, QGraphicsItem):
        'isObscuredBy(self, QGraphicsItem) -> bool'
        return True
    
    @classmethod
    def isPanel(cls, self):
        'isPanel(self) -> bool'
        return True
    
    @classmethod
    def isSelected(cls, self):
        'isSelected(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls, self, QMetaMethod):
        'isSignalConnected(self, QMetaMethod) -> bool'
        return True
    
    @classmethod
    def isUnderMouse(cls, self):
        'isUnderMouse(self) -> bool'
        return True
    
    @classmethod
    def isVisible(cls, self):
        'isVisible(self) -> bool'
        return True
    
    @classmethod
    def isVisibleTo(cls, self, QGraphicsItem):
        'isVisibleTo(self, QGraphicsItem) -> bool'
        return True
    
    @classmethod
    def isWidget(cls, self):
        'isWidget(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindow(cls, self):
        'isWindow(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemChange(cls, self, QGraphicsItemGraphicsItemChange, Any):
        'itemChange(self, QGraphicsItem.GraphicsItemChange, Any) -> Any'
        pass
    
    @classmethod
    def itemTransform(cls, self, QGraphicsItem):
        'itemTransform(self, QGraphicsItem) -> Tuple[QTransform, bool]'
        pass
    
    @classmethod
    def keyPressEvent(cls, self, QKeyEvent):
        'keyPressEvent(self, QKeyEvent)'
        pass
    
    @classmethod
    def keyReleaseEvent(cls, self, QKeyEvent):
        'keyReleaseEvent(self, QKeyEvent)'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def mapFromItem(cls, self, QGraphicsItem, float, float_, float_1, float_2):
        'mapFromItem(self, QGraphicsItem, Union[QPointF, QPoint]) -> QPointF\nmapFromItem(self, QGraphicsItem, QRectF) -> QPolygonF\nmapFromItem(self, QGraphicsItem, QPolygonF) -> QPolygonF\nmapFromItem(self, QGraphicsItem, QPainterPath) -> QPainterPath\nmapFromItem(self, QGraphicsItem, float, float) -> QPointF\nmapFromItem(self, QGraphicsItem, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def mapFromParent(cls, self, float, float_, float_1, float_2):
        'mapFromParent(self, Union[QPointF, QPoint]) -> QPointF\nmapFromParent(self, QRectF) -> QPolygonF\nmapFromParent(self, QPolygonF) -> QPolygonF\nmapFromParent(self, QPainterPath) -> QPainterPath\nmapFromParent(self, float, float) -> QPointF\nmapFromParent(self, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def mapFromScene(cls, self, float, float_, float_1, float_2):
        'mapFromScene(self, Union[QPointF, QPoint]) -> QPointF\nmapFromScene(self, QRectF) -> QPolygonF\nmapFromScene(self, QPolygonF) -> QPolygonF\nmapFromScene(self, QPainterPath) -> QPainterPath\nmapFromScene(self, float, float) -> QPointF\nmapFromScene(self, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def mapRectFromItem(cls, self, QGraphicsItem, float, float_, float_1, float_2):
        'mapRectFromItem(self, QGraphicsItem, QRectF) -> QRectF\nmapRectFromItem(self, QGraphicsItem, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapRectFromParent(cls, self, float, float_, float_1, float_2):
        'mapRectFromParent(self, QRectF) -> QRectF\nmapRectFromParent(self, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapRectFromScene(cls, self, float, float_, float_1, float_2):
        'mapRectFromScene(self, QRectF) -> QRectF\nmapRectFromScene(self, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapRectToItem(cls, self, QGraphicsItem, float, float_, float_1, float_2):
        'mapRectToItem(self, QGraphicsItem, QRectF) -> QRectF\nmapRectToItem(self, QGraphicsItem, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapRectToParent(cls, self, float, float_, float_1, float_2):
        'mapRectToParent(self, QRectF) -> QRectF\nmapRectToParent(self, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapRectToScene(cls, self, float, float_, float_1, float_2):
        'mapRectToScene(self, QRectF) -> QRectF\nmapRectToScene(self, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def mapToItem(cls, self, QGraphicsItem, float, float_, float_1, float_2):
        'mapToItem(self, QGraphicsItem, Union[QPointF, QPoint]) -> QPointF\nmapToItem(self, QGraphicsItem, QRectF) -> QPolygonF\nmapToItem(self, QGraphicsItem, QPolygonF) -> QPolygonF\nmapToItem(self, QGraphicsItem, QPainterPath) -> QPainterPath\nmapToItem(self, QGraphicsItem, float, float) -> QPointF\nmapToItem(self, QGraphicsItem, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def mapToParent(cls, self, float, float_, float_1, float_2):
        'mapToParent(self, Union[QPointF, QPoint]) -> QPointF\nmapToParent(self, QRectF) -> QPolygonF\nmapToParent(self, QPolygonF) -> QPolygonF\nmapToParent(self, QPainterPath) -> QPainterPath\nmapToParent(self, float, float) -> QPointF\nmapToParent(self, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def mapToScene(cls, self, float, float_, float_1, float_2):
        'mapToScene(self, Union[QPointF, QPoint]) -> QPointF\nmapToScene(self, QRectF) -> QPolygonF\nmapToScene(self, QPolygonF) -> QPolygonF\nmapToScene(self, QPainterPath) -> QPainterPath\nmapToScene(self, float, float) -> QPointF\nmapToScene(self, float, float, float, float) -> QPolygonF'
        pass
    
    @classmethod
    def maximumCacheSize(cls, self):
        'maximumCacheSize(self) -> QSize'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mouseDoubleClickEvent(cls, self, QGraphicsSceneMouseEvent):
        'mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent)'
        pass
    
    @classmethod
    def mouseMoveEvent(cls, self, QGraphicsSceneMouseEvent):
        'mouseMoveEvent(self, QGraphicsSceneMouseEvent)'
        pass
    
    @classmethod
    def mousePressEvent(cls, self, QGraphicsSceneMouseEvent):
        'mousePressEvent(self, QGraphicsSceneMouseEvent)'
        pass
    
    @classmethod
    def mouseReleaseEvent(cls, self, QGraphicsSceneMouseEvent):
        'mouseReleaseEvent(self, QGraphicsSceneMouseEvent)'
        pass
    
    @classmethod
    def moveBy(cls, self, float, float_):
        'moveBy(self, float, float)'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def opacity(cls, self):
        'opacity(self) -> float'
        return 1.0
    
    @classmethod
    def opaqueArea(cls, self):
        'opaqueArea(self) -> QPainterPath'
        pass
    
    @classmethod
    def paint(cls, self, QPainter, QStyleOptionGraphicsItem, widget: QWidget=None):
        'paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None)'
        pass
    
    @classmethod
    def panel(cls, self):
        'panel(self) -> QGraphicsItem'
        pass
    
    @classmethod
    def panelModality(cls, self):
        'panelModality(self) -> QGraphicsItem.PanelModality'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentItem(cls, self):
        'parentItem(self) -> QGraphicsItem'
        pass
    
    @classmethod
    def parentObject(cls, self):
        'parentObject(self) -> QGraphicsObject'
        pass
    
    @classmethod
    def parentWidget(cls, self):
        'parentWidget(self) -> QGraphicsWidget'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> QPointF'
        pass
    
    @classmethod
    def prepareGeometryChange(cls, self):
        'prepareGeometryChange(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls, self, PYQT_SIGNAL):
        'receivers(self, PYQT_SIGNAL) -> int'
        return 1
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeSceneEventFilter(cls, self, QGraphicsItem):
        'removeSceneEventFilter(self, QGraphicsItem)'
        pass
    
    @classmethod
    def renderer(cls, self):
        'renderer(self) -> QSvgRenderer'
        pass
    
    @classmethod
    def resetTransform(cls, self):
        'resetTransform(self)'
        pass
    
    @classmethod
    def rotation(cls, self):
        'rotation(self) -> float'
        return 1.0
    
    @classmethod
    def scale(cls, self):
        'scale(self) -> float'
        return 1.0
    
    @classmethod
    def scene(cls, self):
        'scene(self) -> QGraphicsScene'
        pass
    
    @classmethod
    def sceneBoundingRect(cls, self):
        'sceneBoundingRect(self) -> QRectF'
        pass
    
    @classmethod
    def sceneEvent(cls, self, QEvent):
        'sceneEvent(self, QEvent) -> bool'
        return True
    
    @classmethod
    def sceneEventFilter(cls, self, QGraphicsItem, QEvent):
        'sceneEventFilter(self, QGraphicsItem, QEvent) -> bool'
        return True
    
    @classmethod
    def scenePos(cls, self):
        'scenePos(self) -> QPointF'
        pass
    
    @classmethod
    def sceneTransform(cls, self):
        'sceneTransform(self) -> QTransform'
        pass
    
    @classmethod
    def scroll(cls, self, float, float_, rect: QRectF=QRectF()):
        'scroll(self, float, float, rect: QRectF = QRectF())'
        pass
    
    @classmethod
    def sender(cls, self):
        'sender(self) -> QObject'
        pass
    
    @classmethod
    def senderSignalIndex(cls, self):
        'senderSignalIndex(self) -> int'
        return 1
    
    @classmethod
    def setAcceptDrops(cls, self, bool):
        'setAcceptDrops(self, bool)'
        pass
    
    @classmethod
    def setAcceptHoverEvents(cls, self, bool):
        'setAcceptHoverEvents(self, bool)'
        pass
    
    @classmethod
    def setAcceptTouchEvents(cls, self, bool):
        'setAcceptTouchEvents(self, bool)'
        pass
    
    @classmethod
    def setAcceptedMouseButtons(cls, self, UnionQtMouseButtons=None, QtMouseButton=None):
        'setAcceptedMouseButtons(self, Union[Qt.MouseButtons, Qt.MouseButton])'
        pass
    
    @classmethod
    def setActive(cls, self, bool):
        'setActive(self, bool)'
        pass
    
    @classmethod
    def setBoundingRegionGranularity(cls, self, float):
        'setBoundingRegionGranularity(self, float)'
        pass
    
    @classmethod
    def setCacheMode(cls, self, QGraphicsItemCacheMode, logicalCacheSize: QSize=QSize()):
        'setCacheMode(self, QGraphicsItem.CacheMode, logicalCacheSize: QSize = QSize())'
        pass
    
    @classmethod
    def setCursor(cls, self, UnionQCursor=None, QtCursorShape=None):
        'setCursor(self, Union[QCursor, Qt.CursorShape])'
        pass
    
    @classmethod
    def setData(cls, self, int, Any):
        'setData(self, int, Any)'
        pass
    
    @classmethod
    def setElementId(cls, self, str):
        'setElementId(self, str)'
        pass
    
    @classmethod
    def setEnabled(cls, self, bool):
        'setEnabled(self, bool)'
        pass
    
    @classmethod
    def setFiltersChildEvents(cls, self, bool):
        'setFiltersChildEvents(self, bool)'
        pass
    
    @classmethod
    def setFlag(cls, self, QGraphicsItemGraphicsItemFlag, enabled: bool=True):
        'setFlag(self, QGraphicsItem.GraphicsItemFlag, enabled: bool = True)'
        pass
    
    @classmethod
    def setFlags(cls, self, UnionQGraphicsItemGraphicsItemFlags=None, QGraphicsItemGraphicsItemFlag=None):
        'setFlags(self, Union[QGraphicsItem.GraphicsItemFlags, QGraphicsItem.GraphicsItemFlag])'
        pass
    
    @classmethod
    def setFocus(cls, self, focusReason: Qt.FocusReason=Qt.OtherFocusReason):
        'setFocus(self, focusReason: Qt.FocusReason = Qt.OtherFocusReason)'
        pass
    
    @classmethod
    def setFocusProxy(cls, self, QGraphicsItem):
        'setFocusProxy(self, QGraphicsItem)'
        pass
    
    @classmethod
    def setGraphicsEffect(cls, self, QGraphicsEffect):
        'setGraphicsEffect(self, QGraphicsEffect)'
        pass
    
    @classmethod
    def setGroup(cls, self, QGraphicsItemGroup):
        'setGroup(self, QGraphicsItemGroup)'
        pass
    
    @classmethod
    def setInputMethodHints(cls, self, UnionQtInputMethodHints=None, QtInputMethodHint=None):
        'setInputMethodHints(self, Union[Qt.InputMethodHints, Qt.InputMethodHint])'
        pass
    
    @classmethod
    def setMaximumCacheSize(cls, self, QSize):
        'setMaximumCacheSize(self, QSize)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpacity(cls, self, float):
        'setOpacity(self, float)'
        pass
    
    @classmethod
    def setPanelModality(cls, self, QGraphicsItemPanelModality):
        'setPanelModality(self, QGraphicsItem.PanelModality)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setParentItem(cls, self, QGraphicsItem):
        'setParentItem(self, QGraphicsItem)'
        pass
    
    @classmethod
    def setPos(cls, self, UnionQPointF=None, QPoint=None):
        'setPos(self, Union[QPointF, QPoint])\nsetPos(self, float, float)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setRotation(cls, self, float):
        'setRotation(self, float)'
        pass
    
    @classmethod
    def setScale(cls, self, float):
        'setScale(self, float)'
        pass
    
    @classmethod
    def setSelected(cls, self, bool):
        'setSelected(self, bool)'
        pass
    
    @classmethod
    def setSharedRenderer(cls, self, QSvgRenderer):
        'setSharedRenderer(self, QSvgRenderer)'
        pass
    
    @classmethod
    def setToolTip(cls, self, str):
        'setToolTip(self, str)'
        pass
    
    @classmethod
    def setTransform(cls, self, QTransform, combine: bool=False):
        'setTransform(self, QTransform, combine: bool = False)'
        pass
    
    @classmethod
    def setTransformOriginPoint(cls, self, UnionQPointF=None, QPoint=None):
        'setTransformOriginPoint(self, Union[QPointF, QPoint])\nsetTransformOriginPoint(self, float, float)'
        pass
    
    @classmethod
    def setTransformations(cls, self, IterableQGraphicsTransform=None):
        'setTransformations(self, Iterable[QGraphicsTransform])'
        pass
    
    @classmethod
    def setVisible(cls, self, bool):
        'setVisible(self, bool)'
        pass
    
    @classmethod
    def setX(cls, self, float):
        'setX(self, float)'
        pass
    
    @classmethod
    def setY(cls, self, float):
        'setY(self, float)'
        pass
    
    @classmethod
    def setZValue(cls, self, float):
        'setZValue(self, float)'
        pass
    
    @classmethod
    def shape(cls, self):
        'shape(self) -> QPainterPath'
        pass
    
    @classmethod
    def show(cls, self):
        'show(self)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def stackBefore(cls, self, QGraphicsItem):
        'stackBefore(self, QGraphicsItem)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = _mod_PyQt5_QtCore.QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def toGraphicsObject(cls, self):
        'toGraphicsObject(self) -> QGraphicsObject'
        pass
    
    @classmethod
    def toolTip(cls, self):
        'toolTip(self) -> str'
        return ''
    
    @classmethod
    def topLevelItem(cls, self):
        'topLevelItem(self) -> QGraphicsItem'
        pass
    
    @classmethod
    def topLevelWidget(cls, self):
        'topLevelWidget(self) -> QGraphicsWidget'
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transform(cls, self):
        'transform(self) -> QTransform'
        pass
    
    @classmethod
    def transformOriginPoint(cls, self):
        'transformOriginPoint(self) -> QPointF'
        pass
    
    @classmethod
    def transformations(cls, self):
        'transformations(self) -> object'
        pass
    
    @classmethod
    def type(cls, self):
        'type(self) -> int'
        return 1
    
    @classmethod
    def ungrabGesture(cls, self, QtGestureType):
        'ungrabGesture(self, Qt.GestureType)'
        pass
    
    @classmethod
    def ungrabKeyboard(cls, self):
        'ungrabKeyboard(self)'
        pass
    
    @classmethod
    def ungrabMouse(cls, self):
        'ungrabMouse(self)'
        pass
    
    @classmethod
    def unsetCursor(cls, self):
        'unsetCursor(self)'
        pass
    
    @classmethod
    def update(cls, self, float, float_, float_1, float_2):
        'update(self, rect: QRectF = QRectF())\nupdate(self, float, float, float, float)'
        pass
    
    @classmethod
    def updateMicroFocus(cls, self):
        'updateMicroFocus(self)'
        pass
    
    @classmethod
    def wheelEvent(cls, self, QGraphicsSceneWheelEvent):
        'wheelEvent(self, QGraphicsSceneWheelEvent)'
        pass
    
    @classmethod
    def window(cls, self):
        'window(self) -> QGraphicsWidget'
        pass
    
    @classmethod
    def x(cls, self):
        'x(self) -> float'
        return 1.0
    
    @classmethod
    def y(cls, self):
        'y(self) -> float'
        return 1.0
    
    @classmethod
    def zValue(cls, self):
        'zValue(self) -> float'
        return 1.0
    

class QSvgGenerator(_mod_PyQt5_QtGui.QPaintDevice):
    'QSvgGenerator()'
    __class__ = QSvgGenerator
    __dict__ = {}
    def __init__(self):
        'QSvgGenerator()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtSvg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def colorCount(cls, self):
        'colorCount(self) -> int'
        return 1
    
    @classmethod
    def depth(cls, self):
        'depth(self) -> int'
        return 1
    
    @classmethod
    def description(cls, self):
        'description(self) -> str'
        return ''
    
    @classmethod
    def devicePixelRatio(cls, self):
        'devicePixelRatio(self) -> int'
        return 1
    
    @classmethod
    def devicePixelRatioF(cls, self):
        'devicePixelRatioF(self) -> float'
        return 1.0
    
    @classmethod
    def devicePixelRatioFScale(cls):
        'devicePixelRatioFScale() -> float'
        return 1.0
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def height(cls, self):
        'height(self) -> int'
        return 1
    
    @classmethod
    def heightMM(cls, self):
        'heightMM(self) -> int'
        return 1
    
    @classmethod
    def logicalDpiX(cls, self):
        'logicalDpiX(self) -> int'
        return 1
    
    @classmethod
    def logicalDpiY(cls, self):
        'logicalDpiY(self) -> int'
        return 1
    
    @classmethod
    def metric(cls, self, QPaintDevicePaintDeviceMetric):
        'metric(self, QPaintDevice.PaintDeviceMetric) -> int'
        return 1
    
    @classmethod
    def outputDevice(cls, self):
        'outputDevice(self) -> QIODevice'
        pass
    
    @classmethod
    def paintEngine(cls, self):
        'paintEngine(self) -> QPaintEngine'
        pass
    
    @classmethod
    def paintingActive(cls, self):
        'paintingActive(self) -> bool'
        return True
    
    @classmethod
    def physicalDpiX(cls, self):
        'physicalDpiX(self) -> int'
        return 1
    
    @classmethod
    def physicalDpiY(cls, self):
        'physicalDpiY(self) -> int'
        return 1
    
    @classmethod
    def resolution(cls, self):
        'resolution(self) -> int'
        return 1
    
    @classmethod
    def setDescription(cls, self, str):
        'setDescription(self, str)'
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setOutputDevice(cls, self, QIODevice):
        'setOutputDevice(self, QIODevice)'
        pass
    
    @classmethod
    def setResolution(cls, self, int):
        'setResolution(self, int)'
        pass
    
    @classmethod
    def setSize(cls, self, QSize):
        'setSize(self, QSize)'
        pass
    
    @classmethod
    def setTitle(cls, self, str):
        'setTitle(self, str)'
        pass
    
    @classmethod
    def setViewBox(cls, self, QRectF):
        'setViewBox(self, QRect)\nsetViewBox(self, QRectF)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> QSize'
        pass
    
    @classmethod
    def title(cls, self):
        'title(self) -> str'
        return ''
    
    @classmethod
    def viewBox(cls, self):
        'viewBox(self) -> QRect'
        pass
    
    @classmethod
    def viewBoxF(cls, self):
        'viewBoxF(self) -> QRectF'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> int'
        return 1
    
    @classmethod
    def widthMM(cls, self):
        'widthMM(self) -> int'
        return 1
    

class QSvgRenderer(_mod_PyQt5_QtCore.QObject):
    'QSvgRenderer(parent: QObject = None)\nQSvgRenderer(str, parent: QObject = None)\nQSvgRenderer(Union[QByteArray, bytes, bytearray], parent: QObject = None)\nQSvgRenderer(QXmlStreamReader, parent: QObject = None)'
    __class__ = QSvgRenderer
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None, parent: QObject=None):
        'QSvgRenderer(parent: QObject = None)\nQSvgRenderer(str, parent: QObject = None)\nQSvgRenderer(Union[QByteArray, bytes, bytearray], parent: QObject = None)\nQSvgRenderer(QXmlStreamReader, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtSvg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def animated(cls, self):
        'animated(self) -> bool'
        return True
    
    @classmethod
    def animationDuration(cls, self):
        'animationDuration(self) -> int'
        return 1
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def boundsOnElement(cls, self, str):
        'boundsOnElement(self, str) -> QRectF'
        pass
    
    @classmethod
    def childEvent(cls, self, QChildEvent):
        'childEvent(self, QChildEvent)'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls, self, QMetaMethod):
        'connectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def currentFrame(cls, self):
        'currentFrame(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls, self, QEvent):
        'customEvent(self, QEvent)'
        pass
    
    @classmethod
    def defaultSize(cls, self):
        'defaultSize(self) -> QSize'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls, self, QMetaMethod):
        'disconnectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def elementExists(cls, self, str):
        'elementExists(self, str) -> bool'
        return True
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def framesPerSecond(cls, self):
        'framesPerSecond(self) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls, self, QMetaMethod):
        'isSignalConnected(self, QMetaMethod) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def load(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'load(self, str) -> bool\nload(self, Union[QByteArray, bytes, bytearray]) -> bool\nload(self, QXmlStreamReader) -> bool'
        return True
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls, self, PYQT_SIGNAL):
        'receivers(self, PYQT_SIGNAL) -> int'
        return 1
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def render(cls, self, QPainter, str, bounds: QRectF=QRectF()):
        'render(self, QPainter)\nrender(self, QPainter, QRectF)\nrender(self, QPainter, str, bounds: QRectF = QRectF())'
        pass
    
    def repaintNeeded(self):
        'repaintNeeded(self) [signal]'
        pass
    
    @classmethod
    def sender(cls, self):
        'sender(self) -> QObject'
        pass
    
    @classmethod
    def senderSignalIndex(cls, self):
        'senderSignalIndex(self) -> int'
        return 1
    
    @classmethod
    def setCurrentFrame(cls, self, int):
        'setCurrentFrame(self, int)'
        pass
    
    @classmethod
    def setFramesPerSecond(cls, self, int):
        'setFramesPerSecond(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setViewBox(cls, self, QRectF):
        'setViewBox(self, QRect)\nsetViewBox(self, QRectF)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = _mod_PyQt5_QtCore.QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def viewBox(cls, self):
        'viewBox(self) -> QRect'
        pass
    
    @classmethod
    def viewBoxF(cls, self):
        'viewBoxF(self) -> QRectF'
        pass
    

class QSvgWidget(_mod_PyQt5_QtWidgets.QWidget):
    'QSvgWidget(parent: QWidget = None)\nQSvgWidget(str, parent: QWidget = None)'
    __class__ = QSvgWidget
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, parent: QWidget=None):
        'QSvgWidget(parent: QWidget = None)\nQSvgWidget(str, parent: QWidget = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtSvg'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def acceptDrops(cls, self):
        'acceptDrops(self) -> bool'
        return True
    
    @classmethod
    def accessibleDescription(cls, self):
        'accessibleDescription(self) -> str'
        return ''
    
    @classmethod
    def accessibleName(cls, self):
        'accessibleName(self) -> str'
        return ''
    
    @classmethod
    def actionEvent(cls, self, QActionEvent):
        'actionEvent(self, QActionEvent)'
        pass
    
    @classmethod
    def actions(cls, self):
        'actions(self) -> List[QAction]'
        pass
    
    @classmethod
    def activateWindow(cls, self):
        'activateWindow(self)'
        pass
    
    @classmethod
    def addAction(cls, self, QAction):
        'addAction(self, QAction)'
        pass
    
    @classmethod
    def addActions(cls, self, object):
        'addActions(self, object)'
        pass
    
    @classmethod
    def adjustSize(cls, self):
        'adjustSize(self)'
        pass
    
    @classmethod
    def autoFillBackground(cls, self):
        'autoFillBackground(self) -> bool'
        return True
    
    @classmethod
    def backgroundRole(cls, self):
        'backgroundRole(self) -> QPalette.ColorRole'
        pass
    
    @classmethod
    def baseSize(cls, self):
        'baseSize(self) -> QSize'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def changeEvent(cls, self, QEvent):
        'changeEvent(self, QEvent)'
        pass
    
    @classmethod
    def childAt(cls, self, int, int_):
        'childAt(self, QPoint) -> QWidget\nchildAt(self, int, int) -> QWidget'
        pass
    
    @classmethod
    def childEvent(cls, self, QChildEvent):
        'childEvent(self, QChildEvent)'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def childrenRect(cls, self):
        'childrenRect(self) -> QRect'
        pass
    
    @classmethod
    def childrenRegion(cls, self):
        'childrenRegion(self) -> QRegion'
        pass
    
    @classmethod
    def clearFocus(cls, self):
        'clearFocus(self)'
        pass
    
    @classmethod
    def clearMask(cls, self):
        'clearMask(self)'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self) -> bool'
        return True
    
    @classmethod
    def closeEvent(cls, self, QCloseEvent):
        'closeEvent(self, QCloseEvent)'
        pass
    
    @classmethod
    def colorCount(cls, self):
        'colorCount(self) -> int'
        return 1
    
    @classmethod
    def connectNotify(cls, self, QMetaMethod):
        'connectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def contentsMargins(cls, self):
        'contentsMargins(self) -> QMargins'
        pass
    
    @classmethod
    def contentsRect(cls, self):
        'contentsRect(self) -> QRect'
        pass
    
    @classmethod
    def contextMenuEvent(cls, self, QContextMenuEvent):
        'contextMenuEvent(self, QContextMenuEvent)'
        pass
    
    @classmethod
    def contextMenuPolicy(cls, self):
        'contextMenuPolicy(self) -> Qt.ContextMenuPolicy'
        pass
    
    @classmethod
    def create(cls, self, window: sip.voidptr=0, initializeWindow: bool=True, destroyOldWindow: bool=True):
        'create(self, window: sip.voidptr = 0, initializeWindow: bool = True, destroyOldWindow: bool = True)'
        pass
    
    @classmethod
    def createWindowContainer(cls, QWindow, parent: QWidget=None, flags: Union[Qt.WindowFlags,Qt.WindowType]=0):
        'createWindowContainer(QWindow, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = 0) -> QWidget'
        pass
    
    @classmethod
    def cursor(cls, self):
        'cursor(self) -> QCursor'
        pass
    
    @classmethod
    def customEvent(cls, self, QEvent):
        'customEvent(self, QEvent)'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def depth(cls, self):
        'depth(self) -> int'
        return 1
    
    @classmethod
    def destroy(cls, self, destroyWindow: bool=True, destroySubWindows: bool=True):
        'destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True)'
        pass
    
    @classmethod
    def devType(cls, self):
        'devType(self) -> int'
        return 1
    
    @classmethod
    def devicePixelRatio(cls, self):
        'devicePixelRatio(self) -> int'
        return 1
    
    @classmethod
    def devicePixelRatioF(cls, self):
        'devicePixelRatioF(self) -> float'
        return 1.0
    
    @classmethod
    def devicePixelRatioFScale(cls):
        'devicePixelRatioFScale() -> float'
        return 1.0
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls, self, QMetaMethod):
        'disconnectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def dragEnterEvent(cls, self, QDragEnterEvent):
        'dragEnterEvent(self, QDragEnterEvent)'
        pass
    
    @classmethod
    def dragLeaveEvent(cls, self, QDragLeaveEvent):
        'dragLeaveEvent(self, QDragLeaveEvent)'
        pass
    
    @classmethod
    def dragMoveEvent(cls, self, QDragMoveEvent):
        'dragMoveEvent(self, QDragMoveEvent)'
        pass
    
    @classmethod
    def dropEvent(cls, self, QDropEvent):
        'dropEvent(self, QDropEvent)'
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def effectiveWinId(cls, self):
        'effectiveWinId(self) -> sip.voidptr'
        pass
    
    @classmethod
    def ensurePolished(cls, self):
        'ensurePolished(self)'
        pass
    
    @classmethod
    def enterEvent(cls, self, QEvent):
        'enterEvent(self, QEvent)'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def find(cls, sipvoidptr):
        'find(sip.voidptr) -> QWidget'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def focusInEvent(cls, self, QFocusEvent):
        'focusInEvent(self, QFocusEvent)'
        pass
    
    @classmethod
    def focusNextChild(cls, self):
        'focusNextChild(self) -> bool'
        return True
    
    @classmethod
    def focusNextPrevChild(cls, self, bool):
        'focusNextPrevChild(self, bool) -> bool'
        return True
    
    @classmethod
    def focusOutEvent(cls, self, QFocusEvent):
        'focusOutEvent(self, QFocusEvent)'
        pass
    
    @classmethod
    def focusPolicy(cls, self):
        'focusPolicy(self) -> Qt.FocusPolicy'
        pass
    
    @classmethod
    def focusPreviousChild(cls, self):
        'focusPreviousChild(self) -> bool'
        return True
    
    @classmethod
    def focusProxy(cls, self):
        'focusProxy(self) -> QWidget'
        pass
    
    @classmethod
    def focusWidget(cls, self):
        'focusWidget(self) -> QWidget'
        pass
    
    @classmethod
    def font(cls, self):
        'font(self) -> QFont'
        pass
    
    @classmethod
    def fontInfo(cls, self):
        'fontInfo(self) -> QFontInfo'
        pass
    
    @classmethod
    def fontMetrics(cls, self):
        'fontMetrics(self) -> QFontMetrics'
        pass
    
    @classmethod
    def foregroundRole(cls, self):
        'foregroundRole(self) -> QPalette.ColorRole'
        pass
    
    @classmethod
    def frameGeometry(cls, self):
        'frameGeometry(self) -> QRect'
        pass
    
    @classmethod
    def frameSize(cls, self):
        'frameSize(self) -> QSize'
        pass
    
    @classmethod
    def geometry(cls, self):
        'geometry(self) -> QRect'
        pass
    
    @classmethod
    def getContentsMargins(cls, self):
        'getContentsMargins(self) -> Tuple[int, int, int, int]'
        pass
    
    @classmethod
    def grab(cls, self, rectangle: QRect=QRect(QPoint(0,0),QSize(-1,-1))):
        'grab(self, rectangle: QRect = QRect(QPoint(0,0),QSize(-1,-1))) -> QPixmap'
        pass
    
    @classmethod
    def grabGesture(cls, self, QtGestureType, flags: Union[Qt.GestureFlags,Qt.GestureFlag]=Qt.GestureFlags()):
        'grabGesture(self, Qt.GestureType, flags: Union[Qt.GestureFlags, Qt.GestureFlag] = Qt.GestureFlags())'
        pass
    
    @classmethod
    def grabKeyboard(cls, self):
        'grabKeyboard(self)'
        pass
    
    @classmethod
    def grabMouse(cls, self, UnionQCursor=None, QtCursorShape=None):
        'grabMouse(self)\ngrabMouse(self, Union[QCursor, Qt.CursorShape])'
        pass
    
    @classmethod
    def grabShortcut(cls, self, UnionQKeySequence=None, QKeySequenceStandardKey=None, str=None, int=None, context: Qt.ShortcutContext=Qt.WindowShortcut):
        'grabShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int], context: Qt.ShortcutContext = Qt.WindowShortcut) -> int'
        return 1
    
    @classmethod
    def graphicsEffect(cls, self):
        'graphicsEffect(self) -> QGraphicsEffect'
        pass
    
    @classmethod
    def graphicsProxyWidget(cls, self):
        'graphicsProxyWidget(self) -> QGraphicsProxyWidget'
        pass
    
    @classmethod
    def hasFocus(cls, self):
        'hasFocus(self) -> bool'
        return True
    
    @classmethod
    def hasHeightForWidth(cls, self):
        'hasHeightForWidth(self) -> bool'
        return True
    
    @classmethod
    def hasMouseTracking(cls, self):
        'hasMouseTracking(self) -> bool'
        return True
    
    @classmethod
    def hasTabletTracking(cls, self):
        'hasTabletTracking(self) -> bool'
        return True
    
    @classmethod
    def height(cls, self):
        'height(self) -> int'
        return 1
    
    @classmethod
    def heightForWidth(cls, self, int):
        'heightForWidth(self, int) -> int'
        return 1
    
    @classmethod
    def heightMM(cls, self):
        'heightMM(self) -> int'
        return 1
    
    @classmethod
    def hide(cls, self):
        'hide(self)'
        pass
    
    @classmethod
    def hideEvent(cls, self, QHideEvent):
        'hideEvent(self, QHideEvent)'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def initPainter(cls, self, QPainter):
        'initPainter(self, QPainter)'
        pass
    
    @classmethod
    def inputMethodEvent(cls, self, QInputMethodEvent):
        'inputMethodEvent(self, QInputMethodEvent)'
        pass
    
    @classmethod
    def inputMethodHints(cls, self):
        'inputMethodHints(self) -> Qt.InputMethodHints'
        pass
    
    @classmethod
    def inputMethodQuery(cls, self, QtInputMethodQuery):
        'inputMethodQuery(self, Qt.InputMethodQuery) -> Any'
        pass
    
    @classmethod
    def insertAction(cls, self, QAction, QAction_):
        'insertAction(self, QAction, QAction)'
        pass
    
    @classmethod
    def insertActions(cls, self, QAction, IterableQAction=None):
        'insertActions(self, QAction, Iterable[QAction])'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isActiveWindow(cls, self):
        'isActiveWindow(self) -> bool'
        return True
    
    @classmethod
    def isAncestorOf(cls, self, QWidget):
        'isAncestorOf(self, QWidget) -> bool'
        return True
    
    @classmethod
    def isEnabled(cls, self):
        'isEnabled(self) -> bool'
        return True
    
    @classmethod
    def isEnabledTo(cls, self, QWidget):
        'isEnabledTo(self, QWidget) -> bool'
        return True
    
    @classmethod
    def isFullScreen(cls, self):
        'isFullScreen(self) -> bool'
        return True
    
    @classmethod
    def isHidden(cls, self):
        'isHidden(self) -> bool'
        return True
    
    @classmethod
    def isLeftToRight(cls, self):
        'isLeftToRight(self) -> bool'
        return True
    
    @classmethod
    def isMaximized(cls, self):
        'isMaximized(self) -> bool'
        return True
    
    @classmethod
    def isMinimized(cls, self):
        'isMinimized(self) -> bool'
        return True
    
    @classmethod
    def isModal(cls, self):
        'isModal(self) -> bool'
        return True
    
    @classmethod
    def isRightToLeft(cls, self):
        'isRightToLeft(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls, self, QMetaMethod):
        'isSignalConnected(self, QMetaMethod) -> bool'
        return True
    
    @classmethod
    def isVisible(cls, self):
        'isVisible(self) -> bool'
        return True
    
    @classmethod
    def isVisibleTo(cls, self, QWidget):
        'isVisibleTo(self, QWidget) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindow(cls, self):
        'isWindow(self) -> bool'
        return True
    
    @classmethod
    def isWindowModified(cls, self):
        'isWindowModified(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def keyPressEvent(cls, self, QKeyEvent):
        'keyPressEvent(self, QKeyEvent)'
        pass
    
    @classmethod
    def keyReleaseEvent(cls, self, QKeyEvent):
        'keyReleaseEvent(self, QKeyEvent)'
        pass
    
    @classmethod
    def keyboardGrabber(cls):
        'keyboardGrabber() -> QWidget'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def layout(cls, self):
        'layout(self) -> QLayout'
        pass
    
    @classmethod
    def layoutDirection(cls, self):
        'layoutDirection(self) -> Qt.LayoutDirection'
        pass
    
    @classmethod
    def leaveEvent(cls, self, QEvent):
        'leaveEvent(self, QEvent)'
        pass
    
    @classmethod
    def load(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'load(self, str)\nload(self, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def locale(cls, self):
        'locale(self) -> QLocale'
        pass
    
    @classmethod
    def logicalDpiX(cls, self):
        'logicalDpiX(self) -> int'
        return 1
    
    @classmethod
    def logicalDpiY(cls, self):
        'logicalDpiY(self) -> int'
        return 1
    
    @classmethod
    def lower(cls, self):
        'lower(self)'
        pass
    
    @classmethod
    def mapFrom(cls, self, QWidget, QPoint):
        'mapFrom(self, QWidget, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mapFromGlobal(cls, self, QPoint):
        'mapFromGlobal(self, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mapFromParent(cls, self, QPoint):
        'mapFromParent(self, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mapTo(cls, self, QWidget, QPoint):
        'mapTo(self, QWidget, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mapToGlobal(cls, self, QPoint):
        'mapToGlobal(self, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mapToParent(cls, self, QPoint):
        'mapToParent(self, QPoint) -> QPoint'
        pass
    
    @classmethod
    def mask(cls, self):
        'mask(self) -> QRegion'
        pass
    
    @classmethod
    def maximumHeight(cls, self):
        'maximumHeight(self) -> int'
        return 1
    
    @classmethod
    def maximumSize(cls, self):
        'maximumSize(self) -> QSize'
        pass
    
    @classmethod
    def maximumWidth(cls, self):
        'maximumWidth(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def metric(cls, self, QPaintDevicePaintDeviceMetric):
        'metric(self, QPaintDevice.PaintDeviceMetric) -> int'
        return 1
    
    @classmethod
    def minimumHeight(cls, self):
        'minimumHeight(self) -> int'
        return 1
    
    @classmethod
    def minimumSize(cls, self):
        'minimumSize(self) -> QSize'
        pass
    
    @classmethod
    def minimumSizeHint(cls, self):
        'minimumSizeHint(self) -> QSize'
        pass
    
    @classmethod
    def minimumWidth(cls, self):
        'minimumWidth(self) -> int'
        return 1
    
    @classmethod
    def mouseDoubleClickEvent(cls, self, QMouseEvent):
        'mouseDoubleClickEvent(self, QMouseEvent)'
        pass
    
    @classmethod
    def mouseGrabber(cls):
        'mouseGrabber() -> QWidget'
        pass
    
    @classmethod
    def mouseMoveEvent(cls, self, QMouseEvent):
        'mouseMoveEvent(self, QMouseEvent)'
        pass
    
    @classmethod
    def mousePressEvent(cls, self, QMouseEvent):
        'mousePressEvent(self, QMouseEvent)'
        pass
    
    @classmethod
    def mouseReleaseEvent(cls, self, QMouseEvent):
        'mouseReleaseEvent(self, QMouseEvent)'
        pass
    
    @classmethod
    def move(cls, self, int, int_):
        'move(self, QPoint)\nmove(self, int, int)'
        pass
    
    @classmethod
    def moveEvent(cls, self, QMoveEvent):
        'moveEvent(self, QMoveEvent)'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def nativeEvent(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, sipvoidptr=None):
        'nativeEvent(self, Union[QByteArray, bytes, bytearray], sip.voidptr) -> Tuple[bool, int]'
        pass
    
    @classmethod
    def nativeParentWidget(cls, self):
        'nativeParentWidget(self) -> QWidget'
        pass
    
    @classmethod
    def nextInFocusChain(cls, self):
        'nextInFocusChain(self) -> QWidget'
        pass
    
    @classmethod
    def normalGeometry(cls, self):
        'normalGeometry(self) -> QRect'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def overrideWindowFlags(cls, self, UnionQtWindowFlags=None, QtWindowType=None):
        'overrideWindowFlags(self, Union[Qt.WindowFlags, Qt.WindowType])'
        pass
    
    @classmethod
    def overrideWindowState(cls, self, UnionQtWindowStates=None, QtWindowState=None):
        'overrideWindowState(self, Union[Qt.WindowStates, Qt.WindowState])'
        pass
    
    @classmethod
    def paintEngine(cls, self):
        'paintEngine(self) -> QPaintEngine'
        pass
    
    @classmethod
    def paintEvent(cls, self, QPaintEvent):
        'paintEvent(self, QPaintEvent)'
        pass
    
    @classmethod
    def paintingActive(cls, self):
        'paintingActive(self) -> bool'
        return True
    
    @classmethod
    def palette(cls, self):
        'palette(self) -> QPalette'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentWidget(cls, self):
        'parentWidget(self) -> QWidget'
        pass
    
    @classmethod
    def physicalDpiX(cls, self):
        'physicalDpiX(self) -> int'
        return 1
    
    @classmethod
    def physicalDpiY(cls, self):
        'physicalDpiY(self) -> int'
        return 1
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> QPoint'
        pass
    
    @classmethod
    def previousInFocusChain(cls, self):
        'previousInFocusChain(self) -> QWidget'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def raise_(cls, self):
        'raise_(self)'
        pass
    
    @classmethod
    def receivers(cls, self, PYQT_SIGNAL):
        'receivers(self, PYQT_SIGNAL) -> int'
        return 1
    
    @classmethod
    def rect(cls, self):
        'rect(self) -> QRect'
        pass
    
    @classmethod
    def releaseKeyboard(cls, self):
        'releaseKeyboard(self)'
        pass
    
    @classmethod
    def releaseMouse(cls, self):
        'releaseMouse(self)'
        pass
    
    @classmethod
    def releaseShortcut(cls, self, int):
        'releaseShortcut(self, int)'
        pass
    
    @classmethod
    def removeAction(cls, self, QAction):
        'removeAction(self, QAction)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def render(cls, self, QPaintDevice, targetOffset: QPoint=QPoint(), sourceRegion: QRegion=QRegion(), flags: Union[QWidget.RenderFlags,QWidget.RenderFlag]=QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren)):
        'render(self, QPaintDevice, targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren))\nrender(self, QPainter, targetOffset: QPoint = QPoint(), sourceRegion: QRegion = QRegion(), flags: Union[QWidget.RenderFlags, QWidget.RenderFlag] = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren))'
        pass
    
    @classmethod
    def renderer(cls, self):
        'renderer(self) -> QSvgRenderer'
        pass
    
    @classmethod
    def repaint(cls, self, int, int_, int_1, int_2):
        'repaint(self)\nrepaint(self, int, int, int, int)\nrepaint(self, QRect)\nrepaint(self, QRegion)'
        pass
    
    @classmethod
    def resize(cls, self, int, int_):
        'resize(self, QSize)\nresize(self, int, int)'
        pass
    
    @classmethod
    def resizeEvent(cls, self, QResizeEvent):
        'resizeEvent(self, QResizeEvent)'
        pass
    
    @classmethod
    def restoreGeometry(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'restoreGeometry(self, Union[QByteArray, bytes, bytearray]) -> bool'
        return True
    
    @classmethod
    def saveGeometry(cls, self):
        'saveGeometry(self) -> QByteArray'
        pass
    
    @classmethod
    def scroll(cls, self, int, int_, QRect):
        'scroll(self, int, int)\nscroll(self, int, int, QRect)'
        pass
    
    @classmethod
    def sender(cls, self):
        'sender(self) -> QObject'
        pass
    
    @classmethod
    def senderSignalIndex(cls, self):
        'senderSignalIndex(self) -> int'
        return 1
    
    @classmethod
    def setAcceptDrops(cls, self, bool):
        'setAcceptDrops(self, bool)'
        pass
    
    @classmethod
    def setAccessibleDescription(cls, self, str):
        'setAccessibleDescription(self, str)'
        pass
    
    @classmethod
    def setAccessibleName(cls, self, str):
        'setAccessibleName(self, str)'
        pass
    
    @classmethod
    def setAttribute(cls, self, QtWidgetAttribute, on: bool=True):
        'setAttribute(self, Qt.WidgetAttribute, on: bool = True)'
        pass
    
    @classmethod
    def setAutoFillBackground(cls, self, bool):
        'setAutoFillBackground(self, bool)'
        pass
    
    @classmethod
    def setBackgroundRole(cls, self, QPaletteColorRole):
        'setBackgroundRole(self, QPalette.ColorRole)'
        pass
    
    @classmethod
    def setBaseSize(cls, self, int, int_):
        'setBaseSize(self, int, int)\nsetBaseSize(self, QSize)'
        pass
    
    @classmethod
    def setContentsMargins(cls, self, int, int_, int_1, int_2):
        'setContentsMargins(self, int, int, int, int)\nsetContentsMargins(self, QMargins)'
        pass
    
    @classmethod
    def setContextMenuPolicy(cls, self, QtContextMenuPolicy):
        'setContextMenuPolicy(self, Qt.ContextMenuPolicy)'
        pass
    
    @classmethod
    def setCursor(cls, self, UnionQCursor=None, QtCursorShape=None):
        'setCursor(self, Union[QCursor, Qt.CursorShape])'
        pass
    
    @classmethod
    def setDisabled(cls, self, bool):
        'setDisabled(self, bool)'
        pass
    
    @classmethod
    def setEnabled(cls, self, bool):
        'setEnabled(self, bool)'
        pass
    
    @classmethod
    def setFixedHeight(cls, self, int):
        'setFixedHeight(self, int)'
        pass
    
    @classmethod
    def setFixedSize(cls, self, int, int_):
        'setFixedSize(self, QSize)\nsetFixedSize(self, int, int)'
        pass
    
    @classmethod
    def setFixedWidth(cls, self, int):
        'setFixedWidth(self, int)'
        pass
    
    @classmethod
    def setFocus(cls, self, QtFocusReason):
        'setFocus(self)\nsetFocus(self, Qt.FocusReason)'
        pass
    
    @classmethod
    def setFocusPolicy(cls, self, QtFocusPolicy):
        'setFocusPolicy(self, Qt.FocusPolicy)'
        pass
    
    @classmethod
    def setFocusProxy(cls, self, QWidget):
        'setFocusProxy(self, QWidget)'
        pass
    
    @classmethod
    def setFont(cls, self, QFont):
        'setFont(self, QFont)'
        pass
    
    @classmethod
    def setForegroundRole(cls, self, QPaletteColorRole):
        'setForegroundRole(self, QPalette.ColorRole)'
        pass
    
    @classmethod
    def setGeometry(cls, self, int, int_, int_1, int_2):
        'setGeometry(self, QRect)\nsetGeometry(self, int, int, int, int)'
        pass
    
    @classmethod
    def setGraphicsEffect(cls, self, QGraphicsEffect):
        'setGraphicsEffect(self, QGraphicsEffect)'
        pass
    
    @classmethod
    def setHidden(cls, self, bool):
        'setHidden(self, bool)'
        pass
    
    @classmethod
    def setInputMethodHints(cls, self, UnionQtInputMethodHints=None, QtInputMethodHint=None):
        'setInputMethodHints(self, Union[Qt.InputMethodHints, Qt.InputMethodHint])'
        pass
    
    @classmethod
    def setLayout(cls, self, QLayout):
        'setLayout(self, QLayout)'
        pass
    
    @classmethod
    def setLayoutDirection(cls, self, QtLayoutDirection):
        'setLayoutDirection(self, Qt.LayoutDirection)'
        pass
    
    @classmethod
    def setLocale(cls, self, QLocale):
        'setLocale(self, QLocale)'
        pass
    
    @classmethod
    def setMask(cls, self, QRegion):
        'setMask(self, QBitmap)\nsetMask(self, QRegion)'
        pass
    
    @classmethod
    def setMaximumHeight(cls, self, int):
        'setMaximumHeight(self, int)'
        pass
    
    @classmethod
    def setMaximumSize(cls, self, int, int_):
        'setMaximumSize(self, int, int)\nsetMaximumSize(self, QSize)'
        pass
    
    @classmethod
    def setMaximumWidth(cls, self, int):
        'setMaximumWidth(self, int)'
        pass
    
    @classmethod
    def setMinimumHeight(cls, self, int):
        'setMinimumHeight(self, int)'
        pass
    
    @classmethod
    def setMinimumSize(cls, self, int, int_):
        'setMinimumSize(self, int, int)\nsetMinimumSize(self, QSize)'
        pass
    
    @classmethod
    def setMinimumWidth(cls, self, int):
        'setMinimumWidth(self, int)'
        pass
    
    @classmethod
    def setMouseTracking(cls, self, bool):
        'setMouseTracking(self, bool)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setPalette(cls, self, QPalette):
        'setPalette(self, QPalette)'
        pass
    
    @classmethod
    def setParent(cls, self, QWidget, UnionQtWindowFlags=None, QtWindowType=None):
        'setParent(self, QWidget)\nsetParent(self, QWidget, Union[Qt.WindowFlags, Qt.WindowType])'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setShortcutAutoRepeat(cls, self, int, enabled: bool=True):
        'setShortcutAutoRepeat(self, int, enabled: bool = True)'
        pass
    
    @classmethod
    def setShortcutEnabled(cls, self, int, enabled: bool=True):
        'setShortcutEnabled(self, int, enabled: bool = True)'
        pass
    
    @classmethod
    def setSizeIncrement(cls, self, int, int_):
        'setSizeIncrement(self, int, int)\nsetSizeIncrement(self, QSize)'
        pass
    
    @classmethod
    def setSizePolicy(cls, self, QSizePolicyPolicy, QSizePolicyPolicy_):
        'setSizePolicy(self, QSizePolicy)\nsetSizePolicy(self, QSizePolicy.Policy, QSizePolicy.Policy)'
        pass
    
    @classmethod
    def setStatusTip(cls, self, str):
        'setStatusTip(self, str)'
        pass
    
    @classmethod
    def setStyle(cls, self, QStyle):
        'setStyle(self, QStyle)'
        pass
    
    @classmethod
    def setStyleSheet(cls, self, str):
        'setStyleSheet(self, str)'
        pass
    
    @classmethod
    def setTabOrder(cls, QWidget, QWidget_):
        'setTabOrder(QWidget, QWidget)'
        pass
    
    @classmethod
    def setTabletTracking(cls, self, bool):
        'setTabletTracking(self, bool)'
        pass
    
    @classmethod
    def setToolTip(cls, self, str):
        'setToolTip(self, str)'
        pass
    
    @classmethod
    def setToolTipDuration(cls, self, int):
        'setToolTipDuration(self, int)'
        pass
    
    @classmethod
    def setUpdatesEnabled(cls, self, bool):
        'setUpdatesEnabled(self, bool)'
        pass
    
    @classmethod
    def setVisible(cls, self, bool):
        'setVisible(self, bool)'
        pass
    
    @classmethod
    def setWhatsThis(cls, self, str):
        'setWhatsThis(self, str)'
        pass
    
    @classmethod
    def setWindowFilePath(cls, self, str):
        'setWindowFilePath(self, str)'
        pass
    
    @classmethod
    def setWindowFlag(cls, self, QtWindowType, on: bool=True):
        'setWindowFlag(self, Qt.WindowType, on: bool = True)'
        pass
    
    @classmethod
    def setWindowFlags(cls, self, UnionQtWindowFlags=None, QtWindowType=None):
        'setWindowFlags(self, Union[Qt.WindowFlags, Qt.WindowType])'
        pass
    
    @classmethod
    def setWindowIcon(cls, self, QIcon):
        'setWindowIcon(self, QIcon)'
        pass
    
    @classmethod
    def setWindowIconText(cls, self, str):
        'setWindowIconText(self, str)'
        pass
    
    @classmethod
    def setWindowModality(cls, self, QtWindowModality):
        'setWindowModality(self, Qt.WindowModality)'
        pass
    
    @classmethod
    def setWindowModified(cls, self, bool):
        'setWindowModified(self, bool)'
        pass
    
    @classmethod
    def setWindowOpacity(cls, self, float):
        'setWindowOpacity(self, float)'
        pass
    
    @classmethod
    def setWindowRole(cls, self, str):
        'setWindowRole(self, str)'
        pass
    
    @classmethod
    def setWindowState(cls, self, UnionQtWindowStates=None, QtWindowState=None):
        'setWindowState(self, Union[Qt.WindowStates, Qt.WindowState])'
        pass
    
    @classmethod
    def setWindowTitle(cls, self, str):
        'setWindowTitle(self, str)'
        pass
    
    @classmethod
    def sharedPainter(cls, self):
        'sharedPainter(self) -> QPainter'
        pass
    
    @classmethod
    def show(cls, self):
        'show(self)'
        pass
    
    @classmethod
    def showEvent(cls, self, QShowEvent):
        'showEvent(self, QShowEvent)'
        pass
    
    @classmethod
    def showFullScreen(cls, self):
        'showFullScreen(self)'
        pass
    
    @classmethod
    def showMaximized(cls, self):
        'showMaximized(self)'
        pass
    
    @classmethod
    def showMinimized(cls, self):
        'showMinimized(self)'
        pass
    
    @classmethod
    def showNormal(cls, self):
        'showNormal(self)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> QSize'
        pass
    
    @classmethod
    def sizeHint(cls, self):
        'sizeHint(self) -> QSize'
        pass
    
    @classmethod
    def sizeIncrement(cls, self):
        'sizeIncrement(self) -> QSize'
        pass
    
    @classmethod
    def sizePolicy(cls, self):
        'sizePolicy(self) -> QSizePolicy'
        pass
    
    @classmethod
    def stackUnder(cls, self, QWidget):
        'stackUnder(self, QWidget)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = _mod_PyQt5_QtCore.QMetaObject()
    @classmethod
    def statusTip(cls, self):
        'statusTip(self) -> str'
        return ''
    
    @classmethod
    def style(cls, self):
        'style(self) -> QStyle'
        pass
    
    @classmethod
    def styleSheet(cls, self):
        'styleSheet(self) -> str'
        return ''
    
    @classmethod
    def tabletEvent(cls, self, QTabletEvent):
        'tabletEvent(self, QTabletEvent)'
        pass
    
    @classmethod
    def testAttribute(cls, self, QtWidgetAttribute):
        'testAttribute(self, Qt.WidgetAttribute) -> bool'
        return True
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def toolTip(cls, self):
        'toolTip(self) -> str'
        return ''
    
    @classmethod
    def toolTipDuration(cls, self):
        'toolTipDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def underMouse(cls, self):
        'underMouse(self) -> bool'
        return True
    
    @classmethod
    def ungrabGesture(cls, self, QtGestureType):
        'ungrabGesture(self, Qt.GestureType)'
        pass
    
    @classmethod
    def unsetCursor(cls, self):
        'unsetCursor(self)'
        pass
    
    @classmethod
    def unsetLayoutDirection(cls, self):
        'unsetLayoutDirection(self)'
        pass
    
    @classmethod
    def unsetLocale(cls, self):
        'unsetLocale(self)'
        pass
    
    @classmethod
    def update(cls, self, int, int_, int_1, int_2):
        'update(self)\nupdate(self, QRect)\nupdate(self, QRegion)\nupdate(self, int, int, int, int)'
        pass
    
    @classmethod
    def updateGeometry(cls, self):
        'updateGeometry(self)'
        pass
    
    @classmethod
    def updateMicroFocus(cls, self):
        'updateMicroFocus(self)'
        pass
    
    @classmethod
    def updatesEnabled(cls, self):
        'updatesEnabled(self) -> bool'
        return True
    
    @classmethod
    def visibleRegion(cls, self):
        'visibleRegion(self) -> QRegion'
        pass
    
    @classmethod
    def whatsThis(cls, self):
        'whatsThis(self) -> str'
        return ''
    
    @classmethod
    def wheelEvent(cls, self, QWheelEvent):
        'wheelEvent(self, QWheelEvent)'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> int'
        return 1
    
    @classmethod
    def widthMM(cls, self):
        'widthMM(self) -> int'
        return 1
    
    @classmethod
    def winId(cls, self):
        'winId(self) -> sip.voidptr'
        pass
    
    @classmethod
    def window(cls, self):
        'window(self) -> QWidget'
        pass
    
    @classmethod
    def windowFilePath(cls, self):
        'windowFilePath(self) -> str'
        return ''
    
    @classmethod
    def windowFlags(cls, self):
        'windowFlags(self) -> Qt.WindowFlags'
        pass
    
    @classmethod
    def windowHandle(cls, self):
        'windowHandle(self) -> QWindow'
        pass
    
    @classmethod
    def windowIcon(cls, self):
        'windowIcon(self) -> QIcon'
        pass
    
    @classmethod
    def windowIconText(cls, self):
        'windowIconText(self) -> str'
        return ''
    
    @classmethod
    def windowModality(cls, self):
        'windowModality(self) -> Qt.WindowModality'
        pass
    
    @classmethod
    def windowOpacity(cls, self):
        'windowOpacity(self) -> float'
        return 1.0
    
    @classmethod
    def windowRole(cls, self):
        'windowRole(self) -> str'
        return ''
    
    @classmethod
    def windowState(cls, self):
        'windowState(self) -> Qt.WindowStates'
        pass
    
    @classmethod
    def windowTitle(cls, self):
        'windowTitle(self) -> str'
        return ''
    
    @classmethod
    def windowType(cls, self):
        'windowType(self) -> Qt.WindowType'
        pass
    
    @classmethod
    def x(cls, self):
        'x(self) -> int'
        return 1
    
    @classmethod
    def y(cls, self):
        'y(self) -> int'
        return 1
    

__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/PyQt5/QtSvg.so'
__name__ = 'PyQt5.QtSvg'
__package__ = 'PyQt5'

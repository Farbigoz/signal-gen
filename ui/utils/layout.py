def ClearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            layout.removeWidget(child.widget())
            child.widget().setParent(None)


def ClearFrame(frame):
    ClearLayout(frame.layout())


def AddToFrame(frame, widget, n=None, align=None):
    widget.setParent(frame)
    if align is None:
        frame.layout().addWidget(widget)
    else:
        frame.layout().addWidget(widget, 0, align)

    if n is not None:
        frame.layout().insertWidget(n, widget)


def RemoveFromFrame(frame, widget):
    if widget.parent() is not None:
        frame.layout().removeWidget(widget)
        widget.setParent(None)

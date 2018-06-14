# Python Wayland-egl binding

This module provides access to the `wayland-egl` library from Python.

To use EGL with Wayland, you have to call this library, so here is the wrapper.
This library exposes the following function:

```python
def wl_egl_window_create(wl_surface, width, height):
    """Create the wayland-egl window

    Args: 
        wl_surface (ptr): The wayland surface. You can get it with the
                          pywayland library.
        width (int): Window width
        height (int): Window height
    """

def wl_egl_window_resize(wl_egl_window, width, height, dx, dy):
    """Resize the wayland-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`
        width (int): The new window width
        height (int): The new window height
        dx (int): Don't know
        dy (int): Idem
    """

def wl_egl_window_destroy(wl_egl_window):
    """Destroy the window-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`
    """

def wl_egl_window_get_attached_size(wl_egl_window):
    """Destroy the window-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`

    Returns:
        (int, int): Width and height
    """
```
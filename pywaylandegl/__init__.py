from pywaylandegl._pywaylandegl import ffi, lib


def wl_egl_window_create(wl_surface, width, height):
    """Create the wayland-egl window

    Args: 
        wl_surface (ptr): The wayland surface. You can get it with the
                          pywayland library.
        width (int): Window width
        height (int): Window height
    """
    return lib.wl_egl_window_create(wl_surface, width, height)


def wl_egl_window_resize(wl_egl_window, width, height, dx, dy):
    """Resize the wayland-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`
        width (int): The new window width
        height (int): The new window height
        dx (int): Don't know
        dy (int): Idem
    """
    lib.wl_egl_window_resize(wl_egl_window, width, height, dx, dy)


def wl_egl_window_destroy(wl_egl_window):
    """Destroy the window-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`
    """
    lib.wl_egl_window_destroy(wl_egl_window)


def wl_egl_window_get_attached_size(wl_egl_window):
    """Destroy the window-egl window

    Args:
        wl_egl_window (window): The window created with `wl_egl_window_create`

    Returns:
        (int, int): Width and height
    """
    width = ffi.new('int*')
    height = ffi.new('int*')
    lib.wl_egl_window_get_attached_size(wl_egl_window, width, height)

    return width[0], height[0]
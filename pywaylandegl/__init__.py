from pywaylandegl._pywaylandegl import ffi, lib


def wl_egl_window_create(wl_surface, width, height):
    return lib.wl_egl_window_create(wl_surface, width, height)


def wl_egl_window_resize(wl_egl_window, width, height, dx, dy):
    lib.wl_egl_window_resize(wl_egl_window, width, height, dx, dy)


def wl_egl_window_destroy(wl_egl_window):
    lib.wl_egl_window_destroy(wl_egl_window)


def wl_egl_window_get_attached_size(wl_egl_window):
    width = ffi.new('int*')
    height = ffi.new('int*')
    lib.wl_egl_window_get_attached_size(wl_egl_window, width, height)

    return width[0], height[0]
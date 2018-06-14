typedef void* wl_surface;
typedef void* wl_egl_window;
wl_egl_window wl_egl_window_create(wl_surface, int, int);
void wl_egl_window_resize(wl_egl_window, int, int, int, int);
void wl_egl_window_destroy(wl_egl_window);
void wl_egl_window_get_attached_size(wl_egl_window, int*, int*);
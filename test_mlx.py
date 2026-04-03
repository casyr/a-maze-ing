from mlx import Mlx


m = Mlx()
ptr = m.mlx_init()
r, width, height = m.mlx_get_screen_size(ptr)
win = m.mlx_new_window(ptr, width, height, "Test")
cell_size = 1000  ##int(min(3300 / width, 2160 / height))
m.mlx_pixel_put(ptr, win, 200, 200, 0xFFFFFFFF)
for i, _ in enumerate(range(cell_size)):
    m.mlx_pixel_put(ptr, win, 1000 + i, 1000, 0xFFFFFFFF)

def on_close(param):
    m.mlx_loop_exit(ptr)


m.mlx_hook(win, 33, 0, on_close, None)
m.mlx_key_hook(win, lambda key, param: m.mlx_loop_exit(ptr) if key == 65307 else None, None)
m.mlx_loop(ptr)

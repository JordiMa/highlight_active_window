import pyautogui
import tkinter as tk
import pygetwindow as gw

def set_window_opacity(window, opacity):
    """
    Set the opacity of the given window.
    """
    window.attributes("-alpha", opacity)
    return window

def create_overlay(on_click_callback):
    """
    Create an overlay window and bind a click event.
    """
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.configure(bg='black')
    root.bind("<Button-1>", on_click_callback)  # Bind click event
    return root

def get_active_window():
    """
    Get the bounding box of the currently active window.
    """
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.box
    except:
        pass
    return None

def on_overlay_click(event):
    """
    Deactivate the overlays for a short period after a click.
    """
    deactivate_overlays()
    root.after(5000, reactivate_overlays)  # Reactivate overlays after 5 seconds

def deactivate_overlays():
    """
    Set the opacity of all overlays to 0 (invisible).
    """
    set_window_opacity(top_overlay, 0)
    set_window_opacity(left_overlay, 0)
    set_window_opacity(right_overlay, 0)
    set_window_opacity(bottom_overlay, 0)

def reactivate_overlays():
    """
    Set the opacity of all overlays to the dimmed value.
    """
    set_window_opacity(top_overlay, dim_opacity)
    set_window_opacity(left_overlay, dim_opacity)
    set_window_opacity(right_overlay, dim_opacity)
    set_window_opacity(bottom_overlay, dim_opacity)

def update_overlays():
    """
    Update the position and size of the overlays based on the active window.
    """
    active_window_box = get_active_window()

    if active_window_box:
        left = max(0, active_window_box.left)
        top = max(0, active_window_box.top)
        right = min(screen_width, active_window_box.left + active_window_box.width)
        bottom = min(screen_height, active_window_box.top + active_window_box.height)

        # Set the overlays to cover the entire screen except the active window
        top_overlay.geometry(f"{screen_width}x{top}+0+0")
        left_overlay.geometry(f"{left}x{bottom - top}+0+{top}")
        right_overlay.geometry(f"{screen_width - right}x{bottom - top}+{right}+{top}")
        bottom_overlay.geometry(f"{screen_width}x{screen_height - bottom}+0+{bottom}")

        top_overlay.update()
        left_overlay.update()
        right_overlay.update()
        bottom_overlay.update()
    else:
        deactivate_overlays()

    # Schedule the next update
    root.after(100, update_overlays)

screen_width, screen_height = pyautogui.size()
dim_opacity = 0.7  # Adjust this value to set the dimming opacity

# Create a single root window for managing the overlays
root = tk.Tk()
root.withdraw()  # Hide the root window

# Create overlays for the regions around the active window
top_overlay = create_overlay(on_overlay_click)
left_overlay = create_overlay(on_overlay_click)
right_overlay = create_overlay(on_overlay_click)
bottom_overlay = create_overlay(on_overlay_click)

# Set initial opacity for all overlays
set_window_opacity(top_overlay, dim_opacity)
set_window_opacity(left_overlay, dim_opacity)
set_window_opacity(right_overlay, dim_opacity)
set_window_opacity(bottom_overlay, dim_opacity)

# Start the overlay update loop
root.after(100, update_overlays)

# Start the tkinter main loop
root.mainloop()

from mss import mss, tools

with mss() as sct:
    part: dict[str, int] = {"top": 0, "left": 0, "width": 100, "height": 100}
    img = sct.grab(part)
    tools.to_png(
        img.rgb,
        img.size,
        output="Section 26_Controlling Your Computer/files/partial_screenshot.png",
    )

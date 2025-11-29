# Braille Pictures

Convert black–white images into Unicode Braille art that you can view in a terminal, text editor, or screen reader.

This project provides:

- a **GUI app** (`main_GUI.py` / `main_GUI.exe`) to batch–convert images and save the result as `.txt` files  
- a **CLI app** (`main-by_braille.py` / `main-by_braille.exe`) for quick conversions from the command line  
- a small **conversion library** (`main_symbs.py`) that does the actual image → braille work

---

## 1. How it works

The conversion is based on Unicode Braille characters (U+2800–U+28FF).

- The image is converted to **1-bit black/white**.
- The image is processed in **blocks of 2×4 pixels**, which map to the 8 dots of a braille cell:


(x,   y)   -> dot 1
(x,   y+1) -> dot 2
(x,   y+2) -> dot 3
(x+1, y)   -> dot 4
(x+1, y+1) -> dot 5
(x+1, y+2) -> dot 6
(x,   y+3) -> dot 7
(x+1, y+3) -> dot 8

````

- For each cell, the corresponding Unicode braille character is computed and added to the output.

The result is a grid of braille characters that visually approximates the original image.

---

## 2. Project structure

```text
brialle-pictures/
├─ dist/
│  ├─ main_GUI.exe            # Built GUI executable
│  └─ main-by_braille.exe     # Built CLI executable
├─ examples/
│  ├─ input.png
│  ├─ input2.png
│  └─ result.png              # Example braille output screenshot
├─ src/
 └─ gui/
    ├─ main_GUI.py          # PyQt5 GUI frontend
    ├─ main_symbs.py        # Image → braille conversion logic
    main-by_braille.py      # CLI tool
````

> Paths may differ slightly depending on how you cloned / built the project, but the important scripts are `main_GUI.py`, `main-by_braille.py`, and `main_symbs.py`.

---

## 3. Requirements

For running from source (Python):

* Python 3.x
* [Pillow](https://pypi.org/project/Pillow/) (`PIL`)
* [PyQt5](https://pypi.org/project/PyQt5/) (for the GUI only)

Install with:

```bash
pip install pillow pyqt5
```

If you only use the **executables** in `dist/`, you do **not** need Python or these packages installed.

---

## 4. Using the GUI

Script: `src/gui/main_GUI.py`
Executable (if provided): `dist/main_GUI.exe`

### Run

```bash
python main_GUI.py
```

A window titled **“Choosing files and directory”** will appear.

### Steps

1. **Choose files**

   * Click **“Choose files”**.
   * Select one or more image files.
   * Supported formats: `*.png`, `*.jpg`, `*.jpeg`, `*.bmp`.

   Selected files are listed in the main window.

2. **Choose output directory**

   * Click **“Choose directory to save in .txt”**.
   * Pick an existing folder where you want the text files to be written.

   The chosen directory is also displayed in the list.

3. **Run conversion**

   * Click **“Done”**.
   * For each selected image:

     * The program converts it to braille.
     * It saves a `.txt` file inside the chosen directory.
     * The file name is the original image name, but with `.txt`, e.g.
       `myimage.png` → `myimage.txt`.

No additional prompts will appear; check the output directory for the results.

---

## 5. Using the CLI tool

Script: `src/gui/main-by_braille.py`
Executable (if provided): `dist/main-by_braille.exe`

### Run

```bash
python main-by_braille.py
```

The script enters a loop:

1. It asks for an **input image path**:

   ```text
   type in path to image (.png), Ctrl+C to exit
   ```

   Enter the full or relative path to an image (PNG/JPG/BMP, etc.).

2. It asks for an **output path**:

   ```text
   output path (can be None):
   ```

   * Enter a path to a `.txt` file to save the braille art.
   * Example: `output.txt`
   * If you press **Enter** leaving it empty, it will try to open a file named `''` (empty string), so you should usually provide a filename. (You can easily tweak the script to handle `None` if you like.)

3. The tool:

   * Converts the image to braille.
   * Prints the braille art directly to the terminal.
   * Writes it to the given output file.

If any error occurs (wrong path, unsupported file, etc.), it prints:

```text
retry, error: <error message>
```

Then it asks again for a new image path.
Press **Ctrl+C** to exit the loop.

---

## 6. Library functions (`main_symbs.py`)

You can also import the conversion logic in your own Python code:

```python
from main_symbs import get_symbols, print_symbols

symbols = get_symbols("path/to/image.png")   # returns a list of rows, each row is a list of braille chars
print_symbols(symbols)                       # prints to stdout
print_symbols(symbols, "output.txt")         # saves to a file
```

### `get_symbols(path: str) -> list[list[str]]`

* Opens the image at `path`.
* Converts it to 1-bit (black/white).
* Crops the image so the width is divisible by 2 and the height by 4.
* Returns a 2D list (rows of braille characters).

### `print_symbols(symbols, output_file=None, row_delimiter='\n')`

* Takes the `symbols` returned by `get_symbols`.
* Joins each row into a string, separated by `row_delimiter` (default: newline).
* If `output_file` is given, writes the full braille art to that file (UTF-8).

---

## 7. Notes & limitations

* The algorithm currently assumes **dark pixels are “on” dots** and white pixels are background.
* For best results:

  * Use **high-contrast black and white** images.
  * Simple shapes, text, or logos tend to look better in braille.
* The cropping to multiples of 2×4 pixels is automatic; any extra pixels at the edges are discarded.

---


## 8. Future ideas

Some ideas you might want to add later:

* Preview inside the GUI.
* Drag-and-drop image support.

---

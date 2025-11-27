# Brialle-Pictures: Image to Braille Art Converter
**Documentation**

---

## **1. Introduction**
**Brialle-Pictures** is a Python-based tool that converts images into tactile Braille art. It processes input images and generates a text-based representation using Unicode Braille characters, making visual content accessible through touch or text.

The project is designed to work with any image format supported by the **Pillow (PIL)** library, including `.png`, `.jpg`, `.bmp`, and more.

---

## **2. Project Structure**


Project Structure


| Directory/File       | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `dist/`              | Contains the compiled executable (`main-by_brialle.exe`).                  |
| `examples/`          | Sample input images (`input.png`, `input2.png`) and output (`result.txt`). |
| `src/`               | Source code (`main-by_brialle.py`).                                         |

---

## **3. Dependencies**
- **Python 3.x**
- **Pillow (PIL)**: Required for image processing.

Install Pillow using:
```bash
pip install pillow
```

---

## **4. Core Functionality**

### **4.1 Functions**

#### **`braille_to_unicode(dots)`**
- **Purpose**: Converts a list of Braille dot positions into a Unicode Braille character.
- **Parameters**:
  - `dots`: A list of integers (1-8) representing active Braille dots.
- **Returns**: A Unicode Braille character.

#### **`print_symbols(symbols, output_file=None, row_delimiter='\n')`**
- **Purpose**: Prints or saves Braille symbols as text.
- **Parameters**:
  - `symbols`: A 2D list of Braille characters.
  - `output_file`: (Optional) Path to save the output text file.
  - `row_delimiter`: (Optional) Delimiter for rows (default: newline).
- **Output**: Prints the Braille art to the console and/or saves it to a file.

#### **`get_symbols(path)`**
- **Purpose**: Converts an image into a 2D list of Braille characters.
- **Parameters**:
  - `path`: Path to the input image (supports `.png`, `.jpg`, `.bmp`, etc.).
- **Process**:
  1. Opens the image and converts it to black-and-white (1-bit).
  2. Crops the image to ensure its dimensions are multiples of 2 (width) and 4 (height).
  3. Scans the image in 2x4 pixel blocks, converting each block into a Braille character.
- **Returns**: A 2D list of Braille characters.

---

### **4.2 Main Loop**
- The program runs in a loop, prompting the user for an input image path.
- It processes the image, prints the Braille art, and optionally saves it to a file.
- The loop exits on `Ctrl+C`.

---

## **5. Usage**

### **5.1 Running the Script**
1. **From Source**:
   ```bash
   python src/main-by_brialle.py
   ```
   - Enter the path to your image (e.g., `examples/input.png` or `examples/input.jpg`).
   - Optionally, specify an output file path to save the Braille art.

2. **Using the Executable**:
   - Run `dist/main-by_brialle.exe` on Windows.
   - Follow the same prompts as above.

---

### **5.2 Example Workflow**
1. Place your input image (e.g., `input.png`, `input.jpg`) in the `examples/` folder.
2. Run the script or executable.
3. Enter the path to your image (e.g., `examples/input.png`).
4. Optionally, specify an output file path (e.g., `examples/result.txt`).
5. View the Braille art in the console or the output file.

---

## **6. Example Output**
For an input image like `examples/input.png`, the output will be a text file or console output resembling the image, composed of Braille characters.

---

## **7. Limitations**
- **Image Size**: The script automatically crops the image so that its width is a multiple of 2 and its height is a multiple of 4. This is required for accurate Braille character mapping.
- **Color**: The image is converted to black-and-white (1-bit) for processing. Color information is discarded.
- **Detail**: Highly detailed or complex images may lose clarity when converted to Braille art.

---

## **8. Future Improvements**
- **GUI**: A graphical user interface for easier interaction.
- **Customization**: Options to adjust Braille dot density or size.
- **Batch Processing**: Support for converting multiple images at once.
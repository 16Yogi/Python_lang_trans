import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

# Function to translate text
def translate_text():
    # Get the input text
    input_text = text_input.get("1.0", "end-1c")
    
    # Get the selected source and target languages
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()

    try:
        # Translate the text using deep-translator
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
        
        # Display translated text in the result textbox
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, translated)
    except Exception as e:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, f"Error: {str(e)}")

# Create label and textbox for input text
label_input = tk.Label(root, text="Enter Text:")
label_input.pack(pady=10)
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=10)

# Create source language dropdown
label_src_lang = tk.Label(root, text="Select Source Language:")
label_src_lang.pack(pady=5)
src_lang_combobox = ttk.Combobox(root, values=["en", "fr", "es", "de", "it", "ja", "ru", "zh-cn"])
src_lang_combobox.set("en")  # Default to English
src_lang_combobox.pack(pady=5)

# Create target language dropdown
label_dest_lang = tk.Label(root, text="Select Target Language:")
label_dest_lang.pack(pady=5)
dest_lang_combobox = ttk.Combobox(root, values=["en", "fr", "es", "de", "it", "ja", "ru", "zh-cn"])
dest_lang_combobox.set("es")  # Default to Spanish
dest_lang_combobox.pack(pady=5)

# Create button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create label and textbox for output text
label_output = tk.Label(root, text="Translated Text:")
label_output.pack(pady=10)
text_output = tk.Text(root, height=5, width=60)
text_output.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

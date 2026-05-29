import os
from pathlib import Path
from markitdown import MarkItDown

# Initialize MarkItDown
md = MarkItDown(enable_plugins=False)

# Define paths
root_dir = Path("~/Desktop/8th-semester-NDN/DIP").expanduser()
output_dir = root_dir / "batch_convert"

# Create output directory
output_dir.mkdir(exist_ok=True)

# Supported extensions
supported_extensions = {
    '.pdf', '.pptx', '.docx', '.xlsx', '.xls', '.html', '.txt', '.json', '.xml', '.epub', '.jpg', '.jpeg', '.png', '.mp3', '.wav'
}

# Walk through all files
for subdir, _, files in os.walk(root_dir):
    for file in files:
        file_path = Path(subdir) / file
        if file_path.suffix.lower() in supported_extensions:
            # Compute relative path and output path
            rel_path = file_path.relative_to(root_dir)
            output_path = output_dir / rel_path.with_suffix('.md')

            # Create subdirectories in output_dir
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Convert and save
            try:
                result = md.convert(str(file_path))
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(result.text_content)
                print(f"Converted: {file_path} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {file_path}: {e}")

print("Batch conversion complete!")

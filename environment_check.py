"""Print runtime and dependency information for reproducibility."""
import importlib
import platform
import sys

print("Operating system:", platform.platform())
print("Python:", sys.version.replace("\n", " "))

modules = {
    "TensorFlow": "tensorflow",
    "NumPy": "numpy",
    "pandas": "pandas",
    "scikit-learn": "sklearn",
    "SciPy": "scipy",
    "Matplotlib": "matplotlib",
    "Seaborn": "seaborn",
    "Pillow": "PIL",
    "OpenCV": "cv2",
    "openpyxl": "openpyxl",
}
for label, module_name in modules.items():
    try:
        module = importlib.import_module(module_name)
        print(f"{label}: {getattr(module, '__version__', 'version not exposed')}")
        if module_name == "tensorflow":
            print("TensorFlow GPU devices:", module.config.list_physical_devices("GPU"))
    except Exception as exc:
        print(f"{label}: NOT AVAILABLE ({exc})")

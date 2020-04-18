import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {
        "packages": ["pygame"],
        "excludes": ['tcl', 'ttk', 'tkinter', 'Tkinter', 'scipy']}},
    executables=executables

)

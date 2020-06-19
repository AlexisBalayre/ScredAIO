from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=["idna", "json", "requests", "password_generator", "urllib3", "requests.adapters", "requests.packages.urllib3.util.retry"],
    include_files=["Comptes.json"],
)

base = None
executables = [
    Executable(
        "Generateur_Compte_Zalando_V2.py",
        base=base,
    )
]

setup(
    name="Generateur Compte Zalando V2",
    version="1.0",
    description="Generateur de comptes sur zalando",
    options=dict(build_exe=buildOptions),
    executables=executables,
)
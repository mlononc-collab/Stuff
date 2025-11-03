
import os, sys, textwrap

def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(s).lstrip())

def main():
    if len(sys.argv) != 2:
        print("Usage: python scaffold.py <package_name>")
        sys.exit(1)

    pkg = sys.argv[1]
    # root files
    write("README.md", f"# {pkg}\n\nA tiny Python library.\n")
    write("requirements.txt", "")
    write("setup.py", f"""
        from setuptools import setup, find_packages
        setup(
            name="{pkg}",
            version="0.1.0",
            packages=find_packages(),
            install_requires=[],
            python_requires=">=3.9",
        )
    """)
    # package
    write(f"{pkg}/__init__.py", f'__all__ = ["example"]\n')
    write(f"{pkg}/example.py", """
        def say_hello(name: str) -> str:
            return f"Hello, {name}!"
    """)
    # tests
    write("tests/test_example.py", f"""
        from {pkg}.example import say_hello
        def test_say_hello():
            assert say_hello("World") == "Hello, World!"
    """)
    print(f"Scaffolded Python package '{pkg}'. Next:\n"
          f"  pip install -e .\n"
          f"  python -c \"from {pkg}.example import say_hello; print(say_hello('Codespaces'))\"")

if __name__ == "__main__":
    main()

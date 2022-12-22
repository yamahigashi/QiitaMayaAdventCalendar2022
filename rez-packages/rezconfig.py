from pathlib import Path

directory = Path(__file__).parent
base = Path(directory)
package_files = list(base.rglob("package.py"))
candidates = set([x.parent.parent.parent.as_posix() for x in package_files])


packages_path = [
]

packages_path.extend(candidates)

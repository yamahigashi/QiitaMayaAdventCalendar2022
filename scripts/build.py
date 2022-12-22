import sys
import os
import pathlib
from datetime import datetime
import shutil


if sys.version_info >= (3, 0):
    # For type annotation
    from typing import (  # NOQA: F401 pylint: disable=unused-import
        TYPE_CHECKING,
    )

    if TYPE_CHECKING:
        from typing import (  # NOQA: F401 pylint: disable=unused-import
            Optional,
            Dict,
            List,
            Tuple,
            Pattern,
            Callable,
            Any,
            Text,
            Generator,
            Union
        )
        from pathlib import Path  # NOQA: F401, F811 pylint: disable=unused-import,reimported


modpath = os.environ.get("AZP_MODULE_PATH")
if not modpath:
    modpath = os.path.abspath(os.path.join(__file__, "../../python"))

sys.path.append(modpath)
REQUIRED_PACKAGES = [
    # "python",
    # "maya==2024",
    "maya==2023",
    "maya==2022",
    "maya==2020",
    "maya==2019",
    "maya==2018",
    "maya==2017",
    "maya_ui_language==0.zh_CN",
    "maya_ui_language==1.ja_JP",
    "maya_ui_language==2.en_US",
]


def ignore_factory():
    # type: () -> Callable
    """Function factory for ignore argument of copytree."""

    common_ignore = [".mypy_cache", ".git", "__pycache__", "*", ".pytest_cache", "*.stats"]

    # def is_dir(path, name):
    #     target = pathlib.Path(path).joinpath(name)
    #     return target.is_dir()

    def custom_ignore(_path, _names):  # noqa
        return common_ignore

    return custom_ignore


def copytree(src, dst, **kwargs):
    try:
        shutil.copytree(src.resolve().as_posix(), dst.resolve().as_posix(), ignore=shutil.ignore_patterns("*.stats", ".mypy_cache", ".git", "__pycache__", ".pytest_cache"))
    except FileExistsError:
        pass


def get_base_path():
    base_path = pathlib.Path(os.path.abspath(__file__)).parent.parent
    return base_path


def get_rez_package_dir():
    base_path = get_base_path()
    package_dir = base_path.joinpath(pathlib.Path("rez-packages"))
    return package_dir


def get_projects(culture):
    # type: (Text) -> List[Text]
    package_dir = get_rez_package_dir().joinpath(culture)

    if package_dir.exists():
        package_files = list(package_dir.rglob("package.py"))
        candidates = set([x.parent.parent.name for x in package_files])
        print("projects is {}".format(candidates))

        return candidates

    else:
        packages = get_rez_package_dir().rglob("{}/*/package.py".format(culture))
        candidates = set([x.parent.parent.name for x in packages])
        print("projects is {}".format(candidates))

        return candidates


def get_dependency(pkg):
    from rez.status import status
    from rez.resolved_context import ResolvedContext

    import pathlib
    import shutil

    context = ResolvedContext(package_requests=[pkg])
    paths = []

    private_reqs = []
    for _pkg in context.resolved_packages:
        pkg_path = pathlib.Path(_pkg.uri)
        src_path = pkg_path.parent
        paths.append(src_path)
        privates = _pkg.get_requires(private_build_requires=True)
        private_reqs.extend(privates)

    private_reqs= [str(x).lstrip("~") for x in private_reqs]
    context = ResolvedContext(package_requests=private_reqs, print_stats=False)

    for _pkg in context.resolved_packages:
        pkg_path = pathlib.Path(_pkg.uri)
        src_path = pkg_path.parent
        paths.append(src_path)

    return paths


def copy_packages(build_path, culture):

    base_path = pathlib.Path(os.path.abspath(__file__)).parent.parent
    if not build_path.exists():
        os.makedirs(build_path.as_posix())

    all_packages = []
    for proj in get_projects(culture):
        all_packages.extend(get_dependency(proj))

    for add in REQUIRED_PACKAGES:
        all_packages.extend(get_dependency(add))

    all_packages = sorted(list(set(all_packages)))

    for src_path in all_packages:
        dst_path = build_path.joinpath(src_path.relative_to(base_path))
        print("copy package {}".format(src_path))
        copytree(src_path, dst_path)


def copy_rez_basesystem(build_path):

    base_path = pathlib.Path(os.path.abspath(__file__)).parent.parent
    if not build_path.exists():
        os.makedirs(build_path)

    for rez_file in get_rez_package_dir().glob("*"):
        if rez_file.name.startswith("."):
            continue
        if rez_file.is_dir():
            continue
        dst_path = build_path.joinpath(rez_file.relative_to(base_path))
        if not dst_path.parent.exists():
            os.makedirs(dst_path.parent)
        shutil.copyfile(rez_file, dst_path)

    src = base_path.joinpath("bin")
    dst = build_path.joinpath("bin")
    copytree(src, dst, ignore=ignore_factory())

    src = base_path.joinpath("scripts")
    dst = build_path.joinpath("scripts")
    copytree(src, dst, ignore=ignore_factory())


def main():
    date = datetime.now().strftime("%Y%m%d")
    pipeline = pathlib.Path(os.path.abspath(__file__)).parent.parent
    culture = input("input build culture >>  ")

    destination_path = pipeline.parent.joinpath("Pipeline{}_{}".format(date, culture.replace(",", "")))
    # build_path = destination_path.joinpath(datetime.now().strftime("%Y-%m-%d-%H%M"))
    build_path = destination_path

    print("build to %s" % build_path)
    copy_rez_basesystem(build_path)
    for c in culture.split(","):
        copy_packages(build_path, c)


if __name__ == '__main__':
    main()

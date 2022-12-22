import re
import sys
import os

modpath = os.environ.get("AZP_MODULE_PATH")
if not modpath:
    modpath = os.path.abspath(os.path.join(__file__, "../../python"))


sys.path.append(modpath)
import allzpark.cli as cli
def main():
    print("launch allzpark")
    print(os.getenv("REZ_CONFIG_FILE"))
    from allzpark.vendor.Qt import QtWidgets, QtCore
    storage = QtCore.QSettings(QtCore.QSettings.IniFormat,
                               QtCore.QSettings.UserScope,
                               "Allzpark", "preferences")
    print(storage.fileName())
    storage.setValue("showAdvancedControls", True)
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    print(cli.__file__)
    sys.exit(cli.main())


if __name__ == '__main__':
    main()

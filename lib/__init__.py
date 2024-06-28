###########
# IMPORTS #
###########


# OS
import os


########
# CODE #
########


# Add .dll path for the .pyd module (otherwise the FFTW DLL imports will fail when loading .pyd module)
os.add_dll_directory(os.path.join(os.path.dirname(__file__), '3rd_party_libs', 'fftw'))
# Same, but for custom cuda library
os.add_dll_directory(os.path.join(os.path.dirname(__file__), 'cudalib'))
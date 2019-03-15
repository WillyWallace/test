""" Functions for rebinning input data.
"""

x = 2
print(x)

def mira2nc(x):
    """High-level API to convert Mira cloud radar Level 1 file into NetCDF file.

    This function converts raw cloud radar file into a much smaller file that
    contains only the relevant data and can be used in further processing steps.

    Args:
        mmclx_file (str): Raw radar file in NetCDF format.
        output_file (str): Output file name.
        site_properties (dict): Dictionary containing information about the
            site. Required key value pairs are 'name'.
        rebin_data (bool, optional): If True, rebins data to 30s resolution.
            Otherwise keeps the native resolution. Default is False.

    Examples:

    """
    y = x * 2
    return y

print(mira2nc(x))

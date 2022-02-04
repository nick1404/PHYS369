import pandas as pd


def query(filename, types, certainties=[0.9], columns=['ID', 'ra', 'dec']):
    """
    Basic query for Galaxy Zoo 2 data.
    """

    if ".csv" in filename:
        name = filename
    else:
        name = "%s.csv" % (filename)

    loaded_file = pd.read_csv(r'%s' % (name))

    while len(certainties) < len(types):
        certainties.append(certainties[0])

    gz2_col = []

    for type in types:
        if type[0] == "E":
            gz2_col.append("t01_smooth_or_features_a01_smooth_debiased")
        elif type[0] == "S":
            gz2_col.append("t03_bar_a06_bar_debiased")

    df = pd.DataFrame(loaded_file, columns=columns)
    #df_f = df[df.gz2_class.isin(types)]

    dff = pd.DataFrame([])

    for x in range(len(types)):
        dft = df.query('gz2_class.str.startswith("%s") and %s > %s' % (
            types[x], gz2_col[x], certainties[x]), engine="python")

        dff = pd.concat([dff, dft])

    return(dff)


# result = query("gz2_hart16", certainties=[0.95], types=["E"], columns=[
#                'dr7objid', 'ra', 'dec', 'gz2_class', 't01_smooth_or_features_a01_smooth_debiased', 't03_bar_a06_bar_debiased'])
# print(result)

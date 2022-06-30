import decimal
import pandas as pd

array_exp = [15, 11, 8, 5, 8, 8, 5, 4]
array_man = [112, 52, 23, 10, 10, 7, 2, 3]
# decimal.getcontext().prec = 2

df = pd.DataFrame(columns=['Type', 'X_max', 'X_min', 'X_min^s'])
# print("type\tu\t\t\tx_max\t\t\tx_min\t\t\tx_min^s")

for i in range(len(array_exp)):
    exponent = decimal.Decimal(array_exp[i])
    mantissa = decimal.Decimal(array_man[i])
    distribution = 2 ** exponent
    positive = distribution / 2 - 1
    negative = -positive + 1

    precision = 2 ** -(mantissa + 1)
    max_fp = 2 * (2 ** positive)
    min_fp = 1 * (2 ** negative)
    min_fp_sub = 1 * (2 ** (negative - mantissa))
    row = {'Type': "E%dM%d" % (exponent, mantissa), 'X_max': max_fp, 'X_min': min_fp, 'X_min^s': min_fp_sub}
    df.loc[i] = row
    name = ("E%dM%d" % (exponent, mantissa))
    df.rename(index={i: name})
    # print("E%dM%d" % (exponent, mantissa), end="\t")
    # print(precision, end="\t")
    # print(max_fp, end="\t")
    # print(min_fp, end="\t")
    # print(min_fp_sub)

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

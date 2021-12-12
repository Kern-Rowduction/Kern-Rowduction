"""Main script to give examples of use of the Kern_Rowduction package."""

import os
import pandas as pd
import kern_rowduction as krd

if __name__ == '__main__':
    
    # ------------------------- Tutorial -------------------------

    PATH = os.path.dirname(os.path.realpath(__file__)) + "/tests/data/"
    FILENAME = "clean_pima_extract.csv"
    print("----- Tutorial -----", FILENAME)

    df = pd.read_csv(PATH + FILENAME)
    print("df:", len(df), "rows")

    # Kern-rowduct quickly a DataFrame

    krd_df = krd.rowduct(df)
    print("krd_df:", len(krd_df), "rows")

    # Parametrize your Kern-Rowduction

    krd_df_1 = krd.rowduct(df, epsilon = 0.1)
    print("krd_df_1:", len(krd_df_1), "rows")

    krd_df_2 = krd.rowduct(df, rowduction_target=[0], epsilon = 0.1, label_col="Label")
    print("krd_df_2:", len(krd_df_2), "rows")

    krd_df_3 = krd.rowduct(df, rowduction_target=[0], epsilon = 0.1, nb_rows_memory=5, \
        step_activated=True, label_col="Label")
    print("krd_df_3:", len(krd_df_3), "rows")

    del krd_df, krd_df_1, krd_df_2, krd_df_3


    # ------------------------- Other Tests -------------------------

    # Test with a small CSV file

    PATH = os.path.dirname(os.path.realpath(__file__)) + "/tests/data/"
    FILENAME = "clean_pima_extract.csv"
    EPSILON = 0.05
    print("----- Other Tests -----", FILENAME)

    df = pd.read_csv(PATH + FILENAME)
    print(len(df))

    try:
        df2 = krd.apply_kern_rowduction(df, epsilon=EPSILON)
        print("One shot grouped reduction -> ", len(df2), "remaining rows")
    except MemoryError as error:
        print("Memory Error:", error)

    df3 = krd.rowduct(df, [1], EPSILON, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label", rowduction_method = "separately")
    print(df3.head())
    print("Step by step reduction V3 -> ", len(df3), " remaining rows")

    df4 = krd.rowduct(df, epsilon=EPSILON, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label")
    print("Step by step reduction without rowduction target nor method -> ", len(df4), \
        " remaining rows")

    df5 = krd.rowduct(df, epsilon=EPSILON, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    print("One shot grouped reduction without rowduction target -> ", len(df5), \
        " remaining rows")

    # Test with a BIG CSV file

    PATH = os.path.dirname(os.path.realpath(__file__)) + "/tests/data/"
    FILENAME = "clean_adult_extract.csv"
    EPSILON = 0.05
    print("----- Other Tests -----", FILENAME)

    df = pd.read_csv(PATH + FILENAME)
    print(len(df))

    try:
        df2 = krd.apply_kern_rowduction(df, epsilon=EPSILON)
        print("One shot reduction -> ", len(df2), "remaining rows")
    except MemoryError as error:
        print("Memory Error:", error)

    df3 = krd.rowduct(df, [0], EPSILON, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    print("Step by step reduction -> ", len(df3), " remaining rows")

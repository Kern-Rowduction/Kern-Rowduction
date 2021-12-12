"""Units tests on 2 Datasets to detect potential bugs of the Kern_Rowduction package."""

import os
import pandas as pd
import kern_rowduction.rowduction as krd

################## Tests on the Dataset A ##################

def test_rowduction_0_dataset_a(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_pima_extract.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 0 value of the label of the Dataset A.

    Implemented checks :
    -Check if the rowduction reduces the number of rows from the original input df
    -Check if all "one shot" rowductions and rowduction with a
    higher batch size (nb_rows_memory) than the total number of rows give the results
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [0], epsilon, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_12 = krd.rowduct(df, [0], epsilon, nb_rows_memory=50000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_13 = krd.rowduct(df, [0], epsilon, nb_rows_memory=50000, step_activated = False, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_14 = krd.apply_kern_rowduction(df[df["Label"] == 0].reset_index(drop=True), \
        epsilon, nb_rows_memory=50000)
    rowducted_df_14 = rowducted_df_14.append(df[df["Label"] == 1]).reset_index(drop=True)

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [0], epsilon, nb_rows_memory=10000, step_activated = True, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_22 = krd.rowduct(df, [0], epsilon, nb_rows_memory=50000, step_activated = True, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_23 = krd.rowduct(df, [0], epsilon, nb_rows_memory=50000, step_activated = False, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_24 = krd.apply_kern_rowduction(df[df["Label"] == 0].reset_index(drop=True), \
        epsilon, nb_rows_memory=50000)
    rowducted_df_24 = rowducted_df_24.append(df[df["Label"] == 1]).reset_index(drop=True)

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)
    assert len(rowducted_df_12) < len(df)
    assert len(rowducted_df_13) < len(df)
    assert len(rowducted_df_14) < len(df)

    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_11) == len(rowducted_df_12)
    assert len(rowducted_df_12) == len(rowducted_df_13)
    assert len(rowducted_df_13) == len(rowducted_df_14)
    # In terms of rowducted dataframe
    assert (rowducted_df_11 != rowducted_df_12).any(1).count() == len(rowducted_df_12)
    assert (rowducted_df_12 != rowducted_df_13).any(1).count() == len(rowducted_df_13)
    assert (rowducted_df_13 != rowducted_df_14).any(1).count() == len(rowducted_df_14)

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)
    assert len(rowducted_df_22) < len(df)
    assert len(rowducted_df_23) < len(df)
    assert len(rowducted_df_24) < len(df)
    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_21) == len(rowducted_df_22)
    assert len(rowducted_df_22) == len(rowducted_df_23)
    assert len(rowducted_df_23) == len(rowducted_df_24)
    # In terms of rowducted dataframe
    assert (rowducted_df_21 != rowducted_df_22).any(1).count() == len(rowducted_df_22)
    assert (rowducted_df_22 != rowducted_df_23).any(1).count() == len(rowducted_df_23)
    assert (rowducted_df_23 != rowducted_df_24).any(1).count() == len(rowducted_df_24)

def test_rowduction_1_dataset_a(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_pima_extract.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 1 value of the label of the Dataset A.

    Implemented checks :
    -Check if the rowduction reduces the number of rows from the original input df
    -Check if all "one shot" rowductions and rowduction with a
    higher batch size (nb_rows_memory) than the total number of rows give the results
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [1], epsilon, nb_rows_memory=7000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_12 = krd.rowduct(df, [1], epsilon, nb_rows_memory=32000, step_activated = True, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_13 = krd.rowduct(df, [1], epsilon, nb_rows_memory=32000, step_activated = False, \
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_14 = krd.apply_kern_rowduction(df[df["Label"] == 1].reset_index(drop=True),  \
        epsilon, nb_rows_memory=32000)
    rowducted_df_14 = rowducted_df_14.append(df[df["Label"] == 0]).reset_index(drop=True)

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [1], epsilon, nb_rows_memory=7000, step_activated = True, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_22 = krd.rowduct(df, [1], epsilon, nb_rows_memory=32000, step_activated = True, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_23 = krd.rowduct(df, [1], epsilon, nb_rows_memory=32000, step_activated = False, \
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_24 = krd.apply_kern_rowduction(df[df["Label"] == 1].reset_index(drop=True), \
        epsilon, nb_rows_memory=32000)
    rowducted_df_24 = rowducted_df_24.append(df[df["Label"] == 0]).reset_index(drop=True)

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)
    assert len(rowducted_df_12) < len(df)
    assert len(rowducted_df_13) < len(df)
    assert len(rowducted_df_14) < len(df)
    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_11) == len(rowducted_df_12)
    assert len(rowducted_df_12) == len(rowducted_df_13)
    assert len(rowducted_df_13) == len(rowducted_df_14)
    # In terms of rowducted dataframe
    assert (rowducted_df_11 != rowducted_df_12).any(1).count() == len(rowducted_df_12)
    assert (rowducted_df_12 != rowducted_df_13).any(1).count() == len(rowducted_df_13)
    assert (rowducted_df_13 != rowducted_df_14).any(1).count() == len(rowducted_df_14)

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)
    assert len(rowducted_df_22) < len(df)
    assert len(rowducted_df_23) < len(df)
    assert len(rowducted_df_24) < len(df)
    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_21) == len(rowducted_df_22)
    assert len(rowducted_df_22) == len(rowducted_df_23)
    assert len(rowducted_df_23) == len(rowducted_df_24)
    # In terms of rowducted dataframe
    assert (rowducted_df_21 != rowducted_df_22).any(1).count() == len(rowducted_df_22)
    assert (rowducted_df_22 != rowducted_df_23).any(1).count() == len(rowducted_df_23)
    assert (rowducted_df_23 != rowducted_df_24).any(1).count() == len(rowducted_df_24)

def test_rowduction_01_dataset_a(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_pima_extract.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 0 and 1 values of the label of the Dataset A.

    Implemented checks :
        -Check if the rowduction reduces the number of rows from the original input df
        -Check if all "one shot" rowductions and rowduction with a
        higher batch size (nb_rows_memory) than the total number of rows give the results
        -Check if rowduct(...) and apply_kern_rowduction(...) give same results when
        the parameters are similar
        -Check if it gives the same reduced results with no rowduction_target or equal to "all"
        -Check if it gives the same reduced results with no label_col (nor rowduction_target) \
            and whatever the rowduction_method
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=4000, \
        step_activated = True, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_11bis = krd.rowduct(df, "all", epsilon, nb_rows_memory=4000, \
        step_activated = True, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_12 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=73000, \
        step_activated = True, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_13 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_13bis = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_14 = krd.apply_kern_rowduction(df, epsilon, \
        nb_rows_memory=73000).reset_index(drop=True)
    rowducted_df_15 = krd.rowduct(df, "all", epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_16 = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_17 = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=73000, \
        step_activated = False, rowduction_method = "grouped")
    # Since the label_col is by default below, only 1 "separated" value is chosen as target
    rowducted_df_17b = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=73000, \
        step_activated = False, rowduction_method = "separately")

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=4000, \
        step_activated = True, label_col = "Label", rowduction_method = "separately")
    rowducted_df_21bis = krd.rowduct(df, "all", epsilon, nb_rows_memory=4000, \
        step_activated = True, label_col = "Label", rowduction_method = "separately")
    rowducted_df_22 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=73000, \
        step_activated = True, label_col = "Label", rowduction_method = "separately")
    rowducted_df_23 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "separately")
    rowducted_df_23bis = krd.rowduct(df, "all", epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "separately")
    rowducted_df_24a = krd.apply_kern_rowduction(df[df["Label"] == 0].reset_index(drop=True), \
        epsilon, nb_rows_memory=32000)
    rowducted_df_24b = krd.apply_kern_rowduction(df[df["Label"] == 1].reset_index(drop=True), \
        epsilon, nb_rows_memory=32000)
    rowducted_df_24 = rowducted_df_24a.append(rowducted_df_24b).reset_index(drop=True)
    rowducted_df_25 = krd.rowduct(df, rowduction_target="all", epsilon=epsilon, \
        nb_rows_memory=73000, step_activated = False, label_col = "Label", \
        rowduction_method = "separately")
    rowducted_df_26 = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=73000, \
        step_activated = False, label_col = "Label", rowduction_method = "separately")

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)
    assert len(rowducted_df_11bis) < len(df)
    assert len(rowducted_df_12) < len(df)
    assert len(rowducted_df_13) < len(df)
    assert len(rowducted_df_13bis) < len(df)
    assert len(rowducted_df_14) < len(df)
    assert len(rowducted_df_15) < len(df)
    assert len(rowducted_df_16) < len(df)
    assert len(rowducted_df_17) < len(df)

    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_11) == len(rowducted_df_12)
    assert len(rowducted_df_11bis) == len(rowducted_df_12)
    assert len(rowducted_df_11) == len(rowducted_df_11bis)
    assert len(rowducted_df_12) == len(rowducted_df_13)
    assert len(rowducted_df_13) == len(rowducted_df_14)
    assert len(rowducted_df_13bis) == len(rowducted_df_14)
    assert len(rowducted_df_13) == len(rowducted_df_13bis)
    assert len(rowducted_df_14) == len(rowducted_df_15)
    assert len(rowducted_df_15) == len(rowducted_df_16)
    assert len(rowducted_df_16) == len(rowducted_df_17)
    assert len(rowducted_df_17) == len(rowducted_df_17b)

    # In terms of rowducted dataframe
    assert (rowducted_df_11 != rowducted_df_12).any(1).count() == len(rowducted_df_12)
    assert (rowducted_df_11bis != rowducted_df_12).any(1).count() == len(rowducted_df_12)
    assert (rowducted_df_11 != rowducted_df_11bis).any(1).count() == len(rowducted_df_11bis)
    assert (rowducted_df_12 != rowducted_df_13).any(1).count() == len(rowducted_df_13)
    assert (rowducted_df_13 != rowducted_df_14).any(1).count() == len(rowducted_df_14)
    assert (rowducted_df_13bis != rowducted_df_14).any(1).count() == len(rowducted_df_14)
    assert (rowducted_df_13 != rowducted_df_13bis).any(1).count() == len(rowducted_df_13bis)
    assert (rowducted_df_14 != rowducted_df_15).any(1).count() == len(rowducted_df_15)
    assert (rowducted_df_15 != rowducted_df_16).any(1).count() == len(rowducted_df_16)
    assert (rowducted_df_16 != rowducted_df_17).any(1).count() == len(rowducted_df_17)
    assert (rowducted_df_17 != rowducted_df_17b).any(1).count() == len(rowducted_df_17b)


    del rowducted_df_11, rowducted_df_11bis, rowducted_df_12, rowducted_df_13, \
        rowducted_df_13bis, rowducted_df_14, rowducted_df_15, rowducted_df_16, \
        rowducted_df_17

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)
    assert len(rowducted_df_21bis) < len(df)
    assert len(rowducted_df_22) < len(df)
    assert len(rowducted_df_23) < len(df)
    assert len(rowducted_df_23bis) < len(df)
    assert len(rowducted_df_24) < len(df)
    assert len(rowducted_df_25) < len(df)
    assert len(rowducted_df_26) < len(df)

    # Check if the various rowduction parameters lead to a "one shot rowduction"
        # and so the same results
    # In terms of number of rows
    assert len(rowducted_df_21) == len(rowducted_df_22)
    assert len(rowducted_df_21bis) == len(rowducted_df_22)
    assert len(rowducted_df_21) == len(rowducted_df_21bis)
    assert len(rowducted_df_22) == len(rowducted_df_23)
    assert len(rowducted_df_23) == len(rowducted_df_24)
    assert len(rowducted_df_23bis) == len(rowducted_df_24)
    assert len(rowducted_df_23) == len(rowducted_df_23bis)
    assert len(rowducted_df_24) == len(rowducted_df_25)
    assert len(rowducted_df_25) == len(rowducted_df_26)

    # In terms of rowducted dataframe
    assert (rowducted_df_21 != rowducted_df_22).any(1).count() == len(rowducted_df_22)
    assert (rowducted_df_21bis != rowducted_df_22).any(1).count() == len(rowducted_df_22)
    assert (rowducted_df_21 != rowducted_df_21bis).any(1).count() == len(rowducted_df_21bis)
    assert (rowducted_df_22 != rowducted_df_23).any(1).count() == len(rowducted_df_23)
    assert (rowducted_df_23 != rowducted_df_24).any(1).count() == len(rowducted_df_24)
    assert (rowducted_df_23bis != rowducted_df_24).any(1).count() == len(rowducted_df_24)
    assert (rowducted_df_23 != rowducted_df_23bis).any(1).count() == len(rowducted_df_23bis)
    assert (rowducted_df_24 != rowducted_df_25).any(1).count() == len(rowducted_df_25)
    assert (rowducted_df_25 != rowducted_df_26).any(1).count() == len(rowducted_df_26)

    del rowducted_df_21, rowducted_df_21bis, rowducted_df_22, rowducted_df_23, \
        rowducted_df_23bis, rowducted_df_24a, rowducted_df_24b, rowducted_df_24, \
        rowducted_df_25, rowducted_df_26

################## Tests on the Dataset B ##################

def test_rowduction_0_dataset_b(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_adult_extract.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 0 value of the label of the Dataset B. There are less tests than
    with Dataset A because the DF is too heavy to "one shot" rowduct it.

    Implemented checks :
        -Check if the rowduction reduces the number of rows from the original input df
        -Check if the step by step rowduction works and avoid the memory error due to a too large df
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [0], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "grouped")

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [0], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "separately")


    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)

    del rowducted_df_11, rowducted_df_21


def test_rowduction_1_dataset_b(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_adult_extract.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 0 value of the label of the Dataset B. There are less tests than
    with Dataset A because the DF is too heavy to "one shot" rowduct it.

    Implemented checks :
        -Check if the rowduction reduces the number of rows from the original input df
        -Check if the step by step rowduction works and avoid the memory error due to a too large df
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [1], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "grouped")

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [1], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "separately")

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)

    del rowducted_df_11, rowducted_df_21

def test_rowduction_01_dataset_b(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_adult_extract.csv",
    epsilon = 0.052
    ):
    """Test the rowduction on a 0 and 1 values of the label of the Dataset B. There are less tests
       than with Dataset A because the DF is too heavy to "one shot" rowduct it.

    Implemented checks :
        -Check if the rowduction reduces the number of rows from the original input df
        -Check if the step by step rowduction works and avoid the memory error due to a too large df
    """

    # Load the data
    df = pd.read_csv(path)

    # Rowduct the data in a "grouped" way
    rowducted_df_11 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "grouped")
    rowducted_df_12 = krd.rowduct(df, "all", epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "grouped")

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [0,1], epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "separately")
    rowducted_df_22 = krd.rowduct(df, "all", epsilon, nb_rows_memory=500, step_activated = True,\
        label_col = "Label", rowduction_method = "separately")

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)
    assert len(rowducted_df_12) < len(df)
    assert len(rowducted_df_11) == len(rowducted_df_12)

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)
    assert len(rowducted_df_22) < len(df)
    assert len(rowducted_df_21) == len(rowducted_df_22)

    del rowducted_df_11, rowducted_df_12, rowducted_df_21, rowducted_df_22

################## Tests on the Dataset C ##################

def test_rowduction_dataset_c(
    path = os.path.dirname(os.path.realpath(__file__)) + "/data/clean_abalone.csv",
    epsilon = 0.05
    ):
    """Test the rowduction on a 0 and 1 values of the label of the Dataset B. There are less tests
       than with Dataset A because the DF is too heavy to "one shot" rowduct it.

    Implemented checks :
        -Check if the rowduction reduces the number of rows from the original input df
        -Check if the rowduction for a multiclass dataset reduces the rows with the given \
            rowduction_target but not the others
       -Check if the rowduction with all the classes as target (and even more than the ones that \
           actually exist) is equivalent to an "all" rowduction
    """

    # Load the data
    df = pd.read_csv(path)
    print(df["Label"])

    # Rowduct the data in a "grouped" way
        # On specific targets
    rowducted_df_11 = krd.rowduct(df, [10, 11, 12], epsilon, nb_rows_memory=10000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_12a = krd.apply_kern_rowduction(\
        df[df["Label"].isin([10,11,12])].reset_index(drop=True), epsilon, nb_rows_memory=10000
        )
    rowducted_df_12b = df[~df["Label"].isin([10,11,12])]
    rowducted_df_12 = rowducted_df_12a.append(rowducted_df_12b).sample(frac=1)
        # On all targets
    rowducted_df_13 = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=10000, \
        step_activated = False, label_col = "Label", rowduction_method = "grouped")
    rowducted_df_14 = krd.rowduct(df, rowduction_target=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], \
        epsilon=epsilon, nb_rows_memory=10000, step_activated = False, label_col = "Label", \
        rowduction_method = "grouped")

    # Test the "grouped" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_11) < len(df)
    assert len(rowducted_df_12) < len(df)
    assert len(rowducted_df_13) < len(df)
    assert len(rowducted_df_14) < len(df)
    # Check if the "targeting" works as independent rowductions
    assert len(rowducted_df_11) == len(rowducted_df_12)
    assert len(rowducted_df_11[rowducted_df_11["Label"].isin([10,11,12])]) == len(rowducted_df_12a)
    assert len(rowducted_df_11[~rowducted_df_11["Label"].isin([10,11,12])]) == len(rowducted_df_12b)
     # Check if the rowductions remains the same whether all classes
     # or "all" are the rowduction_target
    assert len(rowducted_df_13) == len(rowducted_df_14)

    del rowducted_df_11, rowducted_df_12a, rowducted_df_12b, rowducted_df_12, rowducted_df_13, \
        rowducted_df_14

    # Rowduct the data "separately"
    rowducted_df_21 = krd.rowduct(df, [10, 11, 12], epsilon, nb_rows_memory=10000, \
        step_activated = True, label_col = "Label", rowduction_method = "separately")
    rowducted_df_22a = krd.apply_kern_rowduction(df[df["Label"] == 10].reset_index(drop=True), \
        epsilon, nb_rows_memory=10000)
    rowducted_df_22b = krd.apply_kern_rowduction(df[df["Label"] == 11].reset_index(drop=True), \
        epsilon, nb_rows_memory=10000)
    rowducted_df_22c = krd.apply_kern_rowduction(df[df["Label"] == 12].reset_index(drop=True), \
        epsilon, nb_rows_memory=10000)
    rowducted_df_22d = df[~df["Label"].isin([10,11,12])]
    rowducted_df_22 = rowducted_df_22a.append(rowducted_df_22b).append(
        rowducted_df_22c).append(rowducted_df_22d).sample(frac=1)
    rowducted_df_23 = krd.rowduct(df, epsilon=epsilon, nb_rows_memory=10000, \
        step_activated = False, label_col = "Label", rowduction_method = "separately")
    rowducted_df_24 = krd.rowduct(df, rowduction_target=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], \
        epsilon=epsilon, nb_rows_memory=10000, step_activated = False, label_col = "Label", \
        rowduction_method = "separately")

    # Test the "separately" Rowduction

    # Check if the rowduction reduces the number of rows
    assert len(rowducted_df_21) < len(df)
    assert len(rowducted_df_22) < len(df)
    assert len(rowducted_df_23) < len(df)
    assert len(rowducted_df_24) < len(df)
    # Check if the "targeting" works as independent rowductions
    assert len(rowducted_df_21) == len(rowducted_df_22)
    assert len(rowducted_df_21[rowducted_df_21["Label"].isin([10,11,12])]) == len(rowducted_df_22a)\
        + len(rowducted_df_22b) + len(rowducted_df_22c)
    assert len(rowducted_df_21[~rowducted_df_21["Label"].isin([10,11,12])]) == len(rowducted_df_22d)
     # Check if the rowductions remains the same whether all classes
     # or "all" are the rowduction_target
    assert len(rowducted_df_23) == len(rowducted_df_24)

    del rowducted_df_21, rowducted_df_22a, rowducted_df_22b, rowducted_df_22c, rowducted_df_22d, \
        rowducted_df_22, rowducted_df_23, rowducted_df_24

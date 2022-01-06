Tutorial
========

Kern-rowduct quickly a DataFrame
--------------------------------

First load as a Pandas DataFrame your 'FILENAME' CSV stored in a given 'PATH':

.. code-block:: python

    PATH = "your_given_path_where_the_file_is_stored/"
    FILENAME = "my_file.csv"
    df = pd.read_csv(PATH + FILENAME)

It works with other type of files : Excel xlsx, SAS sas7bdat etc...
The file just needs to be loaded as a pandas DataFrame. More information at : https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html.

Then, you can apply the Kern-Rowduction with the default parameters:

.. code-block:: python

    import kern_rowduction as krd

    krd_df = krd.rowduct(df)

Now you have your kern-rowducted DataFrame krd_df, which normally has less rows than df.

Parametrize your Kern-Rowduction
--------------------------------

First load as a Pandas DataFrame your 'FILENAME' CSV stored in a given 'PATH':

.. code-block:: python

    PATH = "your_given_path_where_the_file_is_stored/"
    FILENAME = "my_file.csv"
    df = pd.read_csv(PATH + FILENAME)

**Set the Epsilon dominance rate**

Then, you can apply the Kern-Rowduction and set the epsilon dominance threshold/rate on 0.1:

.. code-block:: python

    import kern_rowduction as krd

    krd_df_1 = krd.rowduct(df, epsilon = 0.1)

If you're DataFrame is large enough, you would probably notice a difference of number of rows if you test several values of epsilon.

**How to choose the right value of epsilon?**

The higher you set up the epsilon value, the more relaxation you apply to the dominance formula. This will lead to a large number of deleted data and a smaller number of kept data. We generally recommend not to exceed a 0.5 value for epsilon especially if you have standardised your data. If you have non-standardised data, don’t hesitate to try higher values for epsilon (like 1 ;2 ;3 etc.)

**Target the rows to kern-rowduct**

If a given column 'class' has the possible following values : ["A","B","C","D"], you can also
apply the Kern-Rowduction and choose the rows to kern-rowduct according to their label column value of "A" or "B":

.. code-block:: python

    import kern_rowduction as krd

    krd_df_2 = krd.rowduct(df, rowduction_target=["A","B"], epsilon = 0.1, label_col="class")

Normally the rows of df where their column 'class' equals 'C' or 'D' should remain unchanged. 
Only the number of rows with 'class'='A' or 'class'='B' should have been reduced. Feel free to try other 'rowduction_target' or
another column as 'label_col', so long it is an ordinal or categorical variable.

**Deal with too large DataFrames: avoid memory errors**

If the dataset is too large for the CPU/GPU memory when using the rowduct() method, it is possible to 'kern-rowduct' the DataFrame df 
with a given batch size of 1000 rows to process step by step in order to avoid a MemoryError:

.. code-block:: python

    import kern_rowduction as krd
    
    krd_df_3 = krd.rowduct(df, rowduction_target=["A","B"], epsilon = 0.1, nb_rows_memory=1000, step_activated=True, label_col="class")

If you change the value of 'nb_rows_memory', the batch size will be different and the final rowducted DataFrame 'krd_df_3' too.

*Nota Bene 1*: If the 'nb_rows_memory' is superior to the number of actual rows in df or if 'step_activated'=False, the Kern-Rowduction will be applied 
in one shot on the whole DataFrame df.

*Nota Bene 2*: When the Kern-Rowduction is computing, a progress bar is showed in the console.

Now you have your kern-rowducted DataFrame krd_df_1, krd_df_2, krd_df_3, which normally have less rows than df.
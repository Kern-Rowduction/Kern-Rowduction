Source Code Documentation
=========================

Kern Rowduction Package
-----------------------

.. automodule:: kern_rowduction.rowduction
   :members:
   :undoc-members:
   :show-inheritance:

Unit Tests
----------

.. automodule:: tests.test_rowduction
   :members:
   :undoc-members:
   :show-inheritance:

Main / Examples
---------------

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance:

::

      # Import the CSV file as a pandas DataFrame
      import os
      import pandas as pd
      import kern_rowduction.rowduction as krd

      PATH = os.path.dirname(os.path.realpath(__file__)) + "/tests/data/"
      FILENAME = "clean_pima_train.csv"
      EPSILON = 0.05
      print("-----", FILENAME)

      df = pd.read_csv(PATH + FILENAME)
      print(len(df))

      # Try to kern rowduct the DataFrame in "one shot"
      try:
         df2 = krd.rowduct_df(df, EPSILON)
         print("One shot reduction -> ", len(df2), "remaining rows")
      except MemoryError as error:
         print("Memory Error:", error)

      # Kern rowduct the DataFrame by step batches of 10000 rows => it avoids the memory error bug 
      df3 = krd.rowduct(df, EPSILON, [1], nb_rows_memory=10000, step_activated = True, \
         label_col = "Label", rowduction_method = "separately")
      print("Step by step reduction V3 -> ", len(df3), " remaining rows")

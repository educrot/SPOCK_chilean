.. _pythontuto:

Python use
=========

In this tutorial you will learn how to use |SPOCK_chilean| to create and check ACP plans for SSO observations

Create and Check plans
^^^^^^^^^^^^^^^^^

.. jupyter-execute::

    import ipywidgets as w
    from IPython.display import display
    import pandas as pd
    from SPOCK_chilean.make_night_plans import chilean_time

    # set in advance with the planning with SSO team
    telescope = 'Ganymede'

    date = '2020-05-26' # start of night date
    chilean_nb_target = 1 # number of target to observe this night
    counts = 5000 #counts of images per targets (no limit = 5000)
    chilean_plans = chilean_time('2020-05-26')
    target_chilean = pd.DataFrame({'Date': date, 'Telescope': telescope, 'Name': 'Ch_1',
                                   'Start': '2020-05-27 00:30:00.000', 'End': '2020-05-27 03:00:00.000',
                                   'RA': 181.8609974 , \
                                   'DEC': -52.7885865, 'Filter': 'I+z',
                                   'texp': 20, \
                                   'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id','Jmag':11.8,'SpT':'M4'},
                                  index=[0])

    chilean_plans.make_plans(target_chilean)

    chilean_plans.check_plans()


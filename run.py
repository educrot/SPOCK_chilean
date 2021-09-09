import pandas as pd
from SPOCK_chilean.make_night_plans import chilean_time
import SPOCK_chilean.ETC as ETC

# set in advance with the planning with SSO team
telescope = 'Callisto'

date = '2021-09-09'  # start of night date
chilean_nb_target = 2  # number of target to observe this night
counts = 5000  # counts of images per targets (no limit = 5000)
chilean_plans = chilean_time(date, telescope)

# target_chilean = pd.DataFrame({'Date': date, 'Telescope': telescope, 'Name': 'ch_WD_2138-332',
#                                'Start': '2021-09-02 21:30:00.000',
#                                'End': '2021-09-03 08:00:00.000',
#                                'RA':  325.4898548,
#                                'DEC': -33.0082781, 'Filter': 'g\'',
#                                'texp': 1000,
#                                'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Jmag': 14.167,
#                                'Vmag': 14.47, 'SpT': 'WD'},
#                               index=[0])
# if chilean_nb_target > 1:
#     other_target = {'Date': date, 'Telescope': telescope, 'Name': 'ch_SDSS_J003708.42-052532.8',
#                     'Start': '2021-09-03 08:00:00.000',
#                     'End': '2021-09-03 11:00:00.000',
#                     'RA':  9.2850942,
#                     'DEC': -5.4257810,
#                     'Filter': 'g\'',
#                     'texp': 600,
#                     'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Jmag': 19, 'SpT': 'A0'}
#     target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)
#
# chilean_plans.make_night_block(target_chilean)

chilean_plans.check_night_blocks()


print()





# target_chilean = pd.DataFrame({'Date': date, 'Telescope': telescope, 'Name': 'OGLE-TR-211',
#                                'Start': '2021-07-22 23:50:00.000',
#                                'End': '2021-07-23 03:30:00.000',
#                                'RA':  160.0599273,
#                                'DEC': -62.4555608, 'Filter': 'r\'',
#                                'texp': 40,
#                                'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Vmag': 14.3, 'SpT': 'F8'},
#                               index=[0])
# if chilean_nb_target > 1:
#     other_target = {'Date': date, 'Telescope': telescope, 'Name': 'WASP-46',
#                     'Start': '2021-07-23 03:30:00.000',
#                     'End': '2021-07-23 10:30:00.000',
#                     'RA':  318.7369152,
#                     'DEC': -55.8717944,
#                     'Filter': 'r\'',
#                     'texp': 10,
#                     'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Vmag': 12.9, 'SpT': 'G5'}
#     target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)













# set in advance with the planning of the chilean nights
telescope = 'Ganymede'

date = '2020-05-26'
chilean_nb_target = 1
counts = 5000
chilean_plans = chilean_time('2020-05-26')


target_chilean = pd.DataFrame({'Date': date, 'Telescope': telescope, 'Name': 'Ch_1',
                               'Start': '2020-05-27 00:30:00.000', 'End': '2020-05-27 03:00:00.000',
                               'RA': 181.8609974 , \
                               'DEC': -52.7885865, 'Filter': 'I+z',
                               'texp': 20, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id','Jmag':11.8,'SpT':'M4'},
                              index=[0])

if chilean_nb_target > 1:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 2:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 3:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 4:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 5:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 6:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 7:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 8:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

if chilean_nb_target > 9:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_2',
                               'Start': '2020-01-31 05:30:00.000', 'End': '2020-01-31 06:00:00.000',
                               'RA': 79.4074682 , \
                               'DEC': -33.8175201, 'Filter': 'r\'',
                               'texp': 10, \
                               'Counts': counts, '#target': 1,'Gaia_ID':'gaia_id'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

chilean_plans.make_plans(target_chilean)
chilean_plans.check_plans()


print()


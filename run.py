import pandas as pd
from SPOCK_chilean.make_night_plans import chilean_time
import SPOCK_chilean.ETC as ETC

# set in advance with the planning with SSO team
telescope = 'Ganymede'

date = '2021-07-08'  # start of night date
chilean_nb_target = 2  # number of target to observe this night
counts = 5000  # counts of images per targets (no limit = 5000)
chilean_plans = chilean_time(date, telescope)

target_chilean = pd.DataFrame({'Date': date, 'Telescope': telescope, 'Name': 'Ch_HATS-20',
                               'Start': '2021-07-08 22:30:00.000',
                               'End': '2021-07-09 03:30:00.000',
                               'RA':   198.1329246,
                               'DEC': -45.5905664, 'Filter': 'r\'',
                               'texp': 30,
                               'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Vmag': 13.77, 'SpT': 'G0'},
                              index=[0])
if chilean_nb_target > 1:
    other_target = {'Date': date, 'Telescope': telescope, 'Name': 'Ch_OGLE-TR-10',
                    'Start': '2021-07-09 03:30:00.000',
                    'End': '2021-07-09 11:00:00.000',
                    'RA':  267.8677458,
                    'DEC': -29.8764535,
                    'Filter': 'I+z',
                    'texp': 60,
                    'Counts': counts, '#target': 1, 'Gaia_ID': 'gaia_id', 'Vmag': 15.78, 'SpT': 'F5'}
    target_chilean = target_chilean.append(other_target, ignore_index=True, sort=False)

chilean_plans.make_night_block(target_chilean)

chilean_plans.check_night_blocks()


print()



















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


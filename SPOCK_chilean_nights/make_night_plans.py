from astropy.time import Time
from astropy.coordinates import SkyCoord,EarthLocation
from astroplan import FixedTarget,is_observable,AltitudeConstraint, MoonSeparationConstraint,AtNightConstraint
from astroplan import Observer,moon_illumination,is_always_observable
from astropy import units as u
from astroquery.mast import Catalogs
import datetime
import os
import sys
import shutil
import numpy as np
import pandas as pd
import SPOCK_chilean_nights.ETC as ETC
from SPOCK_chilean_nights.txt_files import startup, flatexo_gany, flatexo_io, flatexo_euro, flatexo_calli
from SPOCK_chilean_nights.txt_files import first_target, flatdawn, biasdark
from astropy.utils import iers
#iers.IERS_A_URL  ='ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.all'
#from astroplan import download_IERS_A
#download_IERS_A()


class chilean_time:
    """ Create and check ACP plans for 10% of SSO's on-sky-time dedicated to chilean observations

    """

    def __init__(self,start_date):
        """

        Parameters
        ----------
        start_date : date
        """

        self.start_date = start_date
        self.Path = './Plans_by_date/' + str(Time(start_date, out_subfmt='date').value)
        self.location = EarthLocation.from_geodetic(-70.40300000000002 * u.deg, -24.625199999999996 * u.deg,2635.0000000009704 * u.m)
        self.observatory = Observer(location=self.location, name="SSO", timezone="UTC")
        self.time_start = None
        self.time_end = None

    def make_plans(self,target_chilean):
        """ Make plans from basic information of each target

        Parameters
        ----------
        target_chilean : pd.DataFrame

        Returns
        -------
        txt files
            set of ACP format file required for the observations

        """

        try:
            os.mkdir(self.Path)
        except FileExistsError:
            print('INFO: File for date ' + str(Time(self.start_date, out_subfmt='date')) + ' exists, overwriting')
            shutil.rmtree(self.Path)
            os.mkdir(self.Path)

        # constants
        autofocus = None
        waitlimit = 600
        afinterval = 60
        filters_used = []

        # sun  rise and sun set
        t_day_15 = Time(datetime.datetime.strptime(self.start_date, '%Y-%m-%d')+datetime.timedelta(hours=15))
        sun_set = self.observatory.sun_set_time(t_day_15, which='next')
        sun_rise = self.observatory.sun_rise_time(t_day_15, which='next')

        for i in range(0, len(target_chilean)):
            if i<(len(target_chilean)-1):
                chain = target_chilean['Name'][i+1]
            else:
                chain = None

            if target_chilean['texp'][i] == 0:
                texp = self.etc_chilean(target_chilean['Jmag'][i],target_chilean['SpT'][i],
                                        filt=target_chilean['Filter'][i])
            else:
                texp = target_chilean['texp'][i]

            coords = SkyCoord(frame='icrs', ra=target_chilean['RA'][i], dec=target_chilean['DEC'][i],
                              unit=(u.deg, u.deg), obstime=Time(self.start_date).iso)
            if i == 0:
                self.time_start = Time(target_chilean['Start'][0]).iso
                self.time_end = Time(target_chilean['End'][0]).iso

                if 'Io' in target_chilean['Telescope'][0]:
                    startup(target_chilean['Name'][0], sun_set.iso, self.time_start, self.Path)
                    first_target(target_chilean['Name'][0], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                 target_chilean['Counts'][0], target_chilean['Filter'][0], texp,
                                 coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                 coords.dec.dms[2], chain, target_chilean['Gaia_ID'][0], self.Path)
                if 'Europa' in target_chilean['Telescope'][0]:
                    startup(target_chilean['Name'][0], sun_set.iso, self.time_start, self.Path)
                    first_target(target_chilean['Name'][0], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                 target_chilean['Counts'][0], target_chilean['Filter'][0],texp,
                                 coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                 coords.dec.dms[2], chain, target_chilean['Gaia_ID'][0], self.Path)
                if 'Ganymede' in target_chilean['Telescope'][0]:
                    startup(target_chilean['Name'][0], sun_set.iso, self.time_start, self.Path)
                    first_target(target_chilean['Name'][0], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                 target_chilean['Counts'][0], target_chilean['Filter'][0], texp,
                                 coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                 coords.dec.dms[2], chain, target_chilean['Gaia_ID'][0], self.Path)
                if 'Callisto' in target_chilean['Telescope'][0]:
                    startup(target_chilean['Name'][0], sun_set.iso, self.time_start, self.Path)
                    first_target( target_chilean['Name'][0], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                 target_chilean['Counts'][0], target_chilean['Filter'][0], texp,
                                 coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                 coords.dec.dms[2], chain, target_chilean['Gaia_ID'][0], self.Path)

            if i > 0:
                self.time_start = Time(target_chilean['Start'][i]).iso
                self.time_end = Time(target_chilean['End'][i]).iso

                if i < (len(target_chilean) - 1):
                    first_target(target_chilean['Name'][i], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                    target_chilean['Counts'][i], target_chilean['Filter'][i], texp,
                                    coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                    coords.dec.dms[2], target_chilean['Name'][i + 1],target_chilean['Gaia_ID'][i], self.Path)

                if i == len(target_chilean) - 1:
                    first_target(target_chilean['Name'][i], self.time_start, self.time_end, waitlimit, afinterval, autofocus,
                                target_chilean['Counts'][i], target_chilean['Filter'][i],texp,
                                coords.ra.hms[0], coords.ra.hms[1], coords.ra.hms[2], coords.dec.dms[0], coords.dec.dms[1],
                                coords.dec.dms[2], None,target_chilean['Gaia_ID'][i], self.Path)

            filters_used.append(target_chilean['Filter'][i])

        if 'Io' in target_chilean['Telescope'][0]:
            flatexo_io(self.Path, filters_used, nbu=3, nbHa=3, nbRc=3, nbz=3, nbr=3, nbi=3, nbg=3,nbIz=7,
                       nbExo=3,nbClear=3)
        if 'Europa' in target_chilean['Telescope'][0]:
            flatexo_euro(self.Path, filters_used, nbRc=3, nbB=3, nbz=3, nbV=3, nbr=3, nbi=3,nbg=3, nbIz=7,
                         nbExo=3,nbClear=3)
        if 'Ganymede' in target_chilean['Telescope'][0]:
            flatexo_gany(self.Path, filters_used, nbOIII=3, nbHa=3, nbSII=3, nbz=3, nbr=3, nbi=3,nbg=3, nbIz=7,
                         nbExo=3,nbClear=3)
        if 'Callisto' in target_chilean['Telescope'][0]:
            flatexo_calli(self.Path, t_now, filters_used, nbu=3, nbB=3, nbz=3, nbV=3, nbr=3, nbi=3,nbg=3, nbIz=7,
                          nbExo=3,nbClear=3)

        flatdawn(self.time_end, sun_rise.iso, self.Path)
        biasdark(self.Path)
        info_message ='INFO: Plans made'
        return info_message

    def check_plans(self):
        """ Check if plans meet constraints

        Returns
        -------
        info message
            return message to inform if the plan are ok or not

        """
        target_name = None
        for rr, dd, ff in os.walk(self.Path):
            for f in sorted(ff, reverse = True):
                if f.startswith('startup'):
                    file_startup = open(os.path.join(self.Path, f), 'r')
                    for line in file_startup:
                        if line.startswith('#waituntil 1,'):
                            self.start_date = line[14:].replace('\n','')
                            self.start_date= self.start_date.replace('/','-')
                            twilight_evening = self.observatory.twilight_evening_nautical(Time(self.start_date), which='nearest')
                            twilight_morning = self.observatory.twilight_morning_nautical(Time(self.start_date), which='next')
                            break
                elif f.startswith('Obj_'):
                    file = open(os.path.join(self.Path,f),'r')
                    if (self.time_start is None) or (self.time_end is None) or (target_name is None):
                        for l in file:
                            if l.startswith('#waituntil 1,') and self.time_start is None:
                                line_start = l
                                self.time_start = line_start[14:].replace('\n', '')
                                if len(self.time_start) > 7:
                                    self.time_start = Time(self.time_start.replace('/', '-'))
                                else:
                                    self.time_start = Time(Time((Time(self.start_date) + 1).iso,
                                                                out_subfmt='date').value + ' ' + self.time_start)
                            if l.startswith('#quitat'):
                                line_end = l
                                self.time_end = line_end[7:].replace('\n', '')
                                if len(self.time_end) > 7:
                                    self.time_end = self.time_end.replace('/', '-')
                                else:
                                    self.time_end = Time(Time((Time(self.start_date) + 1).iso,out_subfmt='date').value + self.time_end)
                            if l.startswith('; Ch'):
                                target_name = l[2:].replace('\n', '')

                    file = open(os.path.join(self.Path, f), 'r')
                    for line in file:
                        if line == ';\n':
                            pass
                        elif line.startswith('; Ch'):
                            target_name = line[2:].replace('\n','')
                        elif line.startswith('#filter'):
                            filt = line[8:].replace('\n','')
                            filt_accepted = ['I+z','z\'','i\'','r\'','i','r','z']
                            if filt in filt_accepted:
                                print('INFO: OK, filter chosen for '+ target_name + ' is in the list')
                            else:
                                sys.exit('ERROR: The filter chosen for target ' + target_name + ' is NOT in the filters list (list is [I+z,z\',i\',r\'])')

                        elif line.startswith('#interval'):
                            texp = line[9:].replace('\n', '')
                            if int(texp) < 10:
                                sys.exit('ERROR: The exposure time for target ' + target_name + ' is < 10s')
                            else:
                                print('INFO: OK, exposure time chosen for ' + target_name + ' is >10s')

                        elif line.startswith(target_name):
                            coords_str = line[(len(target_name)+1):].replace('\n','').replace('\t',' ')
                            coords = SkyCoord(coords_str, unit=(u.hourangle, u.deg))

                            if coords.dec.deg > 80:
                                print('WARNING: field ' + target_name + '\'s declination is above 80°, might have tracking issues')
                            time_range = [Time(self.time_start), Time(self.time_end)]
                            target = FixedTarget(coord=SkyCoord(ra=coords.ra.deg* u.degree,dec=coords.dec.deg* u.degree),name=target_name)
                            constraint_elevation = [AltitudeConstraint(min=24 * u.deg),AtNightConstraint.twilight_nautical()]  #
                            constraint_moon = [ MoonSeparationConstraint(min=20*u.deg),AtNightConstraint.twilight_nautical()]
                            observable_elevation = is_always_observable(constraint_elevation, self.observatory, target, time_range=time_range)
                            observable_moon = is_observable(constraint_moon, self.observatory, target,time_range=time_range)

                            if observable_elevation:
                                print('INFO: OK, field ' + target_name +  ' respects the elevation constraint')
                            if not observable_elevation:
                                sys.exit('ERROR: field ' + target_name +  ' does NOT respect the constraint of elevation (<23°)')
                            if observable_moon:
                                print('INFO: OK, field ' + target_name +  ' respects the moon constraint')
                            if not observable_moon:
                                print('WARNING: field ' + target_name + ' does NOT respect the moon separartion angle (>20°)')
                            if abs(coords.dec.deg) > 80:
                                print('WARNING: field ' + target_name + ' is very close to polar (>80) qulity will be worst than usual')

                            if self.time_end < self.time_start:
                                sys.exit('WARNING: Start time of field ' + target_name + ' is > to end time')
                            elif self.time_start < twilight_evening:
                                print('WARNING: Start time of field ' + target_name + ' is < to nautical evening twilight !')
                            elif self.time_end > twilight_morning:
                                print('WARNING: End time of field ' + target_name + ' is > to nautical morning twilight !')
                            elif (Time(self.time_end).jd - Time(self.time_start).jd)*24*60 < 15:
                                sys.exit('ERROR: You can NOT schedule field ' + target_name + ' for less than 15 min')
                            else:
                                print('INFO: Ok, field ' + target_name + ' is scheduled for more than 15 min')
                            self.check_distance_speculoos_targets(coords.ra, coords.dec, target_name)

        print('INFO: Check completed, plans are OK')

    def etc_chilean(self,Jmag,SpT,Filter):
        """ Return the optimized exposure time for the target

        Parameters
        ----------
        Jmag : float
            magnitude in J
        SpT : str
            spectral type of the target
        Filter : str
            filter used

        Returns
        -------
        texp  : float
            exposure time

        """

        moon_phase = round(moon_illumination(Time(self.start_date)), 2)
        a = ETC.etc(mag_val=Jmag, mag_band='J', spt=SpT, \
                    filt=Filter, airmass=1.1, moonphase=moon_phase, irtf=0.8, \
                    num_tel=1, seeing=0.95, gain=1.1)
        texp = a.exp_time_calculator(ADUpeak=30000)
        return texp

    def check_distance_speculoos_targets(self,ra,dec,target_name):
        """ check if target is not in SPECULOOS target list

        Parameters
        ----------
        ra : float
            right ascension (degrees)
        dec : float
            declinaison (degrees)
        target_name : str
            name of the target

        Returns
        -------
        info message
            state whether there is a SPECULOOS target in the field or not

        """

        catalog_data = Catalogs.query_object(str(ra) + str(dec), radius=6*np.sqrt(2) * u.arcminute, catalog="Gaia")
        df = pd.read_csv('./SPOCK_chilean_nights/speculoos_target_list_chilean_nights.txt',delimiter=' ')
        idx_speculoos_found = [np.where((catalog_data['designation'] == 'Gaia DR2 ' + str(gaia_id))) for gaia_id in df['Gaia_ID']]
        if np.any(idx_speculoos_found):
            sys.exit('ERROR: There is a SPECULOOS target in this field, please change your coordinates')
        else:
            print('INFO: OK, field ' + target_name + ' does not contain a SPECULOOS target')





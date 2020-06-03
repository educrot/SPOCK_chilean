import numpy as np
import os
import pandas as pd

startup_time=[]
hour=[]
minute=[]

def startup(name,sun_set,date_start,Path):
    """ Write startup.txt ACP plan

    Parameters
    ----------
    name : str
        name of the target
    sun_set : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    date_start : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    Path : str
        path where the plans will be stored
    Returns
    -------
    txt file
        startup.txt file (ACP compatible)

    """
    date_start=np.datetime64(date_start)
    sun_set=np.datetime64(sun_set)
    startup_time1=sun_set+np.timedelta64(10,'m')
    try:
        open(os.path.join(Path, 'startup.txt'), 'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'startup.txt'))
    with open(os.path.join(Path,'startup.txt'),'w') as out:
        str00=';\n'
        str0=' == Startup =='
        str1='#waituntil 1, '
        str2='#domeopen\n'
        str3='#chill '
        str33='-60\n'
        str4='#duskflats Cal_flatexo.txt\n'
        str5='#chain '
        str6='#quitat '
        out.write(';' + str0 + '\n')
        for i in range(1,3):
            out.write(str00)
        out.write(str1 + pd.to_datetime(str(sun_set)).strftime('%Y/%m/%d %H:%M:%S') + '\n')#+ str(hour00) + ':' + str(minute00) + '\n')
        out.write(str2)
        for i in range(1,2):
            out.write(str00)
        out.write(str3 + str33)
        for i in range(1,2):
            out.write(str00)
        out.write(str1 + pd.to_datetime(str(startup_time1)).strftime('%Y/%m/%d %H:%M:%S') + '\n')#str(hour1) + ':' + str(minute1) + '\n')
        out.write(str4)
        for i in range(1,2):
            out.write(str00)
        out.write(str6 + pd.to_datetime(str(date_start)).strftime('%Y/%m/%d %H:%M:%S') + '\n')#str(hour0) + ':' + str(minute0) + '\n')
        for i in range(1,2):
            out.write(str00)
        out.write(str5 + 'Obj_' + name + '.txt' + '\n')
        out.write(str00)


def target(name,date_start,date_end,waitlimit,afinterval,autofocus,count,filt,exptime,ra1,ra2,ra3,dec1,dec2,dec3,name_2,Gaia_ID,Path):
    """ Write target_name.txt ACP plan

    Parameters
    ----------
    name : str
        name of target
    date_start : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    date_end : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    waitlimit : int
        set to 600 by default
    afinterval : int
        set to 60 by default
    autofocus : int
        set to None by default
    count : int
        number of image for this target, set to 5000 by default
    filt : str
        filter used
    exptime : int
        exposure time
    ra1 : int
        HH in right ascension (HH MM SS.sss format)
    ra2 : int
        MM in right ascension (HH MM SS.sss format)
    ra3 : float
        SS.sss in right ascension (HH MM SS.sss format)
    dec1 : int
        DD in declinaison (DD MM SS.sss format)
    dec2 : int
        MM in declinaison (DD MM SS.sss format)
    dec3 : int
        SS.sss in declinaison (DD MM SS.sss format)
    name_2 : str
        name of the chain plan
    Gaia_ID : str
        gaia ID of the target
    Path : str
        path where the plans are stored

    Returns
    -------
    txt file
        target_name.txt file (ACP compatible)

    """
    gaia_id_target = Gaia_ID
    date_start=np.datetime64(date_start)
    date_end=np.datetime64(date_end)
    binning=1
    name_file=name + '.txt'
    hour0=date_start.astype(object).hour
    hour0='{:02d}'.format(int(hour0))
    minute0=date_start.astype(object).minute
    minute0='{:02d}'.format(int(minute0))
    hour1=date_end.astype(object).hour
    hour1='{:02d}'.format(int(hour1))
    minute1=date_end.astype(object).minute
    minute1='{:02d}'.format(int(minute1))
    try:
        open(os.path.join(Path,'Obj_' + name_file),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Obj_' + name_file))
    with open(os.path.join(Path,'Obj_' + name_file),'w') as out:
        str00=';'
        str1='#waituntil 1, '
        str2='#waitinlimits '
        str22='#domeopen\n'
        str3='#nopreview \n'
        str33=';#afinterval '
        str4='#autofocus \n'
        str5='#count '
        str6='#binning '
        str7='#filter '
        str8='#interval '
        str9='#quitat '
        str10='#chain '
        s=''
        s2=''
        seq_ra=(str(int(ra1)),'h',str(int(ra2)),'m',str(ra3),'s')
        seq_dec=(str(int(dec1)),'d',str(abs(int(dec2))),'m',str(abs(dec3)),'s')
        s.join( seq_ra )
        s2.join( seq_dec )
        for i in range(1,2):
            out.write(str00 + '\n')
        out.write(str00 + ' ' + str(name) + '\n')
        out.write(str00 + '\n')
        out.write(str00 + ' ' + str(gaia_id_target) + '\n')
        for i in range(1,2):
            out.write(str00 + '\n')
        out.write(str1 + str(hour0) + ':' + str(minute0) + '\n')
        out.write(str22)
        out.write('#chill -60\n')
        out.write(str2 + str(waitlimit) + '\n')
        out.write(str3)
        out.write(str33 + str(afinterval) +'\n')
        if autofocus is None:
            out.write(str00 + str4)
        out.write(str5 + str(count) + '\n')
        out.write(str6 + str(binning) + '\n')
        out.write(str7 + str(filt) + '\n')
        out.write(str8 + str(exptime) +'\n')
        out.write('#TAG Donuts=on'+'\n')
        if int(dec1)==-0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '-' + str('{:02d}'.format(int(dec1))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n') #8*np.cos(c.dec.radian)
        if int(dec1)<0 and int(dec1)!=-0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '-' + str('{:02d}'.format(int(abs(dec1)))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n')
        if int(dec1)>0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '+' + str('{:02d}'.format(int(dec1))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n')
        out.write(str00 + '\n')
        out.write(str9 + str(hour1) + ':' + str(minute1) + '\n' )
        if name_2 is None:
            out.write(str10 + 'Cal_flatdawn' + '.txt' + '\n')
        else:
            out.write(str10 + 'Obj_' + name_2 + '.txt' + '\n')
        out.write(str00 + '\n')


def first_target(name,date_start,date_end,waitlimit,afinterval,autofocus,count,filt,exptime,ra1,ra2,ra3,dec1,dec2,dec3,name_2,Gaia_ID,Path):
    """ Write target_name.txt ACP plan for the first target of the night

    Parameters
    ----------
    name : str
        name of target
    date_start : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    date_end : str
        date in "yyyy-mm-dd HH:MM:SS.SSS" format
    waitlimit : int
        set to 600 by default
    afinterval : int
        set to 60 by default
    autofocus : int
        set to None by default
    count : int
        number of image for this target, set to 5000 by default
    filt : str
        filter used
    exptime : int
        exposure time
    ra1 : int
        HH in right ascension (HH MM SS.sss format)
    ra2 : int
        MM in right ascension (HH MM SS.sss format)
    ra3 : float
        SS.sss in right ascension (HH MM SS.sss format)
    dec1 : int
        DD in declinaison (DD MM SS.sss format)
    dec2 : int
        MM in declinaison (DD MM SS.sss format)
    dec3 : int
        SS.sss in declinaison (DD MM SS.sss format)
    name_2 : str
        name of the chain plan
    Gaia_ID : str
        gaia ID of the target
    Path : str
        path where the plans are stored

    Returns
    -------
    txt file
        target_name.txt file (ACP compatible)

    """
    gaia_id_target = Gaia_ID
    date_start=np.datetime64(date_start)
    date_end=np.datetime64(date_end)
    binning=1
    name_file=name + '.txt'
    hour1=date_end.astype(object).hour
    hour1='{:02d}'.format(int(hour1))
    minute1=date_end.astype(object).minute
    minute1='{:02d}'.format(int(minute1))
    try:
        open(os.path.join(Path,'Obj_' + name_file),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Obj_' + name_file))
    with open(os.path.join(Path,'Obj_' + name_file),'w') as out:
        str00=';'
        str1='#waituntil 1, '
        str2='#waitinlimits '
        str22='#domeopen\n'
        str3='#nopreview \n'
        str33=';#afinterval '
        str4='#autofocus \n'
        str5='#count '
        str6='#binning '
        str7='#filter '
        str8='#interval '
        str9='#quitat '
        str10='#chain '
        s=''
        s2=''
        seq_ra=(str(int(ra1)),'h',str(int(ra2)),'m',str(ra3),'s')
        seq_dec=(str(int(dec1)),'d',str(abs(int(dec2))),'m',str(abs(dec3)),'s')
        s.join( seq_ra )
        s2.join( seq_dec )
        for i in range(1,2):
            out.write(str00 + '\n')
        out.write(str00 + ' ' + str(name) + '\n')
        out.write(str00 + '\n')
        out.write(str00 + ' ' + str(gaia_id_target) + '\n')
        for i in range(1,2):
            out.write(str00 + '\n')
        out.write(str1 + pd.to_datetime(str(date_start)).strftime('%Y/%m/%d %H:%M:%S') + '\n')
        out.write(str22)
        out.write('#chill -60\n')
        out.write(str2 + str(waitlimit) + '\n')
        out.write(str3)
        out.write(str33 + str(afinterval) +'\n')
        if autofocus is None:
            out.write(str00 + str4)
        out.write(str5 + str(count) + '\n')
        out.write(str6 + str(binning) + '\n')
        out.write(str7 + str(filt) + '\n')
        out.write(str8 + str(exptime) +'\n')
        out.write('#TAG Donuts=on'+'\n')
        if int(dec1)==-0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '-' + str('{:02d}'.format(int(dec1))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n')
        if int(dec1)<0 and int(dec1)!=-0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '-' + str('{:02d}'.format(int(abs(dec1)))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n')
        if int(dec1)>0:
            out.write(name + '\t' + str('{:02d}'.format(int(ra1))) + ' ' + str('{:02d}'.format(int(ra2))) + ' ' + str('{:05.2f}'.format(float(ra3))) + '\t' + '+' + str('{:02d}'.format(int(dec1))) \
             + ' ' + str('{:02d}'.format(int(abs(dec2)))) + ' ' + str('{:05.2f}'.format(abs(dec3))) + '\n')
        out.write(str00 + '\n')
        out.write(str9 + str(hour1) + ':' + str(minute1) + '\n' )
        if name_2 is None:
            out.write(str10 + 'Cal_flatdawn' + '.txt' + '\n')
        else:
            out.write(str10 + 'Obj_' + name_2 + '.txt' + '\n')
        out.write(str00 + '\n')


def flatdawn(date_end,sun_rise,Path):
    """ Write flatdawn.txt ACP plan

    Parameters
    ----------
    date_end : str
        time stop of obs in "yyyy-mm-dd HH:MM:SS.SSS" format
    sun_rise : str
        sun rise time in "yyyy-mm-dd HH:MM:SS.SSS" format
    Path : str
        path where the file is stored

    Returns
    -------
    txt file
        flatdawn.txt file

    """
    date_end=np.datetime64(date_end)
    hour0=date_end.astype(object).hour
    hour0='{:02d}'.format(int(hour0))
    minute0=date_end.astype(object).minute
    minute0='{:02d}'.format(int(minute0))
    sun_rise=np.datetime64(sun_rise)
    hour1=sun_rise.astype(object).hour
    hour1='{:02d}'.format(int(hour1))
    minute1=sun_rise.astype(object).minute
    minute1='{:02d}'.format(int(minute1))
    try:
        open(os.path.join(Path, 'Cal_flatdawn.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_flatdawn.txt'))
    with open(os.path.join(Path,'Cal_flatdawn.txt'),'w') as out:
        str00=';'
        str1='#waituntil 1, '
        str3='#dawnflats '
        str4='Cal_flatexo.txt \n'
        str44='#quitat '
        str5='#chain '
        str6='Cal_biasdark.txt \n'
        out.write(str1 + str(hour0) + ':' + str(minute0) + '\n')
        out.write(str3 + str4)
        out.write(str44 + str(hour1) + ':' + str(minute1) + '\n')
        out.write(str5 + str6)


def flatexo_gany(Path,filt,nbOIII=None,nbHa=None,nbSII=None,nbz=None,nbr=None,nbi=None,nbg=None,nbIz=None,nbExo=None,nbClear=None):
    """ Write flatexo.txt ACP plan if the telescope is SSO/Ganymede

    Parameters
    ----------
    Path : str
        path where the file is stored
    filt : str
        filter used
    nbOIII : int
        number of flat needed in OIII filter
    nbHa int
        number of flat needed in Ha filter
    nbSII int
        number of flat needed in SII filter
    nbz int
        number of flat needed in z\' filter
    nbr int
        number of flat needed in r\' filter
    nbi int
        number of flat needed in i\' filter
    nbg int
        number of flat needed in g\' filter
    nbIz int
        number of flat needed in I+z filter
    nbExo int
        number of flat needed in Exo filter
    nbClear int
        number of flat needed in Clear filter

    Returns
    -------
    txt file
        flatexo.txt file

    """

    str00=';'
    if nbOIII is None:
        nbOIII=3
    if nbHa is None:
        nbHa=3
    if nbSII is None:
        nbSII=3
    if nbz is None:
        nbz=3
    if nbr is None:
        nbr=3
    if nbi is None:
        nbi=3
    if nbg is None:
        nbg=3
    if nbIz is None:
        nbIz=3
    if nbExo is None:
        nbExo=3
    if nbClear is None:
        nbClear=3
    try:
        open(os.path.join(Path, 'Cal_flatexo.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_flatexo.txt'))
    with open(os.path.join(Path,'Cal_flatexo.txt'),'w') as out:
        if 'OIII' in filt:
            out.write(str(nbOIII) + ',' + 'OIII' + ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbOIII) + ',' + 'OIII' + ',' + '1' + '\n')
        if 'Ha' in filt:
            out.write(str(nbHa) + ',' + 'Ha' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbHa) + ',' + 'Ha' ',' + '1' + '\n')
        if 'SII' in filt:
            out.write(str(nbSII) + ',' + 'SII' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbSII) + ',' + 'SII' + ',' + '1' + '\n')
        if 'I+z' in filt:
            out.write(str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        if 'r\'' in filt:
            out.write(str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        if 'i\'' in filt:
            out.write(str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        if 'g\'' in filt:
            out.write(str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        if 'I+z' in filt:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        else:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        if 'Exo' in filt:
            out.write(str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        if 'Clear' in filt:
            out.write(str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')


def flatexo_calli(Path,filt,nbu=None,nbB=None,nbz=None,nbV=None,nbr=None,nbi=None,nbg=None,nbIz=None,nbExo=None,nbClear=None):
    """ Write flatexo.txt ACP plan if the telescope is SSO/Callisto

    Parameters
    ----------
    Path : str
        path where the file is stored
    filt : str
        filter used
    nbu : int
        number of flat needed in u\' filter
    nbB int
        number of flat needed in B filter
    nbz int
        number of flat needed in z\' filter
    nbV int
        number of flat needed in V filter
    nbr int
        number of flat needed in r\' filter
    nbi int
        number of flat needed in i\' filter
    nbg int
        number of flat needed in g\' filter
    nbIz int
        number of flat needed in I+z filter
    nbExo int
        number of flat needed in Exo filter
    nbClear int
        number of flat needed in Clear filter

    Returns
    -------
    txt file
        flatexo.txt file

    """

    str00=';'
    if nbu is None:
        nbu=3
    if nbB is None:
        nbB=3
    if nbz is None:
        nbz=3
    if nbV is None:
        nbV=3
    if nbr is None:
        nbr=3
    if nbi is None:
        nbi=3
    if nbg is None:
        nbg=3
    if nbIz is None:
        nbIz=3
    if nbExo is None:
        nbExo=3
    if nbClear is None:
        nbClear=3
    try:
        open(os.path.join(Path, 'Cal_flatexo.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_flatexo.txt'))
    with open(os.path.join(Path,'Cal_flatexo.txt'),'w') as out:
        if 'u\'' in filt:
            out.write(str(nbu) + ',' + 'u\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbu) + ',' + 'u\'' ',' + '1' + '\n')
        if 'B' in filt:
            out.write(str(nbB) + ',' + 'B' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbB) + ',' + 'B' + ',' + '1' + '\n')
        if 'z\'' in filt:
            out.write(str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        if 'V' in filt:
            out.write(str(nbV) + ',' + 'V' + ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbV) + ',' + 'V' + ',' + '1' + '\n')
        if 'r\'' in filt:
            out.write(str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        if 'i\'' in filt:
            out.write(str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        if 'g\'' in filt:
            out.write(str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        if 'I+z' in filt:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        else:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        if 'Exo' in filt:
            out.write(str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        if 'Clear' in filt:
            out.write(str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')


def flatexo_euro(Path,filt,nbRc=None,nbB=None,nbz=None,nbV=None,nbr=None,nbi=None,nbg=None,nbIz=None,nbExo=None,nbClear=None):
    """ Write flatexo.txt ACP plan if the telescope is SSO/Europa

    Parameters
    ----------
    Path : str
        path where the file is stored
    filt : str
        filter used
    nbRc : int
        number of flat needed in Rc filter
    nbB int
        number of flat needed in B filter
    nbz int
        number of flat needed in z\' filter
    nbV int
        number of flat needed in V filter
    nbr int
        number of flat needed in r\' filter
    nbi int
        number of flat needed in i\' filter
    nbg int
        number of flat needed in g\' filter
    nbIz int
        number of flat needed in I+z filter
    nbExo int
        number of flat needed in Exo filter
    nbClear int
        number of flat needed in Clear filter

    Returns
    -------
    txt file
        flatexo.txt file

    """
    str00=';'
    if nbRc is None:
        nbRc=3
    if nbB is None:
        nbB=3
    if nbz is None:
        nbz=3
    if nbV is None:
        nbV=3
    if nbr is None:
        nbr=3
    if nbi is None:
        nbi=3
    if nbg is None:
        nbg=3
    if nbIz is None:
        nbIz=3
    if nbExo is None:
        nbExo=3
    if nbClear is None:
        nbClear=3
    try:
        open(os.path.join(Path, 'Cal_flatexo.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_flatexo.txt'))
    with open(os.path.join(Path,'Cal_flatexo.txt'),'w') as out:
        if 'Rc' in filt:
            out.write(str(nbRc) + ',' + 'Rc' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbRc) + ',' + 'Rc' ',' + '1' + '\n')
        if 'B' in filt:
            out.write(str(nbB) + ',' + 'B' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbB) + ',' + 'B' + ',' + '1' + '\n')
        if 'z\'' in filt:
            out.write(str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        if 'V' in filt:
            out.write(str(nbV) + ',' + 'V' + ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbV) + ',' + 'V' + ',' + '1' + '\n')
        if 'r\'' in filt:
            out.write(str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        if 'i\'' in filt:
            out.write(str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        if 'g\'' in filt:
            out.write(str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        if 'I+z' in filt:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        else:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        if 'Exo' in filt:
            out.write(str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        if 'Clear' in filt:
            out.write(str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')


def flatexo_io(Path,filt,nbu=None,nbHa=None,nbRc=None,nbz=None,nbr=None,nbi=None,nbg=None,nbIz=None,nbExo=None,nbClear=None):

    """ Write flatexo.txt ACP plan if the telescope is SSO/io

    Parameters
    ----------
    Path : str
        path where the file is stored
    filt : str
        filter used
    nbu : int
        number of flat needed in u\' filter
    nbHa int
        number of flat needed in Ha filter
    nbRc int
        number of flat needed in Rc filter
    nbz int
        number of flat needed in z\' filter
    nbr int
        number of flat needed in r\' filter
    nbi int
        number of flat needed in i\' filter
    nbg int
        number of flat needed in g\' filter
    nbIz int
        number of flat needed in I+z filter
    nbExo int
        number of flat needed in Exo filter
    nbClear int
        number of flat needed in Clear filter

    Returns
    -------
    txt file
        flatexo.txt file

    """
    str00=';'
    if nbu is None:
        nbu=3
    if nbHa is None:
        nbHa=3
    if nbRc is None:
        nbu=Rc
    if nbz is None:
        nbz=3
    if nbr is None:
        nbr=3
    if nbi is None:
        nbi=3
    if nbg is None:
        nbg=3
    if nbIz is None:
        nbIz=3
    if nbExo is None:
        nbExo=3
    if nbClear is None:
        nbClear=3
    try:
        open(os.path.join(Path, 'Cal_flatexo.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_flatexo.txt'))
    with open(os.path.join(Path,'Cal_flatexo.txt'),'w') as out:
        if 'u\'' in filt:
            out.write(str(nbu) + ',' + 'u\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbu) + ',' + 'u\'' ',' + '1' + '\n')
        if 'Ha' in filt:
            out.write(str(nbHa) + ',' + 'Ha' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbHa) + ',' + 'Ha' + ',' + '1' + '\n')
        if 'Rc' in filt:
            out.write(str(nbRc) + ',' + 'Rc' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbRc) + ',' + 'Rc' + ',' + '1' + '\n')
        if 'z\'' in filt:
            out.write(str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbz) + ',' + 'z\'' ',' + '1' + '\n')
        if 'r\'' in filt:
            out.write(str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbr) + ',' + 'r\'' ',' + '1' + '\n')
        if 'i\'' in filt:
            out.write(str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        else:
            out.write(str00 +  str(nbi) + ',' + 'i\'' ',' + '1' + '\n')
        if 'g\'' in filt:
            out.write(str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbg) + ',' + 'g\'' ',' + '1' + '\n')
        if 'I+z' in filt:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        else:
            out.write(str(nbIz) + ',' + 'I+z' + ',' + '1' + '\n')
        if 'Exo' in filt:
            out.write(str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbExo) + ',' + 'Exo' + ',' + '1' + '\n')
        if 'Clear' in filt:
            out.write(str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')
        else:
            out.write(str00 + str(nbClear) + ',' + 'Clear' + ',' + '1' + '\n')


def biasdark(Path):
    """  Write biasdark.txt ACP plan

    Parameters
    ----------
    Path : str
        path where the file is stored

    Returns
    -------
    text file
        biasdark.txt file

    """
    try:
        open(os.path.join(Path, 'Cal_biasdark.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_biasdark.txt'))
    with open(os.path.join(Path,'Cal_biasdark.txt'),'w') as out:
        str00=';'
        str1='#domeclose \n'
        str2='#nopreview \n'
        str3=' == bias dark exoplanet =='
        str4='#count '
        str5='#binning '
        str6='#interval '
        str7='#dark \n'
        str8='#shutdown \n'
        str9='END'
        out.write(str1)
        out.write(str2)
        out.write(str00 + '\n')
        out.write(str00 + str3 + '\n')
        out.write(str00 + '\n')
        out.write(str4 + '9,9,9,9,9' + '\n')
        out.write(str5 + '1,1,1,1,1' + '\n')
        out.write(str6 + '0,15,30,60,120' + '\n')
        out.write(str7)
        out.write(str8)
        out.write(str00 + '\n')
        out.write(str00 + str9+ '\n')
        out.write(str00 + '\n')


def shutdown(Path):
    """ Write shutdown.txt ACP plan

    Parameters
    ----------
    Path : str
        path where the file is stored

    Returns
    -------
    text file
        shutdown.txt file

    """
    try:
        open(os.path.join(Path, 'Cal_shutdown.txt'),'w')
    except FileNotFoundError:
        os.mkdir(os.path.join(Path,'Cal_shutdown.txt'))
    with open(os.path.join(Path,'Cal_shutdown.txt'),'w') as out:
        str00=';'
        str1='#domeclose \n'
        str2='#shutdown \n'
        out.write(str00 + '\n')
        out.write(str1)
        out.write(str2)
        out.write(str00 + '\n')
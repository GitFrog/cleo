# %% 
import pandas as pd
import re
# %%
# POSTCODE Cleaning 
def clean_postcode(pcode):
    '''
    Write a function that clean the postcode:  
    1. upper case the string  
    2. remove the space in the middle 
    3. remove the dash 
    '''
    pcode = pcode.upper()
    pcode = re.sub(r'\s', '', pcode)
    pcode = re.sub(r'-', '', pcode)
    return pcode

# Validate the postcode
def validate_postal(pcode):
    postcode_regex = '[A-Z][0-9][A-Z][0-9][A-Z][0-9]'  # eg: M2N6Z8

    if re.match(postcode_regex, pcode):
        return True
    else:
        return False
# %%

# Reference: Statistics Canada; Canada Post; USPS
# https://www150.statcan.gc.ca/n1/pub/92-500-g/2013001/tbl/tbl4-2-eng.htm#E
# https://prd11.wsl.canadapost.ca/cpc/en/support/articles/addressing-guidelines/symbols-and-abbreviations.page?
# https://pe.usps.com/text/pub28/28apc_002.htm

def Address_suffix_Standardize(address):
    #  Addresses must follow proper case
    address = address.title()
    #  Standardized Street Suffix
    # \b is used to set the word boundary
    address = re.sub(r'\b\bAllee\b|\b\bAlly\b|\b\bAlley\b', 'Aly', address)
    address = re.sub(r'\b\bAnex\b|\b\bAnnex\b|\b\bAnnx\b', 'Anx', address)
    address = re.sub(
        r'\b\bAv\b|\b\bAvenue\b|\b\bAven\b|\b\bAvenu\b|\b\bAvn\b|\b\bAvnue\b', 'Ave', address)
    address = re.sub(r'\b\bArcade\b', 'Arc', address)
    address = re.sub(r'\b\bBayoo\b|\b\bBayou\b', 'Byu', address)
    address = re.sub(r'\b\bBench\b', 'Bch', address)
    address = re.sub(r'\b\bBend\b', 'Bnd', address)
    address = re.sub(r'\b\bBlf\b|\b\bBluf\b', 'Bluff', address)
    address = re.sub(r'\b\bBot\b|\b\bBtm\b|\b\bBottm\b', 'Bottom', address)
    address = re.sub(r'\b\bBlvd\b|\b\bBoul\b|\b\bBoulv\b',
                     'Boulevard', address)
    address = re.sub(r'\b\bBr\b|\b\bBrnch\b', 'Branch', address)
    address = re.sub(r'\b\bBrdge\b|\b\bBrg\b', 'Bridge', address)
    address = re.sub(r'\b\bBluff\b|\b\bBluf\b', 'Blf', address)
    address = re.sub(r'\b\bBluffs\b|\b\bBlufs\b', 'Blf', address)
    address = re.sub(r'\b\bBot\b|\b\bBottm\b|\b\bBottm\b', 'Btm', address)
    address = re.sub(r'\bBoulevard\b|\bBoul\b|\bBoulv\b', 'Blvd', address)
    address = re.sub(r'\bBr\b|\bBranch\b', 'Br', address)
    address = re.sub(r'\bBrdge\b|\bBridge\b', 'Brg', address)
    address = re.sub(r'\bBrook\b', 'Brk', address)
    address = re.sub(r'\bBrdge\b|\bBridge\b', 'Brg', address)
    address = re.sub(r'\bBrooks\b', 'Brks', address)
    address = re.sub(r'\bBurg\b', 'Bg', address)
    address = re.sub(r'\bBurgs\b', 'Bgs', address)
    address = re.sub(r'\bBypa\b|\bBypas\b|\bBypass\b|\bByps\b', 'Byp', address)
    address = re.sub(r'\bCamp\b|\bCmp\b', 'Cp', address)
    address = re.sub(r'\bCanyn\b|\bCanyon\b|\bCnyn\b', 'Cyn', address)
    address = re.sub(r'\bCape\b', 'Cpe', address)
    address = re.sub(r'\bCauseway\b|\bCauswa\b', 'Cswy', address)
    address = re.sub(r'\bCen\b|\bCent\b|\bCenter\b|\bCentr\b|\bCnter\b|\bCntr\b|\bCentre\b', 'Ctr', address)
    address = re.sub(r'\bCenters', 'Ctrs', address)
    address = re.sub(r'\bCir\b|\bCirc\b|\bCircl\b|\bCircle\b|\bCrcl\b|\bCrcle\b', 'Cir', address)
    address = re.sub(r'\bCliff\b', 'Clf', address)
    address = re.sub(r'\bCliffs', 'Clfs', address)
    address = re.sub(r'\bClub\b', 'Clb', address)
    address = re.sub(r'\bCommon\b', 'CMN', address)
    address = re.sub(r'\bCorner\b', 'Cor', address)
    address = re.sub(r'\bCorners\b', 'Cors', address)
    address = re.sub(r'\bCourse\b', 'Crse', address)
    address = re.sub(r'\bCourt\b', 'Ct', address)
    address = re.sub(r'\bCourts\b', 'Cts', address)
    address = re.sub(r'\bCove\b', 'Cv', address)
    address = re.sub(r'\bCoves\b', 'Cvs', address)
    address = re.sub(r'\bCreek\b', 'Crk', address)
    address = re.sub(r'\bCrescent\b|\bCres\b|\bCrsent\b|\bCrsnt\b', 'Cres', address)
    address = re.sub(r'\bCrest\b', 'Crst', address)
    address = re.sub(r'\bCrossing\b|\bCrssng\b', 'Xing', address)
    address = re.sub(r'\bCurve\b', 'Curv', address)
    address = re.sub(r'\bDale\b', 'Dl', address)
    address = re.sub(r'\bDam\b', 'Dm', address)
    address = re.sub(r'\bDiv\b|\b\bDivide\b|\b\bDv\b|\b\bDvd\b', 'Dv', address)
    address = re.sub(r'\bDr\b|\bDriv\b|\bDrive\b|\bDrv\b', 'Dr', address)
    address = re.sub(r'\bDrives\b', 'Drs', address)
    address = re.sub(r'\bEstate\b', 'Est', address)
    address = re.sub(r'\bEstates\b', 'Ests', address)
    address = re.sub(r'\bExp\b|\bExpr\b|\bExpress\b|\bExpressway\b|\bExpw\b|\bExpy\b', 'Expy', address)
    address = re.sub(r'\bExt\b|\bExtension\b|\bExtn\b|\bExtnsn\b', 'Ext', address)
    address = re.sub(r'\bFalls\b', 'Fls', address)
    address = re.sub(r'\bFerry\b|\bFrry\b|\bFry\b', 'Fry', address)
    address = re.sub(r'\bField\b', 'Fld', address)
    address = re.sub(r'\bFields\b', 'Flds', address)
    address = re.sub(r'\bFlat\b', 'Flt', address)
    address = re.sub(r'\bFlats\b', 'Flts', address)
    address = re.sub(r'\bFord\b', 'Frd', address)
    address = re.sub(r'\bFords\b', 'Frds', address)
    address = re.sub(r'\bForest\b|\bForests\b|\bFrst\b', 'Frst', address)
    address = re.sub(r'\bForg\b|\bForge\b|\bFrg\b', 'Frg', address)
    address = re.sub(r'\bForges\b', 'Frgs', address)
    address = re.sub(r'\bFork\b', 'Frk', address)
    address = re.sub(r'\bForks\b', 'Frks', address)
    address = re.sub(r'\bFort\b|\bFrt\b', 'Ft', address)
    address = re.sub(r'\bFreeway\b|\bFreewy\b|\bFrway\b|\bFrwy\b|\bFwy\b', 'Fwy', address)
    address = re.sub(r'\bGarden\b|\bGardn\b|\bGrden\b|\bGrdn\b', 'Gdn', address)
    address = re.sub(r'\bGardens\b|\bGrdns\b', 'Gdns', address)
    address = re.sub(r'\bGateway\b|\bGatewy\b|\bGatway\b|\bGtway\b|\bGtwy\b', 'Gtwy', address)
    address = re.sub(r'\bGlen\b', 'Gln', address)
    address = re.sub(r'\bGlens\b', 'Glns', address)
    address = re.sub(r'\bGreen\b', 'Grn', address)
    address = re.sub(r'\bGreens\b', 'Grns', address)
    address = re.sub(r'\bGrov\b|\bGrove\b|\bGrv\b', 'Grv', address)
    address = re.sub(r'\bGroves\b', 'Grvs', address)
    address = re.sub(r'\bHarb\b|\bHarbor\b|\bHarbr\b|\bHrbor\b', 'Hbr', address)
    address = re.sub(r'\bHarbors\b', 'Hbrs', address)
    address = re.sub(r'\bHaven\b', 'Hvn', address)
    address = re.sub(r'\bHt\b', 'Hts', address)
    address = re.sub(r'\bHighway\b|\bHighwy\b|\bHiway\b|\bHiwy\b|\bHway\b', 'Hwy', address)
    address = re.sub(r'\bHill\b', 'Hl', address)
    address = re.sub(r'\bHills\b', 'Hls', address)
    address = re.sub(r'\bHllw\b|\bHollow\b|\bHollows\b|\bHolws\b', 'Holw', address)
    address = re.sub(r'\bIsland\b|\bIslnd\b', 'Is', address)
    address = re.sub(r'\bIslands\b|\bIslnds\b', 'Iss', address)
    address = re.sub(r'\bIsles\b', 'Isle', address)
    address = re.sub(r'\bJction\b|\bJctn\b|\bJunction\b|\bJunctn\b|\bJuncton\b', 'Jct', address)
    address = re.sub(r'\bJctns\b|\bJunctions\b', 'Jcts', address)
    address = re.sub(r'\bKey\b', 'Ky', address)
    address = re.sub(r'\bKeys\b', 'Kys', address)
    address = re.sub(r'\bKnol\b|\bKnoll\b', 'Knl', address)
    address = re.sub(r'\bKnolls\b', 'Knls', address)
    address = re.sub(r'\bLake\b', 'Lk', address)
    address = re.sub(r'\bLanding\b|\bLndng\b', 'Lndg', address)
    address = re.sub(r'\bLane\b', 'Ln', address)
    address = re.sub(r'\bLight\b', 'Lgt', address)
    address = re.sub(r'\bLights\b', 'Lgts', address)
    address = re.sub(r'\bLoaf\b', 'Lf', address)
    address = re.sub(r'\bLock\b', 'Lck', address)
    address = re.sub(r'\bLocks\b', 'Lcks', address)
    address = re.sub(r'\bLdge\b|\bLodg\b|\bLodge\b', 'Ldg', address)
    address = re.sub(r'\bLoops\b', 'Loop', address)
    address = re.sub(r'\bManor\b', 'Mnr', address)
    address = re.sub(r'\bManors\b', 'Mnrs', address)
    address = re.sub(r'\bMeadow\b', 'Mdw', address)
    address = re.sub(r'\bMeadows\b|\bMedows\b', 'Mdws', address)
    address = re.sub(r'\bMill\b', 'Ml', address)
    address = re.sub(r'\bMills\b', 'Mls', address)
    address = re.sub(r'\bMissn\b|\bMssn\b', 'Msn', address)
    address = re.sub(r'\bMotorway\b', 'Mtwy', address)
    address = re.sub(r'\bMnt\b|\bMount\b', 'Mt', address)
    address = re.sub(r'\bMntain\b|\bMntn\b|\bMountain\b|\bMountin\b|\bMtin\b', 'Mtn', address)
    address = re.sub(r'\bMountains\b', 'Mtns', address)
    address = re.sub(r'\bNeck\b', 'Nck', address)
    address = re.sub(r'\bOrchard\b|\bOrchrd\b', 'Orch', address)
    address = re.sub(r'\bOvl\b', 'Oval', address)
    address = re.sub(r'\bOverpass\b', 'Opas', address)
    address = re.sub(r'\bPrk\b|\bParks', 'Park', address)
    address = re.sub(r'\bParkway\b|\bParkways\b|\bpkwys\b|\bParkwy\b|\bPkway\b|\bPky\b', 'Pkwy', address)
    address = re.sub(r'\bPassage\b', 'Psge', address)
    address = re.sub(r'\bPaths\b', 'Path', address)
    address = re.sub(r'\bPikes\b', 'Pike', address)
    address = re.sub(r'\bPine\b', 'Pne', address)
    address = re.sub(r'\bPines\b', 'Pnes', address)
    address = re.sub(r'\bPlain\b', 'Pln', address)
    address = re.sub(r'\bPlains\b', 'Plns', address)
    address = re.sub(r'\bPlaza\b|\bPlza\b', 'Plz', address)
    address = re.sub(r'\bPoint\b', 'Pt', address)
    address = re.sub(r'\bPort\b', 'Prt', address)
    address = re.sub(r'\bPorts\b', 'Prts', address)
    address = re.sub(r'\bPrairie\b|\bPrr\b', 'Pr', address)
    address = re.sub(r'\bRad\b|\bRadial\b|\bRadiel\b', 'Radl', address)
    address = re.sub(r'\bRanch\b|\bRanches\b|\bRnchs\b', 'Rnch', address)
    address = re.sub(r'\bRapid\b', 'Rpd', address)
    address = re.sub(r'\bRapids\b', 'Rpds', address)
    address = re.sub(r'\bRest\b', 'Rst', address)
    address = re.sub(r'\bRdge\b|\bRidge\b', 'Rdg', address)
    address = re.sub(r'\bRiver\b|\bRvr\b|\bRivr\b', 'Riv', address)
    address = re.sub(r'\bRoad\b', 'Rd', address)
    address = re.sub(r'\bRoads\b', 'Rds', address)
    address = re.sub(r'\bRoute\b', 'Rte', address)
    address = re.sub(r'\bShoal\b', 'Shl', address)
    address = re.sub(r'\bShoals\b', 'Shls', address)
    address = re.sub(r'\bShoar\b|\bShore\b', 'Shr', address)
    address = re.sub(r'\bShoars\b|\bShores\b', 'Shrs', address)
    address = re.sub(r'\bSkyway\b', 'Skwy', address)
    address = re.sub(r'\bSpng\b|\bSpring\b|\bSprng\b', 'Spg', address)
    address = re.sub(r'\bSpngs\b|\bSprings\b|\bSprngs\b', 'Spgs', address)
    address = re.sub(r'\bSpurs\b', 'Spur', address)
    address = re.sub(r'\bSqr\b|\bSqre\b|\bSqu\b|\bSquare\b', 'Sq', address)
    address = re.sub(r'\bSqrs\b|\bSquares', 'Sqs', address)
    address = re.sub(r'\bStation\b|\bStatn\b|\bStn\b', 'Sta', address)
    address = re.sub(r'\bStrav\b|\bStraven\b|\bStravenue\b|\bStravn\b|\bStrvn\b|\bStrvnue\b', 'Stra', address)
    address = re.sub(r'\bStream\b|\bStreme\b', 'Strm', address)
    address = re.sub(r'\bStreet\b|\bStrt\b|\bSt\b|\bStr\b', 'St', address)
    address = re.sub(r'\bStreets\b', 'Sts', address)
    address = re.sub(r'\bSmt\b|\bSumit\b|\bSumitt\b|\bSummit\b', 'Smt', address)
    address = re.sub(r'\bTerr\b|\bTerrace\b', 'Ter', address)
    address = re.sub(r'\bThroughway\b', 'Trwy', address)
    address = re.sub(r'\bTrace\b|\bTraces\b', 'Trce', address)
    address = re.sub(r'\bTrack\b|\bTracks\b|\bTrk\b|\bTrks', 'Trak', address)
    address = re.sub(r'\bTrafficway\b', 'Trfy', address)
    address = re.sub(r'\bTrail\b|\bTrails\b|\bTrls\b', 'Trl', address)
    address = re.sub(r'\bTrailer\b|\bTrlrs\b', 'Trlr', address)
    address = re.sub(r'\bTunel\b|\bTunls\b|\bTunnel\b|\bTunnels\b|\bTunnl\b', 'Tunl', address)
    address = re.sub(r'\bTrnpk\b|\bTurnpike\b|\bTurnpk\b', 'Tpke', address)
    address = re.sub(r'\bUnderpass\b', 'Upas', address)
    address = re.sub(r'\bUnion\b', 'Un', address)
    address = re.sub(r'\bUnions\b', 'Uns', address)
    address = re.sub(r'\bValley\b|\bVally\b|\bVlly\b', 'Vly', address)
    address = re.sub(r'\bValleys\b', 'Vlys', address)
    address = re.sub(r'\bVdct\b|\bViadct\b|\bViaduct\b', 'Via', address)
    address = re.sub(r'\bView\b', 'Vw', address)
    address = re.sub(r'\bViews\b', 'Vws', address)
    address = re.sub(r'\bVill\b|\bVillag\b|\bVillage\b|\bVillg\b|\bVilliage\b', 'Vlg', address)
    address = re.sub(r'\bVillages\b', 'Vlgs', address)
    address = re.sub(r'\bVille\b', 'Vl', address)
    address = re.sub(r'\bVist\b|\bVista\b|\bVst\b|\bVsta\b', 'Vis', address)
    address = re.sub(r'\bWalks\b', 'Walk', address)
    address = re.sub(r'\bWy\b', 'Way', address)
    address = re.sub(r'\bWell\b', 'Wl', address)
    address = re.sub(r'\bWells\b', 'Wls', address)

    return address
# %%
def Unit_designators_Standardize(address):

    #  Standardized Unit_designators
    address = re.sub(r'\bUni\b|\bU\b|\bUit\b|\bUnite\b', 'Unit', address)
    address = re.sub(r'\bApartment\b|\broom\b|\bAppartment\b|\bApart\b|\bAptment\b|\bApartments\b|\bAppart\b', 'Apt', address)
    address = re.sub(r'\bSui\b|\bSuit\b', 'Suite', address)
    address = re.sub(r'\bFloor\b|\bFlor\b|\bFlr\b', 'Floor', address)

    return address
# %%
def Street_directions_Standardize(address):

    #  Standardized street directions
    address = re.sub(r'\bEast\b', 'E', address)
    address = re.sub(r'\bNorth\b', 'N', address)
    address = re.sub(r'\bNortheast\b', 'NE', address)
    address = re.sub(r'\bNorthwest\b', 'NW', address)
    address = re.sub(r'\bSouth\b', 'S', address)
    address = re.sub(r'\bSoutheast\b', 'SE', address)
    address = re.sub(r'\bSouthwest\b', 'SW', address)
    address = re.sub(r'\bWest\b', 'W', address)

    return address
# %%
# Input of component_addr function: 1. index of the dataframe; 2.address column; 3. dataframe  
def component_addr(index, address, df):
    # def component_addr(address):

    #print("input address:",address)
    address = Address_suffix_Standardize(address)
    address = Unit_designators_Standardize(address)
    address = Street_directions_Standardize(address)

    '''Checks for address after normalization and puts them in the standard format'''

    #print("address after normalization:",address)
    ####################################################################################
    ########################         Unit_Num            ###############################
    ####################################################################################
    # pattern for apt number/suit number/unit number
    unit_nums = re.findall(r"(?<=Unit)\s*\w?\d+\w?|(?<=Floor)\s*\w*\d+\w*|(?<=Apt)\s*\w?\d+\w?|(?<=\#)\s*\w?\d+\w?|(?<=Suite)\s*\w?\d+\w?|\w?\d+\w?(?=\s*/)|\w?\d+\w?(?=\s*-)", address)
    unit_num = unit_nums[0].strip() if len(unit_nums) == 1 else ""

    # Trim the unit designnator & punctuation
    proc_addr = re.sub(r"Unit\s*\w?\d+\w?/?|Apt\s*\w?\d+\w?/?|Suite\s*\d+\w?/?|\w?\d+\w?\s*/|\w?\d+\w?\s*-", "", address)
    proc_addr = re.sub(r"^[,\-\/ ]+|[,\-\/ ]+$", "", proc_addr)

    #print("Unitless address: ", proc_addr)
    ####################################################################################
    ########################         Building_Num        ###############################
    ####################################################################################
    # pattern for building # A/B/C/D
    Building_nums = re.findall(r"\s[ABCD]{1}\s", proc_addr)
    building_num = Building_nums[0].strip() if len(Building_nums) == 1 else ""

    # Trim the building number
    proc_addr = re.sub(r"\s[ABCD]{1}\s", " ", proc_addr)
    #print("Buildingless address: ", proc_addr)
    ####################################################################################
    ########################         Street_direction          #########################
    ####################################################################################
    Street_directions = re.findall(r"\b\sE\b|\b\sN\b|\b\sNE\b|\b\sNW\b|\b\sS\b|\b\sSE\b|\b\sSW\b|\b\sSW\b|\b\sW\b", proc_addr)
    Street_direction = Street_directions[0].strip() if len(
        Street_directions) >= 1 else ""

    # Trim the building number
    proc_addr = re.sub(r"\s\bE\b|\s\bN\b|\s\bNE\b|\s\bNW\b|\s\bS\b|\s\bSE\b|\s\bSW\b|\s\bSW\b|\s\bW\b", "", proc_addr)
    #print("street direction less address: ", proc_addr)
    ####################################################################################
    ######################## RegEx Named Capture Group        #########################
    ####################################################################################
    Address_suffix_opts = r"Aly|Anx|Arc|Ave|Byu|Bch|Bnd|Blf|Blfs|Btm|Blvd|Br|Brg|Brk|Brks|Bg|Bgs|Byp|Cp|Cyn|Cpe|Cswy|Ctr|Ctrs|Cir|Cirs|Clf|Clfs|Clb|Cmn|Cmns|Cor|Cors|Crse|Ct|Cts|Cv|Cvs|Crk|Cres|Crst|Xing|Xrd|Xrds|Curv|Dl|Dm|Dv|Dr|Drs|Est|Ests|Expy|Ext|Exts|Fall|Fls|Fry|Fld|Flds|Flt|Flts|Frd|Frds|Frst|Frg|Frgs|Frk|Frks|Ft|Fwy|Gdn|Gdns|Gtwy|Gln|Glns|Grn|Grns|Grv|Grvs|Hbr|Hbrs|Hvn|Hts|Hwy|Hl|Hls|Holw|Inlt|Is|Iss|Isle|Jct|Jcts|Ky|Kys|Knl|Knls|Lk|Lks|Land|Lndg|Ln|Line|Lgt|Lgts|Lf|Lck|Lcks|Ldg|Loop|Mall|Mnr|Mnrs|Mdw|Mdws|Mews|Ml|Mls|Msn|Mtwy|Mt|Mtn|Mtns|Nck|Orch|Oval|Opas|Park|Park|Pkwy|Pkwy|Pass|Psge|Path|Pike|Pne|Pnes|Pl|Pln|Plns|Plz|Pt|Pts|Prt|Prts|Pr|Radl|Ramp|Rnch|Rpd|Rpds|Rst|Rdg|Rdgs|Riv|Rd|Rds|Rte|Row|Rue|Run|Shl|Shls|Shr|Shrs|Skwy|Spg|Spgs|Spur|Spur|Sq|Sqs|Sta|Stra|Strm|St|Sts|Smt|Ter|Trwy|Trce|Trak|Trfy|Trl|Trlr|Tunl|Tpke|Upas|Un|Uns|Vly|Vlys|Via|Vw|Vws|Vlg|Vlgs|Vl|Vis|Walk|Walk|Wall|Way|Ways|Wl|Wls"
    standard_address_pattern = r"(?P<civic_no>\w?\d+(\-\d+)?\w?\s+)(?P<rd_nm>[a-zA-z \d\-\']+)\s+(?P<rd_tp>" + \
        Address_suffix_opts + ")"
    #print("Road Attr Pattern: ", standard_address_pattern)
    road_attrs = re.search(standard_address_pattern, proc_addr)
    try:
        civic_num = road_attrs.group('civic_no').strip()
    except AttributeError:
        civic_num = ""
    #print("Road number: ", road_num)
    try:
        road_name = road_attrs.group('rd_nm').strip()
    except AttributeError:
        road_name = ""
    #print("Road name: ", road_name)
    try:
        road_type = road_attrs.group('rd_tp').strip()
    except AttributeError:
        road_type = ""
    #print("Road type: ", road_type)
    # return unit_num, building_num,civic_num,road_name,road_type,Street_direction

    df.at[index, 'unit_num'] = unit_num
    df.at[index, 'building_num'] = building_num
    df.at[index, 'civic_num'] = civic_num
    df.at[index, 'road_name'] = road_name
    df.at[index, 'road_type'] = road_type 
    df.at[index, 'Street_direction'] = Street_direction
# %%
def clean_address(address):

    #print("input address:",address)
    address = Address_suffix_Standardize(address)
    address = Unit_designators_Standardize(address)
    address = Street_directions_Standardize(address)

    '''Checks for address after normalization and puts them in the standard format'''

    #print("address after normalization:",address)
    ####################################################################################
    ########################         Unit_Num            ###############################
    ####################################################################################
    # pattern for apt number/suit number/unit number 
    unit_nums = re.findall(r"(?<=Unit)\s*\w?\d+\w?|(?<=Floor)\s*\w*\d+\w*|(?<=\#)\s*\w?\d+\w?|(?<=Apt)\s*\w?\d+\w?|(?<=Suite)\s*\w?\d+\w?|\w?\d+\w?(?=\s*/)|\w?\d+\w?(?=\s*-)|[1-9]*(?=\s\d+\b)", address)
    unit_num = '#'+unit_nums[0].strip() if len(unit_nums) >= 1 else ""
    # Trim the unit designnator & punctuation 
    proc_addr = re.sub(
        r"Unit\s*\w?\d+\w?/?|Apt\s*\w?\d+\w?/?|Suite\s*\d+\w?/?|\w?\d+\w?\s*/|\w?\d+\w?\s*-|[1-9]*(?=\s\d+\b)", "", address)
    proc_addr = re.sub(r"^[,\-\/ ]+|[,\-\/ ]+$", "", proc_addr)

    #print("Unitless address: ", proc_addr)
    ####################################################################################
    ########################         Building_Num        ###############################
    ####################################################################################
    # pattern for building # A/B/C/D
    Building_nums = re.findall(r"\s[ABCD]{1}\s", proc_addr)
    building_num = Building_nums[0].strip() if len(Building_nums) == 1 else ""
 
    # Trim the building number
    proc_addr = re.sub(r"\s[ABCD]{1}\s", " ", proc_addr)
    #print("Buildingless address: ", proc_addr)
    ####################################################################################
    ########################         Street_direction          #########################
    ####################################################################################
    Street_directions = re.findall(r"\b\sE\b|\b\sN\b|\b\sNE\b|\b\sNW\b|\b\sS\b|\b\sSE\b|\b\sSW\b|\b\sSW\b|\b\sW\b", proc_addr)
    Street_direction = Street_directions[0].strip() if len(Street_directions) >= 1 else ""
 
    #Trim the building number
    proc_addr = re.sub(r"\s\bE\b|\s\bN\b|\s\bNE\b|\s\bNW\b|\s\bS\b|\s\bSE\b|\s\bSW\b|\s\bSW\b|\s\bW\b", "", proc_addr)
    #print("street direction less address: ", proc_addr)
    ####################################################################################
    ######################## RegEx Named Capture Group        #########################
    ####################################################################################
    Address_suffix_opts = r"Aly|Anx|Arc|Ave|Byu|Bch|Bnd|Blf|Blfs|Btm|Blvd|Br|Brg|Brk|Brks|Bg|Bgs|Byp|Cp|Cyn|Cpe|Cswy|Ctr|Ctrs|Cir|Cirs|Clf|Clfs|Clb|Cmn|Cmns|Cor|Cors|Crse|Ct|Cts|Cv|Cvs|Crk|Cres|Crst|Xing|Xrd|Xrds|Curv|Dl|Dm|Dv|Dr|Drs|Est|Ests|Expy|Ext|Exts|Fall|Fls|Fry|Fld|Flds|Flt|Flts|Frd|Frds|Frst|Frg|Frgs|Frk|Frks|Ft|Fwy|Gdn|Gdns|Gtwy|Gln|Glns|Grn|Grns|Grv|Grvs|Hbr|Hbrs|Hvn|Hts|Hwy|Hl|Hls|Holw|Inlt|Is|Iss|Isle|Jct|Jcts|Ky|Kys|Knl|Knls|Lk|Lks|Land|Lndg|Ln|Line|Lgt|Lgts|Lf|Lck|Lcks|Ldg|Loop|Mall|Mnr|Mnrs|Mdw|Mdws|Mews|Ml|Mls|Msn|Mtwy|Mt|Mtn|Mtns|Nck|Orch|Oval|Opas|Park|Park|Pkwy|Pkwy|Pass|Psge|Path|Pike|Pne|Pnes|Pl|Pln|Plns|Plz|Pt|Pts|Prt|Prts|Pr|Radl|Ramp|Rnch|Rpd|Rpds|Rst|Rdg|Rdgs|Riv|Rd|Rds|Rte|Row|Rue|Run|Shl|Shls|Shr|Shrs|Skwy|Spg|Spgs|Spur|Spur|Sq|Sqs|Sta|Stra|Strm|St|Sts|Smt|Ter|Trwy|Trce|Trak|Trfy|Trl|Trlr|Tunl|Tpke|Upas|Un|Uns|Vly|Vlys|Via|Vw|Vws|Vlg|Vlgs|Vl|Vis|Walk|Walk|Wall|Way|Ways|Wl|Wls"
    standard_address_pattern = r"(?P<civic_no>\w?\d+(\-\d+)?\w?\s+)(?P<rd_nm>[a-zA-z \d\-\']+)\s+(?P<rd_tp>" +  Address_suffix_opts + ")"
    #print("Road Attr Pattern: ", standard_address_pattern)
    road_attrs = re.search(standard_address_pattern, proc_addr)
    try:
        civic_num = road_attrs.group('civic_no').strip()
    except AttributeError:
        civic_num = ""
    #print("Road number: ", road_num)
    try:
        road_name = road_attrs.group('rd_nm').strip()
    except AttributeError:
        road_name = ""
    #print("Road name: ", road_name)
    try:
        road_type = road_attrs.group('rd_tp').strip()
    except AttributeError:
        road_type = ""
    #print("Road type: ", road_type)
    #clean_address=[]
    address=unit_num,building_num,civic_num,road_name,road_type,Street_direction
    #clean_address.append(address)
    clean_address = list(address)

    clean_address = [x for x in clean_address if x != '']

    clean_address=(' '.join(clean_address))

    return clean_address

# %%
def clean_address_without_unitnum(address):

    #print("input address:",address)
    address = Address_suffix_Standardize(address)
    address = Unit_designators_Standardize(address)
    address = Street_directions_Standardize(address)

    '''Checks for address after normalization and puts them in the standard format'''

    #print("address after normalization:",address)
    ####################################################################################
    ########################         Unit_Num            ###############################
    ####################################################################################
    # pattern for apt number/suit number/unit number 
    unit_nums = re.findall(r"(?<=Unit)\s*\w?\d+\w?|(?<=Floor)\s*\w*\d+\w*|(?<=\#)\s*\w?\d+\w?|(?<=Apt)\s*\w?\d+\w?|(?<=Suite)\s*\w?\d+\w?|\w?\d+\w?(?=\s*/)|\w?\d+\w?(?=\s*-)|[1-9]*(?=\s\d+\b)", address)
    unit_num = '#'+unit_nums[0].strip() if len(unit_nums) >= 1 else ""
    # Trim the unit designnator & punctuation 
    proc_addr = re.sub(
        r"Unit\s*\w?\d+\w?/?|Apt\s*\w?\d+\w?/?|Suite\s*\d+\w?/?|\w?\d+\w?\s*/|\w?\d+\w?\s*-|[1-9]*(?=\s\d+\b)", "", address)
    proc_addr = re.sub(r"^[,\-\/ ]+|[,\-\/ ]+$", "", proc_addr)

    #print("Unitless address: ", proc_addr)
    ####################################################################################
    ########################         Building_Num        ###############################
    ####################################################################################
    # pattern for building # A/B/C/D
    Building_nums = re.findall(r"\s[ABCD]{1}\s", proc_addr)
    building_num = Building_nums[0].strip() if len(Building_nums) == 1 else ""
 
    # Trim the building number
    proc_addr = re.sub(r"\s[ABCD]{1}\s", " ", proc_addr)
    #print("Buildingless address: ", proc_addr)
    ####################################################################################
    ########################         Street_direction          #########################
    ####################################################################################
    Street_directions = re.findall(r"\b\sE\b|\b\sN\b|\b\sNE\b|\b\sNW\b|\b\sS\b|\b\sSE\b|\b\sSW\b|\b\sSW\b|\b\sW\b", proc_addr)
    Street_direction = Street_directions[0].strip() if len(Street_directions) >= 1 else ""
 
    #Trim the building number
    proc_addr = re.sub(r"\s\bE\b|\s\bN\b|\s\bNE\b|\s\bNW\b|\s\bS\b|\s\bSE\b|\s\bSW\b|\s\bSW\b|\s\bW\b", "", proc_addr)
    #print("street direction less address: ", proc_addr)
    ####################################################################################
    ######################## RegEx Named Capture Group        #########################
    ####################################################################################
    Address_suffix_opts = r"Aly|Anx|Arc|Ave|Byu|Bch|Bnd|Blf|Blfs|Btm|Blvd|Br|Brg|Brk|Brks|Bg|Bgs|Byp|Cp|Cyn|Cpe|Cswy|Ctr|Ctrs|Cir|Cirs|Clf|Clfs|Clb|Cmn|Cmns|Cor|Cors|Crse|Ct|Cts|Cv|Cvs|Crk|Cres|Crst|Xing|Xrd|Xrds|Curv|Dl|Dm|Dv|Dr|Drs|Est|Ests|Expy|Ext|Exts|Fall|Fls|Fry|Fld|Flds|Flt|Flts|Frd|Frds|Frst|Frg|Frgs|Frk|Frks|Ft|Fwy|Gdn|Gdns|Gtwy|Gln|Glns|Grn|Grns|Grv|Grvs|Hbr|Hbrs|Hvn|Hts|Hwy|Hl|Hls|Holw|Inlt|Is|Iss|Isle|Jct|Jcts|Ky|Kys|Knl|Knls|Lk|Lks|Land|Lndg|Ln|Line|Lgt|Lgts|Lf|Lck|Lcks|Ldg|Loop|Mall|Mnr|Mnrs|Mdw|Mdws|Mews|Ml|Mls|Msn|Mtwy|Mt|Mtn|Mtns|Nck|Orch|Oval|Opas|Park|Park|Pkwy|Pkwy|Pass|Psge|Path|Pike|Pne|Pnes|Pl|Pln|Plns|Plz|Pt|Pts|Prt|Prts|Pr|Radl|Ramp|Rnch|Rpd|Rpds|Rst|Rdg|Rdgs|Riv|Rd|Rds|Rte|Row|Rue|Run|Shl|Shls|Shr|Shrs|Skwy|Spg|Spgs|Spur|Spur|Sq|Sqs|Sta|Stra|Strm|St|Sts|Smt|Ter|Trwy|Trce|Trak|Trfy|Trl|Trlr|Tunl|Tpke|Upas|Un|Uns|Vly|Vlys|Via|Vw|Vws|Vlg|Vlgs|Vl|Vis|Walk|Walk|Wall|Way|Ways|Wl|Wls"
    standard_address_pattern = r"(?P<civic_no>\w?\d+(\-\d+)?\w?\s+)(?P<rd_nm>[a-zA-z \d\-\']+)\s+(?P<rd_tp>" +  Address_suffix_opts + ")"
    #print("Road Attr Pattern: ", standard_address_pattern)
    road_attrs = re.search(standard_address_pattern, proc_addr)
    try:
        civic_num = road_attrs.group('civic_no').strip()
    except AttributeError:
        civic_num = ""
    #print("Road number: ", road_num)
    try:
        road_name = road_attrs.group('rd_nm').strip()
    except AttributeError:
        road_name = ""
    #print("Road name: ", road_name)
    try:
        road_type = road_attrs.group('rd_tp').strip()
    except AttributeError:
        road_type = ""
    #print("Road type: ", road_type)
    #clean_address=[]
    address=building_num,civic_num,road_name,road_type,Street_direction
    #clean_address.append(address)
    clean_address = list(address)

    clean_address = [x for x in clean_address if x != '']

    clean_address=(' '.join(clean_address))

    return clean_address

# %%

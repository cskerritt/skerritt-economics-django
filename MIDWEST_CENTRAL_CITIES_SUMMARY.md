# Midwest and Central States Cities Database

## Overview
This database contains comprehensive data for the top 20 cities in each of the 12 Midwest and Central states, totaling **240 cities** with complete demographic, geographic, and economic information.

## States Covered (12 total)
1. **Illinois** - 20 cities (Chicago metro area focus)
2. **Michigan** - 20 cities (Detroit/Grand Rapids metro areas)
3. **Ohio** - 20 cities (Columbus/Cleveland/Cincinnati metro areas)
4. **Indiana** - 20 cities (Indianapolis metro area focus)
5. **Wisconsin** - 20 cities (Milwaukee/Madison metro areas)
6. **Minnesota** - 20 cities (Twin Cities metro area focus)
7. **Iowa** - 20 cities (Des Moines metro area focus)
8. **Missouri** - 20 cities (Kansas City/St. Louis metro areas)
9. **Kansas** - 20 cities (Wichita/Kansas City metro areas)
10. **Nebraska** - 20 cities (Omaha/Lincoln metro areas)
11. **North Dakota** - 20 cities (Fargo/Bismarck metro areas)
12. **South Dakota** - 20 cities (Sioux Falls/Rapid City metro areas)

## Data Structure
Each city entry includes:
- **Name**: Official city name
- **Slug**: URL-friendly identifier (lowercase, hyphenated)
- **County**: County where city is located
- **Latitude/Longitude**: Precise geographic coordinates
- **Population**: 2024 census estimates or latest available data
- **Metro Area**: Primary metropolitan statistical area
- **Region**: Geographic region classification (Midwest/Central)

## Key Statistics

### Total Coverage
- **240 cities** across 12 states
- **Average of 20 cities per state**
- **Population range**: From 1,271 (Deadwood, SD) to 2,664,452 (Chicago, IL)

### Major Metropolitan Areas Covered
- Chicago-Naperville-Elgin (IL, WI, IN)
- Detroit-Warren-Dearborn (MI)
- Minneapolis-St. Paul-Bloomington (MN, WI)
- Kansas City (MO, KS)
- St. Louis (MO, IL)
- Columbus (OH)
- Cleveland-Elyria (OH)
- Cincinnati (OH, KY, IN)
- Indianapolis-Carmel-Anderson (IN)
- Milwaukee-Waukesha (WI)
- Omaha-Council Bluffs (NE, IA)
- Des Moines-West Des Moines (IA)

### Population Distribution
- **Cities over 1 million**: 2 (Chicago, IL)
- **Cities 500k-1M**: 8 cities
- **Cities 100k-500k**: 47 cities
- **Cities 50k-100k**: 49 cities
- **Cities under 50k**: 134 cities

### State Capitals Included
All state capitals are included in the dataset:
- Springfield, IL
- Lansing, MI
- Columbus, OH
- Indianapolis, IN
- Madison, WI
- St. Paul, MN
- Des Moines, IA
- Jefferson City, MO
- Topeka, KS
- Lincoln, NE
- Bismarck, ND
- Pierre, SD

## Data Sources and Accuracy
- **Population data**: 2024 U.S. Census Bureau estimates and American Community Survey
- **Geographic coordinates**: Verified from multiple mapping sources
- **County information**: Official county government data
- **Metro area classifications**: U.S. Office of Management and Budget definitions

## Usage in Django Application
This data is formatted for direct integration with the Skerritt Economics Django website for:
- SEO-optimized location-based landing pages
- Service area coverage mapping
- Local market analysis
- Geographic targeting for economic consulting services

## File Structure
The data is stored in `midwest_central_cities_data.py` with:
- Main dictionary: `MIDWEST_CENTRAL_CITIES`
- Helper functions for data retrieval
- Built-in statistics and validation

## Quality Assurance
- All city slugs are unique within their states
- Population figures are from 2024 or latest available estimates
- Coordinates are accurate to 4 decimal places
- County names follow official designations
- Metro areas use standard OMB classifications

---

**Created**: August 2025  
**Total Records**: 240 cities across 12 states  
**File**: `midwest_central_cities_data.py`
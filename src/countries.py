from typing import List

from src.constants import (
    COUNTRY_CODE_TO_ADMIN_LEVELS,
    COUNTRY_CODE_TO_NAME,
    COUNTRY_CODE_TO_OSM_ID,
    OSM_ID_TO_COUNTRY_CODE
)


def get_admin_level(country_code: str) -> List[str]:
    """
    Get the admin levels of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: Admin levels
    """
    return COUNTRY_CODE_TO_ADMIN_LEVELS[country_code]


def get_admin_levels(country_codes: List[str]) -> List[str]:
    """
    Get the admin levels of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: Admin levels
    """
    return [COUNTRY_CODE_TO_ADMIN_LEVELS[country_code] for country_code in country_codes]


def get_country_code(osm_id: str) -> str:
    """
    Get the country code of a country given its OSM ID

    Args:
        osm_id (str): OSM ID of the country

    Returns:
        str: Country code in ISO 3166 alpha-2 format
    """
    return OSM_ID_TO_COUNTRY_CODE[osm_id]


def get_country_codes(osm_ids: List[str]) -> List[str]:
    """
    Get the country codes of a list of countries given their OSM IDs

    Args:
        osm_ids (List[str]): OSM IDs of the countries

    Returns:
        List[str]: Country codes in ISO 3166 alpha-2 format
    """
    return [OSM_ID_TO_COUNTRY_CODE[osm_id] for osm_id in osm_ids]


def get_name(country_code: str) -> str:
    """
    Get the name of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: Name of the country
    """
    return COUNTRY_CODE_TO_NAME[country_code]


def get_names(country_codes: List[str]) -> List[str]:
    """
    Get the names of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: Names of the countries
    """
    return [COUNTRY_CODE_TO_NAME[country_code] for country_code in country_codes]


def get_osm_id(country_code: str) -> str:
    """
    Get the OSM ID of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: OSM ID of the country
    """
    return COUNTRY_CODE_TO_OSM_ID[country_code]


def get_osm_ids(country_codes: List[str]) -> List[str]:
    """
    Get the OSM IDs of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: OSM IDs of the countries
    """
    return [COUNTRY_CODE_TO_OSM_ID[country_code] for country_code in country_codes]

# OSM Mapping

This library helps Citibeats projects to centralize the mapping between all different countries and their data (such as the country code, the name, the admin levels and the OSM ID)

## Format of the data

### Countries

The country [codes](https://restcountries.com/v3.1/independent?status=true&fields=name,cca2,languages) follows the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) international standard and they are formatted as an Alpha-2 code.

## Usage

### `osm_mapping.countries`

- `get_admin_level`

```python
def get_admin_level(country_code: str) -> List[str]:
    """
    Get the admin levels of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: Admin levels
    """
```

- `get_admin_levels`

```python
def get_admin_levels(country_codes: List[str]) -> List[str]:
    """
    Get the admin levels of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: Admin levels
    """
```

- `get_country_code`

```python
def get_country_code(osm_id: str) -> str:
    """
    Get the country code of a country given its OSM ID

    Args:
        osm_id (str): OSM ID of the country

    Returns:
        str: Country code in ISO 3166 alpha-2 format
    """
```

- `get_country_codes`

```python
def get_country_codes(osm_ids: List[str]) -> List[str]:
    """
    Get the country codes of a list of countries given their OSM IDs

    Args:
        osm_ids (List[str]): OSM IDs of the countries

    Returns:
        List[str]: Country codes in ISO 3166 alpha-2 format
    """
```

- `get_name`

```python
def get_name(country_code: str) -> str:
    """
    Get the name of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: Name of the country
    """
```

- `get_names`

```python
def get_names(country_codes: List[str]) -> List[str]:
    """
    Get the names of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: Names of the countries
    """
```

- `get_osm_id`

```python
def get_osm_id(country_code: str) -> str:
    """
    Get the OSM ID of a country given its country code

    Args:
        country_code (str): Country code in ISO 3166 alpha-2 format

    Returns:
        str: OSM ID of the country
    """
```

- `get_osm_ids`

```python
def get_osm_ids(country_codes: List[str]) -> List[str]:
    """
    Get the OSM IDs of a list of countries given their country codes

    Args:
        country_codes (List[str]): Country codes in ISO 3166 alpha-2 format

    Returns:
        List[str]: OSM IDs of the countries
    """
```

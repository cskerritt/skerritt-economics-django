# Settings Configuration

## Optional: Configurable Data File Path

You can optionally configure the location of the locations.json data file by adding the following to your Django settings:

```python
# Path to the locations data file (optional)
LOCATION_DATA_FILE = '/path/to/your/locations.json'
```

Alternatively, you can set the `LOCATION_DATA_FILE` environment variable:

```bash
export LOCATION_DATA_FILE=/path/to/your/locations.json
```

If neither is set, the default path `main/data/locations.json` will be used.

## Development Mode

The `clear_cache()` function in `main.utils.data_loader` is restricted to development mode only. Ensure `DEBUG = True` in your settings when developing locally.
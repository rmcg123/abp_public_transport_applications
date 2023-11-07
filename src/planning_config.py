"""Configuration settings for transport planning analysis."""

DATA_FOLDER = "data/"
OUTPUTS_FOLDER = "results/"

ABP_BASE_URL = "https://www.pleanala.ie/en-ie/case/"

PROJECT_DETAILS = {
    "Rail": {
        "Metrolink": 314724,
        "Dart+ West": 314232,
        "Dart+ South West": 316119,
        "GMTT": 315087,
        "DCLC": 310286,
    },
    "Bus": {
        "BCD 1": 313182,
        "BCD 2": 317121,
        "BCD 3/4": 314610,
        "BCD 5": 313892,
        "BCD 6": 314942,
        "BCD 7": 314056,
        "BCD 8/9": 316828,
        "BCD 10/12": 316272,
        "BCD 11": 317660,
        "BCD 13": 317742,
        "BCD 14/15": 313509,
        "BCD 16": 317679,
        "BCG CCL": 314597,
    },
}

PROJECT_ACRONYMS = {
    "BCD": "Bus Connects Dublin Core Bus Corridor",
    "BCG CCL": "Bus Connects Galway Cross-City Link",
    "GMTT": "Glounthaune to Midleton Twin Tracking",
    "DCLC": "Dublin-Cork Line Level Crossing Closures",
}

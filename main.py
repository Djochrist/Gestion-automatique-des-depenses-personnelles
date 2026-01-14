from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def main() -> None:
    """Pipeline ETL principal."""
    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)


if __name__ == "__main__":
    main()

